#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32


class Scanning:
    def __init__(self):
        rospy.init_node('scanning', anonymous = True)
        rospy.Subscriber('/scan', LaserScan, self.check_target)
        self.pub = rospy.Publisher('/dist_scan', Float32, queue_size = 10)
        
    def check_target(self, msg):
        t1 = msg.ranges
        p = Float32()
        
        a = t1[0:50]
        b = t1[310:]        
        c = a + b    
           
        print(min(i for i in c if i > 0.05))        
        p = min(i for i in c if i > 0.05)
        self.pub.publish(p)    

if __name__ == '__main__':
    try:
        Scanning()
        rospy.spin()
        
    except rospy.ROSInterruptException:  pass
