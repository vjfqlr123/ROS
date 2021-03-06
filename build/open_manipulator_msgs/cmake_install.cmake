# Install script for directory: /home/dody3333/catkin_ws/src/open_manipulator_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/dody3333/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/open_manipulator_msgs/msg" TYPE FILE FILES
    "/home/dody3333/catkin_ws/src/open_manipulator_msgs/msg/JointPosition.msg"
    "/home/dody3333/catkin_ws/src/open_manipulator_msgs/msg/KinematicsPose.msg"
    "/home/dody3333/catkin_ws/src/open_manipulator_msgs/msg/OpenManipulatorState.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/open_manipulator_msgs/srv" TYPE FILE FILES
    "/home/dody3333/catkin_ws/src/open_manipulator_msgs/srv/GetJointPosition.srv"
    "/home/dody3333/catkin_ws/src/open_manipulator_msgs/srv/GetKinematicsPose.srv"
    "/home/dody3333/catkin_ws/src/open_manipulator_msgs/srv/SetJointPosition.srv"
    "/home/dody3333/catkin_ws/src/open_manipulator_msgs/srv/SetKinematicsPose.srv"
    "/home/dody3333/catkin_ws/src/open_manipulator_msgs/srv/SetDrawingTrajectory.srv"
    "/home/dody3333/catkin_ws/src/open_manipulator_msgs/srv/SetActuatorState.srv"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/open_manipulator_msgs/cmake" TYPE FILE FILES "/home/dody3333/catkin_ws/build/open_manipulator_msgs/catkin_generated/installspace/open_manipulator_msgs-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/dody3333/catkin_ws/devel/include/open_manipulator_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/dody3333/catkin_ws/devel/share/roseus/ros/open_manipulator_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/dody3333/catkin_ws/devel/share/common-lisp/ros/open_manipulator_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/dody3333/catkin_ws/devel/share/gennodejs/ros/open_manipulator_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/dody3333/catkin_ws/devel/lib/python2.7/dist-packages/open_manipulator_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/dody3333/catkin_ws/devel/lib/python2.7/dist-packages/open_manipulator_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/dody3333/catkin_ws/build/open_manipulator_msgs/catkin_generated/installspace/open_manipulator_msgs.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/open_manipulator_msgs/cmake" TYPE FILE FILES "/home/dody3333/catkin_ws/build/open_manipulator_msgs/catkin_generated/installspace/open_manipulator_msgs-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/open_manipulator_msgs/cmake" TYPE FILE FILES
    "/home/dody3333/catkin_ws/build/open_manipulator_msgs/catkin_generated/installspace/open_manipulator_msgsConfig.cmake"
    "/home/dody3333/catkin_ws/build/open_manipulator_msgs/catkin_generated/installspace/open_manipulator_msgsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/open_manipulator_msgs" TYPE FILE FILES "/home/dody3333/catkin_ws/src/open_manipulator_msgs/package.xml")
endif()

