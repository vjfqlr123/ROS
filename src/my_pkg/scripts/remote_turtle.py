#!/usr/bin/env python


import rospy                    
from geometry_msgs.msg import Twist
from my_lib.GetChar import GetChar


msg = '''
----------------------------
        (forward)
           'w'
(left)'a'  's'  'd'(right)
        (backward)
----------------------------
'''


def getKey():

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)

    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

rospy.init_node('remote_turtle', anonymous=True)

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

tw = Twist()
rate =  rospy.Rate(10)
kb = GetChar()

tw.linear.x = tw.linear.y = tw.linear.z = 0
tw.angular.x = tw.angular.y = tw.angular.z = 0 

count = 0
ch = 0

print msg

while not rospy.is_shutdown(): 
    ch = kb.getch()
    
    if ch == 'w':
        tw.linear.x = 2.0
        print "forward"
        
    elif ch == 's':
        tw.linear.x = -2.0
        print "backward"
        
    elif ch == 'a':
        tw.angular.z = 2.0
        print "left"
        
    elif ch == 'd':
        tw.angular.z = -2.0
        print "right"
    
    elif ch == 'Q':
        break
    
    else:
        pass
    
    pub.publish(tw)
    tw.linear.x = tw.angular.z = 0
    
    count += 1
    if count == 10:
        count = 0
        print msg
    
    
    rate.sleep()

'''
if __name__ == '__main__':  
    try:                    
        simple_pub()        
    except rospy.ROSInterruptException: 
        print "Program terminated"
'''
