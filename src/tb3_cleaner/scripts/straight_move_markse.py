#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose
from math import degrees, pi
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
             
        rospy.Subscriber('/ar_pose_marker', AlvarMarkers, self.get_marker )
        rospy.Subscriber('/tb3pose', Pose, self.get_tb3_pose)
        
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
        
        self.st_dist = 0
        
        self.tw = Twist()
        self.tw.angular.z = SPEED
        
        self.theta_now   = 0
        self.theta_start = 0
        self.theta_end   = 0
        
        self.is_1st_find = True
        self.is_1st_lost = True
        self.align_finished = False
        
    def get_tb3_pose(self, dat):
        self.theta_now = dat.theta

    
    def get_marker(self, msg):
        
        self.pub.publish(self.tw)
        
        if len(msg.markers) > 0:            # found marker at least 1 more
        
            for msg in msg.markers:
            
                if msg.id == TARGET_ID:
                    print "found target marker"
                    
                    if self.is_1st_find == True:
                        self.theta_start = self.theta_now
                        print "get start value"
                        self.is_1st_find = False
                    
                    elif self.align_finished == True and self.is_1st_find == False and self.is_1st_lost == False:
                    
                        print "tb3 move~~~"
                        self.st_dist = msg.pose.pose.position.z
                        self.straight()  
                
                else:
                    print "id mismatch"
                
            

        else: # lost marker
            print "lost marker"
            
            if self.is_1st_find == False and self.is_1st_lost == True:
                self.theta_end = self.theta_now
                print "get end value"
                self.is_1st_lost = False
                
                if self.align_finished == False:
                    
                    self.roatate()
                    self.align_finished = True   

    def straight(self):
        
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
        print "stop"
        self.tw.angular.z = 0
        self.pub.publish(self.tw)
        rospy.sleep(0.05)
        
        current = self.theta_now        
        target = current - abs(self.theta_start - self.theta_end) * 0.8
        print "get target value"
        
        self.tw.angular.z = -SPEED        
        self.pub.publish(self.tw)
        rospy.sleep(0.05)
        
        while self.theta_now > target:
            pass
        
        self.tw.angular.z = 0
        self.pub.publish(self.tw)
        rospy.sleep(0.05)
        print "align complete"
        
   

if __name__ == '__main__':
    try:
        
        RotoSt()
        rospy.spin()
        
    except rospy.ROSInterruptException:  pass        
