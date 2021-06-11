#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from math import pi

def get_pose(dat):
    ang_z = dat.pose.pose.orientation.z
    rospy.loginfo("ang_z = %s(rad) = %s(deg)" ang_z*pi, ang_z*180)
        
def sub_turtlebot3_pose():
    rospy.init_node('sub_turtlebot3_pose')#, anonymous=True)
    rospy.Subscriber('/odom', Odometry, get_pose)
    rospy.spin()
    
if __name__ == '__main__':
    sub_turtlebot3_pose()
