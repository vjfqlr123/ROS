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
LIM_NEAR  =  0.15
LIM_FAR   =  0.20


class AlignMarker:

    def __init__(self):
    
        rospy.init_node('align_to_marker', anonymous = True)   
             
        rospy.Subscriber('/ar_pose_marker', AlvarMarkers, self.get_marker)       
        rospy.Subscriber('/tb3pose', Pose, self.get_tb3_pose)
        
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
        
        self.tw = Twist()
        self.tw.angular.z = SPEED
        
        self.theta_now   = 0
        self.theta_start = 0
        self.theta_end   = 0
        
        self.is_1st_find = True
        self.is_1st_lost = True
        self.align_finished = False
        
    def get_marker(self, msg):
        
        self.pub.publish(self.tw)
        
        if len(msg.markers) > 0:            # found marker at least 1 more
        

            if msg.markers[0].id == TARGET_ID:
                print "found target marker"
                
                if self.is_1st_find == True:
                    self.theta_start = self.theta_now
                    print "get start value"
                    self.is_1st_find = False
            
            else:
                print "id mismatch"
                
        else: # lost marker
            print "lost marker"
            
            if self.is_1st_find == False and self.is_1st_lost == True:
                self.theta_end = self.theta_now
                print "get end value"
                self.is_1st_lost = False
                
                if self.align_finished == False:
                    self.move2marker()
                    self.align_finished = True       
                          
        
    def get_tb3_pose(self, dat):
        self.theta_now = dat.theta
                             
    def move2marker(self):
        print "stop"
        self.tw.angular.z = 0
        self.pub.publish(self.tw)
        
        current = self.theta_now        
        target = current - abs(self.theta_start - self.theta_end) * 0.7
        print "get target value"
        
        self.tw.angular.z = -SPEED        
        self.pub.publish(self.tw)
        
        while self.theta_now > target:  pass
        
        self.tw.angular.z = 0
        self.pub.publish(self.tw)
        print "align complete"
          

if __name__ == '__main__':
    try:
        
        AlignMarker()
        rospy.spin()
        
    except rospy.ROSInterruptException:  pass
