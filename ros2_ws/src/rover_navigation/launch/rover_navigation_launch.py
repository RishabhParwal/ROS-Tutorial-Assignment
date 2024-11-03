from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rover_navigation',
            executable='obstacle_avoidance',
            name='obstacle_avoidance',
            output='screen'
        ),
        Node(
            package='rover_navigation',
            executable='rover_navigation',
            name='rover_navigation',
            output='screen'
        )
    ])
