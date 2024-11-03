#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from mars_msgs.msg import RoverOdometry

class RoverOdometrySubscriber(Node):
    def __init__(self):
        x = 0
        y = 0
        theta = 0
        super().__init__('rover_odometry_subscriber')
        self.subscription = self.create_subscription(RoverOdometry, 'rover_odometry', self.odometry_callback, 10)

    def odometry_callback(self, msg):
        self.x += msg.linear_velocity.linear.x
        self.y += msg.linear_velocity.linear.y
        self.get_logger().info(f"X: {self.x}, Y: {self.y}, Theta: {self.theta}")
        if (msg.linear_velocity.x**2 + msg.linear_velocity.y**2)**0.5 > 3:
            self.get_logger().info("Warning: Rover going too fast!")

def main(args=None):
    rclpy.init(args=args)
    node = RoverOdometrySubscriber()
    rclpy.spin(node)
    rclpy.shutdown()