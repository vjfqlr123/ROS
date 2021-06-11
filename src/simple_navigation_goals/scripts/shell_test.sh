#!/bin/bash

echo "step 1 : roscore start...."
roscore &
sleep 3s

#####################################
echo "Connecting to Raspberry Pi..."
ssh -l pi 172.16.93.13 -p turtlebot

########################################
#echo "step 3 : gazebo start...."
#roslaunch turtlebot3_gazebo turtlebot3_world.launch &
#sleep 3s

########################################
echo "step 3 : map loading...."
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/test1.yaml &
sleep 3s

########################################
echo "step 4 : simple navi start..."
rosrun simple_navigation_goals simple_navigation.py &


########################################
echo "step 5 : "

########################################
echo "step 6 : "



[ WARN] [1620867630.127592306]: Timed out waiting for transform from base_footprint to map to become available before running costmap, tf error: canTransform: target_frame map does not exist.. canTransform returned after 0.100078 timeout was 0.1.

