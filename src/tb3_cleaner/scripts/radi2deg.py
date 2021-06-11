#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from math import degrees, radians, pi, sin, asin

SPEED = 1.0

class Test:
    
    def cb_func(self, dat):
        self.th = dat.pose.pose.orientation.z

    def simple_sub_pub(self):
        rospy.init_node('pose_odom_rotate')
        sub = rospy.Subscriber('/odom', Odometry, self.cb_func)
        
        # Receiveing the user's input
        print("input speed within 0 ~ 360")
        angle     = input("Type your distance (degrees):")
        
        print(degrees(2*asin(self.th)))
        
        radi = sin(radians(angle)/2)
        print(radi)
        
        
        
if __name__ == '__main__':
    sh = Test()
    sh.simple_sub_pub() 
