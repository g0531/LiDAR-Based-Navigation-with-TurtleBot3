# ################################################################################
# # Set minimum required version of cmake, project name and compile options
# ################################################################################
# cmake_minimum_required(VERSION 3.0.2)
# project(turtlebot3_navigation)

# ################################################################################
# # Find catkin packages and libraries for catkin and system dependencies
# ################################################################################
# # find_package(catkin REQUIRED)
# find_package(catkin REQUIRED COMPONENTS
#   rospy
#   actionlib
#   interactive_markers
#   std_msgs
#   sensor_msgs
#   geometry_msgs
#   nav_msgs
#   visualization_msgs
#   actionlib_msgs
#   turtlebot3_msgs
#   message_generation
# )

# catkin_python_setup()

# ################################################################################
# # Setup for python modules and scripts
# ################################################################################

# ################################################################################
# # Declare ROS messages, services and actions
# ################################################################################

# ################################################################################
# # Declare ROS dynamic reconfigure parameters
# ################################################################################

# ################################################################################
# # Declare catkin specific configuration to be passed to dependent projects
# ################################################################################
# catkin_package()

# ################################################################################
# # Build
# ################################################################################

# ################################################################################
# # Install
# ################################################################################
# install(DIRECTORY launch maps param rviz
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

# ################################################################################
# # Test
# ################################################################################
# catkin_install_python(PROGRAMS src/movebase_client.py
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

################################################################################
# Set minimum required version of cmake, project name and compile options
################################################################################
cmake_minimum_required(VERSION 3.0.2)
project(turtlebot3_navigation)

################################################################################
# Find catkin packages and libraries for catkin and system dependencies
################################################################################
find_package(catkin REQUIRED COMPONENTS
  rospy
  actionlib
  interactive_markers
  std_msgs
  sensor_msgs
  geometry_msgs
  nav_msgs
  visualization_msgs
  actionlib_msgs
  turtlebot3_msgs
  message_generation
)

################################################################################
# Setup for python modules and scripts
################################################################################

################################################################################
# Declare ROS messages, services and actions
################################################################################

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
  actionlib_msgs
)

################################################################################
# Declare ROS dynamic reconfigure parameters
################################################################################

################################################################################
# Declare catkin specific configuration to be passed to dependent projects
################################################################################
catkin_package(
  CATKIN_DEPENDS
    rospy
    actionlib
    interactive_markers
    std_msgs
    sensor_msgs
    geometry_msgs
    nav_msgs
    visualization_msgs
    actionlib_msgs
    turtlebot3_msgs
    message_runtime
)

################################################################################
# Build
################################################################################
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

################################################################################
# Install
################################################################################
catkin_install_python(PROGRAMS src/movebase_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch maps param rviz
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
################################################################################
# Test
################################################################################
