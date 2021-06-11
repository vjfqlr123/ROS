#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import degrees, radians, pi

SPEED = 1.0

class Rotate2:

    def __init__(self):
        rospy.init_node('sub_turtle_pose')#, anonymous=True)
        rospy.Subscriber('/turtle1/pose', Pose, self.get_pose)
        #self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist)
        #self.tw = Twist()
        
        
        
        self.x = self.y = self.th = 0

    def get_pose(self, dat):
        self.x  = round(dat.x, 2) 
        self.y  = round(dat.y, 2)
        self.th = round(dat.theta, 2)       
        
    def rotate2(self, angle):
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
        tw = Twist()
        
        
        if angle < 0:
            wise = -1
            speed = SPEED * wise
            while self.th >= angle:
                tw.angular.z = speed
                pub.Publish(tw)
            
        else:
            speed = SPEED
            while self.th <= angle:
                tw.angular.z = speed
                pub.publish(tw)
        
        
        tw.angular.z = 0
        pub.publish(tw)
        
if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            rt2 = Rotate2()
    
            ang = radians(float(input("input angle to turn(deg): ")))
            
            rt2.rotate2(ang)
            
            rospy.spin()
    except rospy.ROSInterruptException:
        pass
