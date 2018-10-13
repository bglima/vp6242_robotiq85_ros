#!/usr/bin/env python
"""
Calling example:
rosrun vp6242_robotiq85_gazebo response_test.py /vp6242/trajectory_controller/command joint1
"""


import rospy
import sys
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

even_iteration = True

def publisher(topic_name, joint_name):
    global even_iteration
    pub = rospy.Publisher(topic_name, JointTrajectory, queue_size=1)
    rospy.init_node('robot_tester', anonymous=True)
    sleep_time = rospy.Duration(3)
    while not rospy.is_shutdown():

        msg = JointTrajectory()
        msg.header.stamp = rospy.Time.now()
        msg.joint_names.append("{}".format(joint_name))

        p = JointTrajectoryPoint()
        if even_iteration:
            p.positions.append(-1.57)
            p.velocities.append(0)
            p.accelerations.append(0)
        else:
            p.positions.append(0)
            p.velocities.append(0)
            p.accelerations.append(0)

        even_iteration = not even_iteration
        p.time_from_start = rospy.Duration.from_sec(0.5)
        msg.points.append(p)

        rospy.loginfo(msg)
        pub.publish(msg)
        rospy.sleep(sleep_time)

def main():
    my_argv = rospy.myargv(argv=sys.argv)
    if len(my_argv) < 3:
        print('[ERROR] Missing topic and joint name from JointTrajectory msg.')
        return
    try:
        print("[INFO] Publishing {} to {}!".format(my_argv[1], my_argv[2]))
        publisher(my_argv[1], my_argv[2])
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()
