#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from math import pi, radians

SPEED = 1.0

class Pub_Tb3_Pose:

    def __init__(self):
        rospy.init_node('sub_tb3_pose')#, anonymous=True)
        rospy.Subscriber('/odom', Odometry, self.get_pose)
        self.pb = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
        self.tw = Twist()
        self.th = 0
        
        
        
    def get_pose(self, dat):
        self.th = dat.pose.pose.orientation.z * pi
        #rospy.loginfo("ang_z = %s(rad) = %s(deg)" ang_z*pi, ang_z*180)
            
    def pub_turtlebot3_pose(self):
        
        angle = radians(input("input angle to turn(deg): "))
        th_now = self.th
        
        if angle < 0:
            self.tw.angular.z = -SPEED
            if th_now < 0:
                if abs(angle) < abs(pi-th_now):
                    while self.th > abs(th_now) + abs(angle):
                        self.pb.publish(tw)
                    self.tw.angular.z = 0
                    self.pb.publish(tw)
            
            else:
            
            
        else:
            tw.angular.z = SPEED
        
        od.pose.pose.orientation.z = self.ang_z
        rospy.spin()
    
if __name__ == '__main__':
    tb3 = Pub_Tb3_Pose()
    tb3.pub_turtlebot3_pose()
