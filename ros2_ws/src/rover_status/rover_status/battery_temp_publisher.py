#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import random

class BatteryTempPublisher(Node):

    def __init__(self):
        super().__init__('battery_temp_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'battery_temp', 10)
        self.timer = self.create_timer(1.0, self.publish_temp)

    def publish_temp(self):
        msg = Float32MultiArray()
        msg.data = [random.uniform(0, 100), random.uniform(-20, 80)]
        self.publisher_.publish(msg)
        # self.get_logger().info(f"Publishing: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = BatteryTempPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()