#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose
from math import degrees, pi
from geometry_msgs.msg import Twist
from ar_track_alvar_msgs.msg import AlvarMarkers
#from tf.transformations import euler_from_quaternion

TARGET_ID =  5
LIM_NEAR = 0.15
LIM_FAR = 0.20
MAX_SPEED = 0.22

class MarkerPose:

    def __init__(self):
    
        rospy.init_node('tb3_keep_dist', anonymous = True)        
        rospy.Subscriber('/ar_pose_marker', AlvarMarkers, self.get_marker )
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
        self.dist = 0
        
    def get_marker(self, msg):
    

        for msg in msg.markers:
            if msg.id == TARGET_ID:
            
                self.dist = msg.pose.pose.position.z
                self.move2marker()
        

    def move2marker(self):
        
        tw = Twist()
        
        if self.dist > LIM_FAR:
            tw.linear.x = MAX_SPEED / 4
        
        elif self.dist < LIM_NEAR:
            tw.linear.x = -MAX_SPEED / 4
        
        else:
            tw.linear.x = 0
            
        self.pub.publish(tw)
          

if __name__ == '__main__':
    try:
        
        MarkerPose()
        rospy.spin()
        
    except rospy.ROSInterruptException:  pass
