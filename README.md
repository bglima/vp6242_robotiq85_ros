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
For now, only RViz visualization is avaliable:
```
roslaunch vp6242_robotiq85_description vp6242gripper.launch
```

## Controlling by topics
By default, ```joint_state_publisher``` node starts with ```use_gui``` parameter as true. In order to listen to topics, use:
```
roslaunch vp6242_robotiq85_description vp6242gripper.launch gui:=false
```
You can set joint positions by sending a message to ```ik_joint_states``` topic, as following example:
```
rostopic pub /ik_joint_states  sensor_msgs/JointState '{header: {seq: 0, stamp: {secs: 0, nsecs: 0}, frame_id: ""}, 
  name: ["joint1", "joint2", "gripper_finger1_joint"],
  position: [1.57, 0.5, 1.0]}'
```

## References
[Joint State Publisher wiki](http://wiki.ros.org/joint_state_publisher)

[Why to use a joint_state_publisher?](https://answers.ros.org/question/207728/why-use-joint_state_publisher/)
