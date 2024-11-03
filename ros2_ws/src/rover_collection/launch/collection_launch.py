from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rover_collection',
            executable='collection_service',
            name='collection_service'
        ),
        Node(
            package='rover_collection',
            executable='collection_client',
            name='collection_client'
        ),
        Node(
            package='rover_collection',
            executable='rover_collection',
            name='rover_collection'
        )
    ])
