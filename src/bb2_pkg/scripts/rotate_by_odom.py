#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Empty
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from math import degrees, radians, pi, sin, asin
from tf.transformations import euler_from_quaternion

ANG_SPD = 0.5

class BB2_Rotate:

    def __init__(self):    
        rospy.init_node('bb2_turn_by_odom', anonymous = True)
                
        rospy.Subscriber('/bebop/odom', Odometry, self.get_odom_cb)
        
        self.pub0 = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size = 1)
        self.pub1 = rospy.Publisher('/bebop/takeoff', Empty, queue_size = 1)
        self.pub2 = rospy.Publisher('/bebop/land',    Empty, queue_size = 1)
        self.pub3 = rospy.Publisher('/bebop/reset',   Empty, queue_size = 1)
        
        self.theta_now = 0.0
        self.prv_theta = 0.0
        self.theta_sum = 0.0
        self.theta_org = 0.0

        
    def get_odom_cb(self, dat):
        
        theta = self.get_theta(dat)

        
        if   (theta - self.prv_theta) >  5.0: #  5.0(rad) =  286.479(deg)
            d_theta = (theta - self.prv_theta) - 2 * pi            
        elif (theta - self.prv_theta) < -5.0: # -5.0(rad) = -286.479(deg)
            d_theta = (theta - self.prv_theta) + 2 * pi
        else:
            d_theta = (theta - self.prv_theta)

        self.theta_sum = self.theta_sum + d_theta
        self.prv_theta = theta
        
        self.theta_now = self.theta_sum     
        
    def get_theta(self, msg):
        
        q = (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, 
             msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
                                            # quart[0] = roll
        quart = euler_from_quaternion(q)    # quart[1] = pitch
        theta = quart[2]                    # quart[2] = yaw <----
        
    	# make theta within from 0 to 360 degree
        if theta < 0:
            theta = theta + pi * 2
        if theta > pi * 2:
            theta = theta - pi * 2

        return theta
        
    def print_theta(self, angle):
        print("theta = %f = %f" %(angle, degrees(angle)))

    def update_org(self):
        # save current tb3pose.theta to org.theta when called this function
        self.theta_org = self.theta_now 
        
    def elapsed_angle(self):
        return abs(self.theta_now - self.theta_org)
        
    def rotate(self, angle, tolerance):
        tw = Twist()
        self.update_org()
        print "start from: %s" %(round(degrees(self.theta_org), 2))
        
        if angle >= 0:	# angle(+): rotate left(ccw)
            tw.angular.z =  ANG_SPD;
        else:			# angle(-): rotate right(cw)
            tw.angular.z = -ANG_SPD;
            
        while self.elapsed_angle() < abs(angle) - tolerance:
            self.pub0.publish(tw)
            # print "%s of %s" %(round(degrees(self.elapsed_angle()),2) ,round(degrees(abs(angle)),2))
            
        tw.angular.z =  0;  self.pub0.publish(tw)
        rospy.sleep(1)
        print "stop to   : %s" %(round(degrees(self.theta_now), 2))              

if __name__ == '__main__':
    try:
        bb2 = BB2_Rotate()
        angle = radians(float(input("input angle(deg) to turn: ")))
        tolerance = float(input("input tolerance(0.0~0.5): "))
        bb2.rotate(angle, tolerance)
        rospy.spin()
        
    except rospy.ROSInterruptException:  pass
