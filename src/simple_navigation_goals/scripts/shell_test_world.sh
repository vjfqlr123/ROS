#!/bin/bash


########################################
echo "step 1 : gazebo start...."
roslaunch turtlebot3_gazebo turtlebot3_world.launch &
sleep 3s

########################################
echo "step 2 : map loading...."
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml &
sleep 3s

########################################
echo "step 3 : simple navi start..."
rosrun simple_navigation_goals sim_navi_world.py


########################################
echo "step 5 : "


