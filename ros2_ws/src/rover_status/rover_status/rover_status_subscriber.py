#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, String

class RoverStatusSubscriber(Node):
    def __init__(self):
        super().__init__('rover_status_subscriber')
        self.battery_temp_subscriber_ = self.create_subscription(Float32MultiArray, 'battery_temp', self.battery_temp_callback, 10)
        self.health_status_subscriber_ = self.create_subscription(String, 'health_status', self.health_status_callback, 10)

    def battery_temp_callback(self, msg):
        self.get_logger().info(f"Battery Level: {round(msg.data[0],1)}%, {round(msg.data[1],1)}C")
    
    def health_status_callback(self, msg):
        self.get_logger().info(f"Health Status: {msg.data}")
        

def main(args=None):
    rclpy.init(args=args)
    node = RoverStatusSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()