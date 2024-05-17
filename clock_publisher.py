#!/usr/bin/env python

import rospy
from rosgraph_msgs.msg import Clock

if __name__ == '__main__':
    rospy.init_node('clock_publisher', anonymous=True)
    rate = rospy.Rate(10)  # Adjust the rate as needed
    clock_publisher = rospy.Publisher('/clock', Clock, queue_size=1)

    while not rospy.is_shutdown():
        current_time = rospy.get_time()
        clock_msg = Clock()
        clock_msg.clock = rospy.Time.from_sec(current_time)
        clock_publisher.publish(clock_msg)
        rate.sleep()

