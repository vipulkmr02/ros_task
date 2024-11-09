#!/usr/bin/env python3

import math
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('move_turtle_rectangle_node', anonymous=True)
publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10)

def move_straight(x: int):
    rospy.loginfo(f"Displacing {x} units straight ahead")
    msg = Twist()
    msg.linear.x = x
    msg.linear.y = 0
    msg.linear.z = 0
    publisher.publish(msg)
    rospy.loginfo(f"Displaced {x} units straight ahead")

def turn():
    rospy.loginfo("Turning 90 deg")
    msg = Twist()
    msg.angular.z = 1.57;
    publisher.publish(msg)
    rospy.loginfo("Turned")


def move_turtle():
    rospy.loginfo("Moving the turtle in a rectangle...")
    l: int = 4
    b: int = 2

    for _ in range(2):
        rospy.sleep(1.0)
        move_straight(l)  # covering wide path
        rospy.sleep(1)
        turn()  # turning
        rospy.sleep(1.0)
        move_straight(b)  # covering smaller path
        rospy.sleep(1)
        turn()  # turning


if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
