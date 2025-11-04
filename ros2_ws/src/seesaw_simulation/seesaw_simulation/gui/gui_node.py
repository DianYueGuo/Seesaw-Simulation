import rclpy
from rclpy.node import Node
from .aiohttp_server import AIOHTTPServer
import json

from std_msgs.msg import Float64


class GUINode(Node):

    def __init__(self):
        super().__init__('gui_node')

        self.aiohttp_server = AIOHTTPServer(self.__msg_callback)
        self.aiohttp_server.start_threading()

        self.__slider_radial_position_subscribers = self.create_subscription(
                msg_type=Float64,
                topic="slider_radial_position_m",
                callback=self.__slider_radial_position_subscription_callback,
                qos_profile=10
            )

        self.__slider_radial_velocity_subscribers = self.create_subscription(
                msg_type=Float64,
                topic="slider_radial_velocity_m_per_s",
                callback=self.__slider_radial_velocity_subscription_callback,
                qos_profile=10
            )

        self.__slider_angular_position_subscribers = self.create_subscription(
                msg_type=Float64,
                topic="slider_angular_position_rad",
                callback=self.__slider_angular_position_subscription_callback,
                qos_profile=10
            )

        self.__slider_angular_velocity_subscribers = self.create_subscription(
                msg_type=Float64,
                topic="slider_angular_velocity_rad_per_s",
                callback=self.__slider_angular_velocity_subscription_callback,
                qos_profile=10
            )

    def __slider_radial_position_subscription_callback(self, msg):
        self.aiohttp_server.send_topic("slider_radial_position_m", msg.data)

    def __slider_radial_velocity_subscription_callback(self, msg):
        self.aiohttp_server.send_topic("slider_radial_velocity_m_per_s", msg.data)

    def __slider_angular_position_subscription_callback(self, msg):
        self.aiohttp_server.send_topic("slider_angular_position_rad", msg.data)

    def __slider_angular_velocity_subscription_callback(self, msg):
        self.aiohttp_server.send_topic("slider_angular_velocity_rad_per_s", msg.data)

    def __msg_callback(self, msg):
        print(msg)
        msg_json_object = json.loads(msg)

        if msg_json_object["type"] == "topic":
            if msg_json_object["data"]["topic_name"] == "":
                pass

def main(args=None):
    rclpy.init(args=args)

    gui_node = GUINode()

    rclpy.spin(gui_node)

    gui_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
