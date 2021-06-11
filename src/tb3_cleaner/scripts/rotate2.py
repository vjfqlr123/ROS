#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from math import degrees, radians, pi, sin, asin

SPEED = 0.5

class SIM:

    def cb_func(self, dat):
        self.th = dat.pose.pose.orientation.z
        self.th2 = degrees(2*asin(self.th))

    def simple_sub_pub(self):
        rospy.init_node('pose_odom_rotate')
        sub = rospy.Subscriber('/odom', Odometry, self.cb_func)
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        msg = Twist()
        
        # Receiveing the user's input
        print("input speed within 0 ~ 360")
        angle     = input("Type your distance (degrees):")
        
        radi = sin(radians(angle)/2)
        print(radi)
        
        print(self.th2)
        print("direction cw:1, ccw:0")
        clockwise = input("Clockwise?: ")
        
        th_now = self.th
        th_now2 = self.th2
        
        if th_now > 0:
            if clockwise:
                if th_now + radi <= 1:
                    msg.angular.z = SPEED
                    pub.publish(msg)
                    while self.th < radi:
                        
                        print(radi)
                        print(self.th)
                        print(self.th2)
                        
                    msg.angular.z = 0
                    pub.publish(msg)
                    print('==')
                else:
                    th_rep = 1- th_now
                    th_rem = th_rep - 1
                    while self.th2 < 1:
                        msg.angular.z = th_rep
                        pub.publish(msg)
                    msg.angular.z = 0
                    pub.publish(msg)
                    while self.th2 < th_rem:
                        msg.angular.z = abs(th_rem)
                        pub.publish(msg)
                    msg.angular.z = 0
                    pub.publish(msg)                    
            else:
                pass
            
        else:
            pass
        
        msg.angular.z = 0    
        pub.publish(msg)
        
        rospy.spin()

if __name__ == '__main__':
    sh = SIM()
    sh.simple_sub_pub() 
