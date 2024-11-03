from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rover_status',
            executable='battery_temp_publisher',
            name='battery_temp_publisher'
        ),
        Node(
            package='rover_status',
            executable='health_status_publisher',
            name='health_status_publisher'
        ),
        Node(
            package='rover_status',
            executable='rover_status_subscriber',
            name='rover_status_subscriber'
        )
    ])