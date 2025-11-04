from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='seesaw_simulation',
            executable='seesaw_simulation'
        ),
        Node(
            package='seesaw_simulation',
            executable='gui_node'
        )
    ])
