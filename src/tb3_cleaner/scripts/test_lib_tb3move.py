#!/usr/bin/env python
'''
################################################################################
#  Be sure the topic("/tb3pose") has to be published before start this code!!! #
################################################################################
'''
import rospy
from tb3_cleaner.MoveTB3 import MoveTB3 # <---- import like this
'''  ----------- -------        -------
          ^         ^              ^
src/tb3_cleaner > MoveTB3.py > class MoveTB3:
'''
from math import radians

if __name__ == '__main__':

    try:        
        tb3 = MoveTB3()
        angle = radians(input("input angle to rotate(deg): "))
        tb3.rotate(angle)
        dist = float(input("input distance to stright(m): "))
        tb3.straight(dist)
        rospy.spin()
        
    except rospy.ROSInterruptException:  pass
