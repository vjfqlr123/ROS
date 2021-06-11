#!/usr/bin/env python

import rospy
import open_manipulator_msgs
import ar_track_alvar_msgs
import sensor_msgs


if __name__ == "__main__":
    # Initialize moveit_commander and node
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('d1_get_basic_info', anonymous=False)
    #rospy.Subscriber('/ar_pose_marker', AlvarMarkers, self.get_marker_info)
    
    # Get instance from moveit_commander
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    # Get group_commander from MoveGroupCommander
    #group_name = "panda_arm"
    group_name = "arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)


    # Move using joint space
    joint_goal = move_group.get_current_joint_values()
    print joint_goal

    joint_goal[0] = 0
    joint_goal[1] = 0.008
    joint_goal[2] = 0.028
    joint_goal[3] = 0.006


    move_group.go(joint_goal, wait=True)
    move_group.stop()

    current_joints = move_group.get_current_joint_values()
    print current_joints

    quit()
