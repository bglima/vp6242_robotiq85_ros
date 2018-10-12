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
## How to run
RViz visualization:
```
roslaunch vp6242_robotiq85_description vp6242gripper.launch
```

If you want to run Gazebo world instead:
```
roslaunch vp6242_robotiq85_gazebo vp6242_robotiq_85.launch
```

In order to control Gazebo model, use JointTrajectory. You can change more than one joint at once. Following example shows how to change joints 1, 2, 3 and 5:
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
