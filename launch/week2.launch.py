from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
           package='week_2',
            namespace='otter',
            executable='otter',
            name='otter',
            output='screen'
        ),
        Node(
           package='week_2',
            namespace='kcs',
            executable='kcs',
            name='kcs',
            output='screen'

        ),
    ])
