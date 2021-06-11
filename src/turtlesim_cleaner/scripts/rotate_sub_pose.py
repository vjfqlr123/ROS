#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def rotate():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    msg = Twist()
    
    # Receiveing the user's input
    angle     = input("Type your distance (degrees):")
    clockwise = input("Clockwise?: ") # True or false
    
    # Converting from angles to radians
    relative_angle = angle*2*PI/360
