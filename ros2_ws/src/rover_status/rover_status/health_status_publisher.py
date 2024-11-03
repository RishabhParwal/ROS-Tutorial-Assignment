#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, String

class HealthStatusPublisher(Node):
    def __init__(self):
        super().__init__('health_status_publisher')
        self.publisher_ = self.create_publisher(String, 'health_status', 10)
        self.subscriber_ = self.create_subscription(Float32MultiArray, 'battery_temp', self.battery_temp_callback, 10)

    def battery_temp_callback(self, msg):
        self.battery_level = msg.data[0]
        self.publish_status()

    def publish_status(self):
        if self.battery_level > 75:
            status = "Healthy"
        elif self.battery_level > 40:
            status = "Warning"
        else:
            status = "Critical"
        msg = String()
        msg.data = status
        self.publisher_.publish(msg)
        # self.get_logger().info(f"Publishing: {msg.data}")
        

def main(args=None):
    rclpy.init(args=args)
    node = HealthStatusPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()