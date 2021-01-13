#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import time
import random


class sign_control():

    def __init__(self):
        # Initialize node
        rospy.init_node('sign_control')

        # Initiate publisher
        self._joint_red_pub = rospy.Publisher('/traffic_sign/joint_red_position_controller/command',
                                              Float64, queue_size=1)

        self._joint_green_pub = rospy.Publisher('/traffic_sign/joint_green_position_controller/command',
                                                Float64, queue_size=1)

        # wait for controllers to come up
        while self._joint_red_pub.get_num_connections() == 0 or \
                self._joint_green_pub.get_num_connections() == 0:
            rospy.sleep(rospy.Duration(0.2))

        rospy.loginfo("Sending motion commands")

        # initial state is stop
        self.send_red()

        # Wait for random time before turning the sign green
        rospy.sleep(rospy.Duration(random.randint(3, 10)))
        # NOTE: A similar logic would be used to evaluate your submission, hence
        # it is highly recommended to test your work with random time for Red
        # as shown above

        self.send_green()
        # wait on green for exactly 10 seconds (including the 2 seconds taken
        # to change the sign in function 'send_green()' above)
        rospy.sleep(rospy.Duration(8))

        # Return to Red and exit
        self.send_red()

    def send_red(self):
        j1 = Float64(0)
        j2 = Float64(1.57)

        self._joint_red_pub.publish(j1)
        self._joint_green_pub.publish(j2)

        # wait for sign joints to reach the given position
        rospy.sleep(2)

    def send_green(self):
        j1 = Float64(1.57)
        j2 = Float64(0)

        self._joint_red_pub.publish(j1)
        self._joint_green_pub.publish(j2)

        # wait for sign joints to reach the given position
        rospy.sleep(2)


if __name__ == "__main__":
    try:
        sign_control()
    except rospy.ROSInterruptException:
        pass
