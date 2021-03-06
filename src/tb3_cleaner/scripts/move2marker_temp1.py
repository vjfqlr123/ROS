#!/usr/bin/env python

import rospy
from math import degrees, radians, sin, cos, pi
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
from ar_track_alvar_msgs.msg import AlvarMarkers
from tf.transformations import euler_from_quaternion

TARGET_ID = 5

# Turtlebot3 Specification
MAX_LIN_SPEED =  0.05
ANG_SPEED =  0.1

# set parking zone(kind of tolerlance)
MAX_DIST = 0.10
MIN_DIST = 0.07


class Move2Marker:

    def __init__(self):
    
        rospy.init_node('move_to_marker', anonymous = True)       
        rospy.Subscriber('/tb3pose', Pose, self.get_tb3_pose)
        rospy.Subscriber('/ar_pose_marker', AlvarMarkers, self.get_marker_info)
        rospy.Subscriber('/marker_pose', Pose, self.get_marker_pose)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
        
        self.ang_speed = ANG_SPEED
        self.lin_speed = MAX_LIN_SPEED
        
        self.tw = Twist()
        self.tw.angular.z = self.ang_speed
        
        # get marker pose()
        self.marker = Pose()
        self.dist_x    = 0
        self.dist_y    = 0
        self.theta     = 0
        
        # get tb3 pose()
        self.tb3pose2d = Pose()
        self.curr_th   = 0
        

        # by odom --> center marker camera
        self.find_th   = 0
        self.lost_th   = 0
        
        # get_marker_pose()
        self.x         = 0
        self.y         = 0
        self.th        = 0
        self.dist      = 0
        
        self.wise      = 0
        self.count     = 0
        
        # misson complete
        self.right_case  = False
        self.left_case   = False
        self.center_case = False
        
        self.find_first_time_passed  = False
        self.lost_first_time_passed  = False
        
        self.step1_align2marker_end  = False
        self.step2_1st_rotation_end  = False
        self.step3_move_2_front_end  = False
        self.step4_2nd_rotation_end  = False
        self.step5_move_2_marker_end = False
        
        
    def get_marker_info(self, msg):
        
        self.pub.publish(self.tw)
        
        if len(msg.markers) > 0:

          
            for msg in msg.markers:
            
                if msg.id == TARGET_ID:
                
                    print "found target marker"
                    
                    self.dist = msg.pose.pose.position.z
                                                  
                
                    if  self.find_first_time_passed == False:
                        self.find_th  = self.curr_th
                        print('find_th(odom)', degrees(self.find_th))
                        print "## get tb3 theta to start recognize marker."
                        self.find_first_time_passed = True
                        
                    if self.step1_align2marker_end == True and self.step2_1st_rotation_end == False:

                        self.dist_x = self.marker.x
                        self.dist_y = self.marker.y
                        theta = self.marker.theta
                         
                        self.get_marker_pose_save()
                        
                        
                        print "theta = %f" %(degrees(theta))
                        
                                              
                        if theta >= 0:
                            angle = 0.5 * pi - theta
                            angle = angle * 0.95
                            
                        else:
                            angle = -(0.5 * pi + theta)
                            angle = angle * 0.95
                            
                        
                        self.rotate(angle)
                        print "angle = %f" %(degrees(angle))
                        self.step2_1st_rotation_end = True
                    
                    if self.step4_2nd_rotation_end == True and self.step5_move_2_marker_end == False:
                        self.approach()
                        
                    
                else:
                    print "id mismatch"
                    
                
        else: # lost marker            
            print "lost marker"
        
            if self.find_first_time_passed == True and self.lost_first_time_passed == False:
                self.lost_th = self.curr_th
                print('self.lost_th(odom)', degrees(self.lost_th))   
                print "## get tb3 theta to end recognize marker."
                self.lost_first_time_passed = True
                
            
            if self.lost_first_time_passed == True and self.step1_align2marker_end == False:
                self.align2marker()                    
                self.step1_align2marker_end = True
                
            if self.step2_1st_rotation_end == True and self.step3_move_2_front_end == False:
                
                print('self.y', self.y)
                if self.y < 0:
                    self.move(abs(self.y * 1.21))
                else:
                    self.move(abs(self.y * 1.1))
                self.step3_move_2_front_end = True
            
            if self.step3_move_2_front_end == True and self.step4_2nd_rotation_end == False:
                if self.y < 0:
                    self.rotate(radians(88))
                else:
                    self.rotate(-radians(88))
                    
                self.step4_2nd_rotation_end = True    
                  

    
    def get_marker_pose(self, msg):
        self.marker = msg
    
    def get_tb3_pose(self, msg):
        self.tb3pose2d = msg     
        self.curr_th = self.tb3pose2d.theta 

    def align2marker(self):
        print "## align ##"

        current = self.curr_th
        target = current - abs(self.find_th - self.lost_th) * 0.55

        self.tw.angular.z = -ANG_SPEED  
        self.pub.publish(self.tw)
        print('current(odom)', degrees(current))
        print('target(odom)', degrees(target))

        while self.curr_th > target:
            pass


        self.tw.angular.z = 0
        self.pub.publish(self.tw)
        rospy.sleep(5)

        print "align complete."
        
        
    def get_marker_pose_save(self):
        self.x = self.dist_x
        self.y = self.dist_y
        print "dist_x = %f, dist_y = %f" %(self.x, self.y)
                
    
    def rotate(self, angle):  
        
        self.count = self.count + 1
        print "## rotate %d" %(self.count)
        
        current_angle = self.curr_th
        target_angle  = current_angle + angle
        print "target_angle = %f, current_angle = %f" %(degrees(target_angle) ,degrees(current_angle))
        
        
        if angle > 0:
            self.tw.angular.z = ANG_SPEED
            self.pub.publish(self.tw)
            while target_angle > self.curr_th:  pass
            
        else:
            self.tw.angular.z = ANG_SPEED * -1
            self.pub.publish(self.tw)
            while target_angle < self.curr_th:  pass
            
        
        self.tw.angular.z = 0
        self.pub.publish(self.tw)
        print degrees(self.curr_th)
        rospy.sleep(5)
        
        
    def move(self, dist_y):
        speed = MAX_LIN_SPEED
        duration = 1.58 * dist_y / speed
        time2end = rospy.Time.now() + rospy.Duration(duration)
        
        print "## move for %f(sec)" %(duration)
        print('time2end', time2end)
        now = rospy.get_rostime()
        rospy.loginfo("Current time %i %i", now.secs, now.nsecs)
        
        self.tw.linear.x = self.lin_speed       
        self.pub.publish(self.tw)
        
        while time2end > rospy.Time.now():
            pass
        

        
        self.tw.linear.x = 0       
        self.pub.publish(self.tw) 
        rospy.sleep(3)
        
        
    def approach(self):
        print "## approach ##"
        '''
        # marker
        #   |        min    max
        #   |   --->  |      |  <---
        #   +---------+------+----------------
        #    backward   stop   forward 
        '''
        speed = MAX_LIN_SPEED

        if   self.dist > MAX_DIST:
            if self.dist - MAX_DIST > 0.20:
                self.tw.linear.x =  speed * 2.0
            else:
                self.tw.linear.x =  speed * 0.55
        elif self.dist < MIN_DIST:
            self.tw.linear.x =  speed * 0.45 * -1
            
        elif self.dist < MAX_DIST:
            self.tw.linear.x = 0
            self.pub.publish(self.tw)
            print "####### approach complete #########" 
    
        
        self.pub.publish(self.tw)        
        print "distance to marker = %f(cm)" %(self.dist * 100)
        


if __name__ == '__main__':
    try:
        #TARGET_ID = int(input("input marker id: "))
        Move2Marker()        
        rospy.spin()
        
    except rospy.ROSInterruptException:  pass
