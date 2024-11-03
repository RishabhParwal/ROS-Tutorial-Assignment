#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import heapq

class RoverNavigation(Node):
    def __init__(self):
        super().__init__('rover_navigation')
        self.steps = 0
        self.R = int(input("Enter the number of rows: "))
        self.C = int(input("Enter the number of columns: "))
        self.x = float(input("Enter the initial x coordinate: "))
        self.y = float(input("Enter the initial y coordinate: "))
        self.m = float(input("Enter the goal x coordinate: "))
        self.n = float(input("Enter the goal y coordinate: "))
        self.obstacles = []
        self.path = []
        self.coordinate_publisher_ = self.create_publisher(Float32MultiArray, 'rover_coordinate', 10)
        self.timer = self.create_timer(0.1, self.coordinate_publisher_callback)
        self.obstacle_subscriber_ = self.create_subscription(Float32MultiArray, 'obstacle_coordinates', self.obstacle_subscriber_callback, 10)
    
    def coordinate_publisher_callback(self):
        if not self.path:
            self.path = self.find_path((self.x, self.y), (self.m, self.n))
        
        if self.path:
            next_step = self.path.pop(0)
            self.x, self.y = next_step
            msg = Float32MultiArray()
            msg.data = [self.x, self.y]
            self.coordinate_publisher_.publish(msg)
            self.get_logger().info(f'Moving to: {self.x}, {self.y}')
            self.steps += 1
            if self.x == self.m and self.y == self.n:
                self.get_logger().info(f'Goal reached! in {self.steps - 1} steps')
                msg.data = [-100.0, -100.0]
                self.coordinate_publisher_.publish(msg)
                self.timer.cancel()
                rclpy.shutdown()

    def obstacle_subscriber_callback(self, msg):
        self.obstacles = [(msg.data[i], msg.data[i+1]) for i in range(0, len(msg.data), 2)]
        # self.get_logger().info(f'Obstacles: {self.obstacles}')

    def find_path(self, start, goal):
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start, goal)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        total_path.reverse()
        return total_path

    def get_neighbors(self, node):
        neighbors = [
            (node[0] + 1, node[1]),
            (node[0] - 1, node[1]),
            (node[0], node[1] + 1),
            (node[0], node[1] - 1),
            (node[0] + 1, node[1] + 1),
            (node[0] - 1, node[1] - 1),
            (node[0] + 1, node[1] - 1),
            (node[0] - 1, node[1] + 1),
        ]
        # Filter out neighbors that are obstacles or out of bounds
        valid_neighbors = []
        for neighbor in neighbors:
            if (0 <= neighbor[0] < self.R and 0 <= neighbor[1] < self.C) and neighbor not in self.obstacles:
                valid_neighbors.append(neighbor)
        return valid_neighbors

def main(args=None):
    rclpy.init(args=args)
    node = RoverNavigation()
    rclpy.spin(node)
    rclpy.shutdown()