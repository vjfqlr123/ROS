#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

destination = [[1.3, -0.6, 0.0], [1.5, 0.4, 0.0], [-1.7, 0.3, 0.0]]
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
        for i in range(3):
            result = movebase_client(destination[i], orientation)
            if result:
                rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
