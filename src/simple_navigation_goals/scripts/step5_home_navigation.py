#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
import rosmaster.master_api
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

destination1 = [[1.88, 0.0, 0.0], [0.0, 0.0, 0.0]]
orientation = (0.0, 0.0, 0.0, 1.0)


def movebase_client(dest, orient):

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = dest[0]
    goal.target_pose.pose.position.y = dest[1]
    goal.target_pose.pose.position.z = dest[2]
    goal.target_pose.pose.orientation.x = orient[0]
    goal.target_pose.pose.orientation.y = orient[1]
    goal.target_pose.pose.orientation.z = orient[2]
    goal.target_pose.pose.orientation.w = orient[3]

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()
        

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        while not rospy.core.is_shutdown():
            arrive = rospy.get_param("/step4_move_back/back_move_end") 
            
            if arrive :
                i = 0
                while i < 2:
                    movebase_client(destination1[i], orientation) 
                    i = i + 1         
                 
                rospy.loginfo("Goal execution done!")
                rospy.set_param("/step4_move_back/back_move_end", False)
                
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
