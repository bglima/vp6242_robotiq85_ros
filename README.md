# vp6242_robotiq85_ros
ROS package for Denso VP6242 coupled with Robotiq 85 Gripper.

## How to install
In your workspace/src folder, clone dependency packages robotiq_85_gripper and vp6242_ros.

```
cd ~/catkin_ws/src
git clone https://github.com/bglima/robotiq_85_gripper
git clone https://github.com/bglima/VP6242_ROS.git
```

Then, install MoveIT core and dependencies:
```
sudo apt-get install ros-$ROS_DISTRO-moveit
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
