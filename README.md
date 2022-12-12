# LiDAR-Based-Navigation-with-TurtleBot3
This lab consists of two parts: the robot first auto-navigate from P1 and visit P2,P3,and P4 in turn, and the robot park in front of the ArUco marker upon returning to P1. 
## Step 1: robot set up
roslaunch turtlebot3_bringup turtlebot3_robot.launch

roslaunch hls_lfcd_lds_driver hlds_laser.launch

roslaunch raspicam_node camerav2_410x308_30fps.launch 

## Step 2: roslaunch to find ArUco marker on PC
roslaunch aruco_marker_finder.launch markerID:=14 markerSize:=0.05
## Step 3: roslaunch navigation based on the map.yaml on PC
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml

PS: The rviz and smach state machine can help you know the process.
