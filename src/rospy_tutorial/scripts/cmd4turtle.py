#!/usr/bin/env python

import rospy
import geometry_msgs.msg

def move_turtle():
    rospy.init_node("move_turtle")
    pub = rospy.Publisher("turtle1/cmd_vel", geometry_msgs.msg.Twist, queue_size=10)
    tw  = geometry_msgs.msg.Twist()
    tw.linear.x = 0.3
    tw.angular.z = 0.2
    pub.publish(tw)
   
if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            move_turtle()
            
    except rospy.ROSInterruptException:
        print "Program terminated!"
