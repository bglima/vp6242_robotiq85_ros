# vp6242_robotiq85_ros
ROS package for Denso VP6242 coupled with Robotiq 85 Gripper.

## How to install
In your workspace/src folder, clone dependency packages robotiq_85_gripper and vp6242_ros.

```
cd ~/catkin_ws/src
git clone https://github.com/bglima/robotiq_85_gripper
git clone https://github.com/bglima/VP6242_ROS.git
```

Then, install MoveIT core and ROS effort-controller dependencies:
```
sudo apt-get install ros-$ROS_DISTRO-moveit
sudo apt-get install ros-$ROS_DISTRO-effort-controllers
```

Then clone this repo and build workspace.
```
git clone https://github.com/bglima/vp6242_robotiq85_ros.git
cd ~/catkin_ws
catkin_make
```
## How to run RViz
RViz visualization:
```
roslaunch vp6242_robotiq85_description vp6242gripper.launch
```

By default, ```joint_state_publisher``` node starts with ```use_gui``` parameter as true, in order to use GUI sliders. Alternatively, you may desire to control visualization by topic publishing, using:
```
roslaunch vp6242_robotiq85_description vp6242gripper.launch gui:=false
```
You can set joint positions by sending a message to ```ik_joint_states``` topic, as following example:
```
rostopic pub /ik_joint_states  sensor_msgs/JointState '{header: {seq: 0, stamp: {secs: 0, nsecs: 0}, frame_id: ""},
  name: ["joint1", "joint2", "gripper_finger1_joint"],
  position: [1.57, 0.5, 1.0]}'
```

## Running Gazebo physical simulation

If you want to run Gazebo world instead:
```
roslaunch vp6242_robotiq85_gazebo vp6242_robotiq_85.launch
```

In order to control Gazebo arm model, use JointTrajectory. You can change more than one joint at once. Following example shows how to change joints 1, 2, 3 and 5:
```
rostopic pub /vp6242/trajectory_controller/command trajectory_msgs/JointTrajectory "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
joint_names: ['joint1', 'joint2', 'joint3', 'joint5']
points:
- positions: [0, 0, 1.57, 0]   
  velocities: [0, 0, 0, 0]
  accelerations: [0, 0, 0, 0]
  effort: [0, 0, 0, 0]
  time_from_start: {secs: 1, nsecs: 0}"
```

Lastly, you can command gripper to open or close. Position 0.8 means fully closed, while position 0.0 means fully opened.
Command example:
```
rostopic pub vp6242/gripper_position_controller/command trajectory_msgs/JointTrajectory "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
joint_names:
- 'gripper_finger1_joint'
points:
- positions: [0.80]
  velocities: [0]
  accelerations: [0]
  effort: [0]
  time_from_start: {secs: 1, nsecs: 0}"
```

## References
[Joint State Publisher wiki](http://wiki.ros.org/joint_state_publisher)

[Why to use a joint_state_publisher?](https://answers.ros.org/question/207728/why-use-joint_state_publisher/)

[Joint Trajectory Controller](http://wiki.ros.org/joint_trajectory_controller)
