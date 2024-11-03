import rclpy
from rclpy.node import Node
from rover_odometry.srv import CollectSample

class CollectionClient(Node):
    def __init__(self):
        super().__init__('collection_client')
        self.client = self.create_client(CollectSample, 'collect_sample')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        self.send_requests([(1.0, 2.0), (3.0, 4.0), (5.0, 6.0)])  # Example targets

    def send_requests(self, coordinates):
        for x, y in coordinates:
            request = CollectSample.Request()
            request.target_x = x
            request.target_y = y
            self.future = self.client.call_async(request)
            self.future.add_done_callback(self.callback)

    def callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Response: {response.status}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = CollectionClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
