import rclpy
from rclpy.node import Node
from rover_odometry.srv import CollectSample
import time

class RoverCollection(Node):
    def __init__(self):
        super().__init__('rover_collection')
        self.srv = self.create_service(CollectSample, 'collect_sample', self.handle_collection)

    def handle_collection(self, request, response):
        target = (request.target_x, request.target_y)
        self.get_logger().info(f'Moving to target: {target}')

        if self.navigate_to_target(target):
            response.status = 'Collection Successful'
        else:
            response.status = 'Collection Failed'
        return response

    def navigate_to_target(self, target):
        # Dummy navigation logic, simulates moving to target
        self.get_logger().info(f'Navigating to {target}')
        time.sleep(2)  # Simulating delay
        return True  # Always returns success for simplicity

def main(args=None):
    rclpy.init(args=args)
    node = RoverCollection()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
