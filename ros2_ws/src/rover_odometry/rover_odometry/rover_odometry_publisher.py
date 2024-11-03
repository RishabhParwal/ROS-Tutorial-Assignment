#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from mars_msgs.msg import RoverOdometry
import random

class RoverOdometryPublisher(Node):
    def __init__(self):
        super().__init__('rover_odometry_publisher')
        self.publisher_ = self.create_publisher(RoverOdometry, 'rover_odometry', 10)
        self.timer = self.create_timer(1.0, self.publish_odometry)

    def publish_odometry(self, x, y, theta):
        msg = RoverOdometry()
        msg.robot_id = 1
        msg.linear_velocity.linear.x = random.uniform(-2.5, 2.5)
        msg.linear_velocity.linear.y = random.uniform(-2.5, 2.5)
        msg.orientation = 0
        msg.angular_velocity.angular.z = random.uniform(0, 1)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RoverOdometryPublisher()
    rclpy.spin(node)
    rclpy.shutdown()