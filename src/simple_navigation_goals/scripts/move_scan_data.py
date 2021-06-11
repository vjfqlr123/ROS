#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from math import degrees, radians, sin, cos, pi
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

# Turtlebot3 Specification
MAX_LIN_SPEED =  0.02

# set parking zone(kind of tolerlance)
MAX_DIST = 0.103

class ALMOST:
    def __init__(self):
        rospy.init_node('scanning', anonymous = True, disable_signals = False)
        rospy.Subscriber('/dist_scan', Float32, self.get_scan_info)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
           
        self.tw = Twist()
        self.tw.linear.x = MAX_LIN_SPEED
        
        self.dist = 0


    def get_scan_info(self, msg):
        self.pub.publish(self.tw)
        self.dist = msg
        print(self.dist.data)
        
        if self.dist.data < MAX_DIST:
            print("======================")
            self.tw.linear.x = 0
            self.pub.publish(self.tw)
            rospy.signal_shutdown(True)
        
    
        
if __name__ == '__main__':
    try:
     
        ALMOST()
            
        rospy.spin()            
           
                   
        
    except rospy.ROSInterruptException:
        pass        
