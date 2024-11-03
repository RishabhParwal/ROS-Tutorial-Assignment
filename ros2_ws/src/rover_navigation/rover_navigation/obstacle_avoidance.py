#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import numpy as np

R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))

def matrix_input():
    global grid
    grid = list(map(int, input("Enter the entries(1 or 0) in a single line (separated by space): ").split()))

def obstacle_detector(grid, coordinates):
    # Using numpy to convert the list to 2D array
    grid = np.array(grid).reshape(R, C)
    list_of_obstacles = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                list_of_obstacles.append((j - coordinates[0], R - i -1 - coordinates[1]))

    return list_of_obstacles

class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance')
        self.x = 0.0
        self.y = 0.0
        self.coordinate_subscriber_ = self.create_subscription(Float32MultiArray, 'rover_coordinate', self.coordinate_subscriber_callback, 10)
        self.obstacles = obstacle_detector(grid, (self.x, self.y))
        self.obstacles_publisher_ = self.create_publisher(Float32MultiArray, 'obstacle_coordinates', 10)
        self.timer = self.create_timer(0.1, self.obstacles_publisher_callback)

    def coordinate_subscriber_callback(self, msg):
        self.x = float(msg.data[0])
        self.y = float(msg.data[1])
        if self.x == -100 and self.y == -100:
            self.timer.cancel()
            rclpy.shutdown()

        self.obstacles = obstacle_detector(grid, (self.x, self.y))  # Update obstacles based on new coordinates
    
    def obstacles_publisher_callback(self):
        msg = Float32MultiArray()
        # Publish each obstacle as a pair of floats
        msg.data = [coord for obstacle in self.obstacles for coord in (float(obstacle[0]), float(obstacle[1]))]
        self.obstacles_publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    matrix_input()
    node = ObstacleAvoidance()
    rclpy.spin(node)
    rclpy.shutdown()