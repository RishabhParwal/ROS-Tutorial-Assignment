import rclpy
from rclpy.node import Node
from rover_odometry.srv import CollectSample

class CollectionService(Node):
    def __init__(self):
        super().__init__('collection_service')
        self.srv = self.create_service(CollectSample, 'collect_sample', self.collect_sample_callback)

    def collect_sample_callback(self, request, response):
        self.get_logger().info(f'Received request for collection at ({request.target_x}, {request.target_y})')
        
        # Simulate success/failure
        if self.is_accessible(request.target_x, request.target_y):
            response.status = 'Collection Successful'
        else:
            response.status = 'Collection Failed'
        return response

    def is_accessible(self, x, y):
        # Logic to check if the target is reachable (mock implementation)
        return True  # Modify with real obstacle checking logic

def main(args=None):
    rclpy.init(args=args)
    node = CollectionService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
