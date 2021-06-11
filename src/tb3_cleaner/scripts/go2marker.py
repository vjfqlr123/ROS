#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose
from math import degrees, radians, sin, cos, pi
from geometry_msgs.msg import Twist
from ar_track_alvar_msgs.msg import AlvarMarkers
from tf.transformations import euler_from_quaternion
        
TARGET_ID =  5
MAX_SPEED =  0.22
SPEED = MAX_SPEED * 0.75
LIM_NEAR  =  0.20
LIM_FAR   =  0.30        


class RotoSt:

    def __init__(self):
    
        rospy.init_node('rotate_to_straight', anonymous = True)   
        
        rospy.Subscriber('/tb3pose', Pose, self.get_tb3_pose)     
        rospy.Subscriber('/ar_pose_marker', AlvarMarkers, self.get_marker )
        
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
        
        self.tw = Twist()
        self.tw.angular.z = SPEED
        
        # move_straight
        self.st_dist = 0
        
        # roatate, get_tb3_pose
        self.theta_start = 0
        self.theta_end   = 0
        self.tb3_theta_now   = 0
        self.tb3_dist_x = 0
        
        # get_ar_pose
        self.dist_x = 0
        self.dist_y = 0
        self.theta = 0
        
        # get_marker_pose
        self.x = 0
        self.y = 0
        self.th = 0
        
        # fix_dist_y
        self.fixing_dist_y = 0
        
        # get_marker
        self.is_1st_find = True
        self.is_1st_lost = True
        self.align_finished = False
        self.go2front_complete = False
        self.align_center = False
        self.fix_dist_y_clear = False
        
        # ar_center_tb3
        self.reverse_clear = False
    
    def get_marker(self, msg):
        
        self.pub.publish(self.tw)
        
        if len(msg.markers) > 0:            # found marker at least 1 more
        
            for msg in msg.markers:
            
                if msg.id == TARGET_ID:
                    print "found target marker"
                    
                    self.dist_x, self.dist_y, theta = self.get_ar_pose(msg)
                    
                    if self.fix_dist_y_clear == False:
                        self.fixing_dist_y = self.dist_y
                        self.fix_dist_y_clear = True
                                      
                    self.st_dist = msg.pose.pose.position.z
                    
                    if  (theta >  5.0):
                        self.theta = theta - 2 * pi            
                    elif(theta < -5.0):
                        self.theta = theta + 2 * pi
                    else:
                        self.theta = theta
                    
                    
                    if self.is_1st_find == True:
                        self.theta_start = self.tb3_theta_now
                        print "get start theta value"
                        self.is_1st_find = False
                    
                    if self.align_finished == True:
                        if self.go2front_complete == False and self.fix_dist_y_clear == True:
                            
                            self.get_marker_pose()
                            self.ar_center_tb3()
                            self.go2front_complete = True
                            print "()"
                            
                    
                        if self.go2front_complete == True:
                            self.move_straight()
                            print "1234"  
                    
                else:
                    print "id mismatch"
                
            

        else: # lost marker
            print "lost marker"
            
            if self.is_1st_find == False and self.is_1st_lost == True:
                self.theta_end = self.tb3_theta_now
                print "get end value"
                self.is_1st_lost = False
                
                if self.align_finished == False:
                    
                    self.roatate()
                    self.get_marker_pose()
                    self.align_finished = True  
                     
    
    def ar_center_tb3(self):
        
        if self.y > 0:
            print "123123"
            
            current = self.tb3_theta_now        
            target = current + self.th
            self.tw.angular.z = SPEED
            self.pub.publish(self.tw)
            while self.tb3_theta_now > target: pass
            
            self.tw.angular.z = 0
            self.pub.publish(self.tw)
            ########################################
            duration = self.y / SPEED
            time2end = rospy.Time.now() + rospy.Duration(duration)
            self.tw.linear.x = MAX_SPEED / 4
            self.pub.publish(self.tw)
        
            while rospy.Time.now() < time2end: pass
            
            self.tw.linear.x = 0
            self.pub.publish(self.tw)
            ########################################
            current = self.tb3_theta_now
            target = current - 0.5 * pi
            self.tw.angular.z = SPEED
            self.pub.publish(self.tw)
            while self.tb3_theta_now > target: pass
      
        else:
            print "234234"
          
            target = radians(pi/2) - self.theta
            self.tw.angular.z = -SPEED
            self.pub.publish(self.tw)
            while self.tb3_theta_now > target: pass
            
            self.tw.angular.z = 0
            self.pub.publish(self.tw)
            
            self.reverse_clear = True
            print '1111'
            ########################################
            if self.reverse_clear == True:
                print '2222'
                print(self.dist_y)
                print(self.y)
                print(self.fixing_dist_y)
                
                duration = abs(self.fixing_dist_y / SPEED)
                time2end = rospy.Time.now() + rospy.Duration(duration)
                self.tw.linear.x = MAX_SPEED / 4
                self.pub.publish(self.tw)
                
                while rospy.Time.now() < time2end:
                    #print(rospy.Time.now())
                    #print'========='
                    #print(time2end)
                    #print'777777777'
                    pass
                
                print(self.dist_y)
                print(self.y)
                print(self.fixing_dist_y)
            
                self.tw.linear.x = 0
                self.pub.publish(self.tw)
            ########################################
            
            
            current = self.theta
            target = current + 0.5 * pi
            self.tw.angular.z = SPEED
            self.pub.publish(self.tw)
            while self.theta > target: pass
            
            print '4444'
            
        self.tw.angular.z = 0
        self.pub.publish(self.tw)
            
        print "tb3-----marker"

    def move_straight(self):
        
        if self.st_dist > LIM_FAR:
            self.tw.linear.x = MAX_SPEED / 4
        
        elif self.st_dist < LIM_NEAR:
            self.tw.linear.x = -MAX_SPEED / 4
        
        else:
            self.tw.linear.x = 0
            print "WOW"
            
        self.pub.publish(self.tw)
        rospy.sleep(0.01)
    
    def roatate(self):
        print "find marker stop"
        self.tw.angular.z = 0
        self.pub.publish(self.tw)
        rospy.sleep(0.05)
        
        current = self.tb3_theta_now        
        target = current - abs(self.theta_start - self.theta_end) * 0.7
        print "get target value"
        
        self.tw.angular.z = -SPEED        
        self.pub.publish(self.tw)
        rospy.sleep(0.05)
        
        while self.tb3_theta_now > target:
            pass
        
        self.tw.angular.z = 0
        self.pub.publish(self.tw)
        rospy.sleep(0.05)
        print "align complete"
        
    def get_ar_pose(self, msg):
        q = (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, 
             msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
             
        quart = euler_from_quaternion(q)
        theta = quart[1]
        
        if theta < 0:
            theta = theta + pi * 2
        if theta > pi * 2:
            theta = theta - pi * 2
        
        dist_x =  msg.pose.pose.position.z * cos(theta)
        dist_y =  msg.pose.pose.position.z * sin(theta)

        return dist_x, dist_y, theta 
    
    def get_tb3_pose(self, dat):
    
        self.tb3_theta_now = dat.theta
        self.tb3_dist_x = dat.x
    
    def get_marker_pose(self):
        self.x = self.dist_x
        self.y = self.dist_y
        self.th = self.theta
        print "dist_x = %f, dist_y = %f, theta = %f" %(self.x, self.y, degrees(self.th))    
   

if __name__ == '__main__':
    try:
        
        RotoSt()
        rospy.spin()
        
    except rospy.ROSInterruptException:  pass        
