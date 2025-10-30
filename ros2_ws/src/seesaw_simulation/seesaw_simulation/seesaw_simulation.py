import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64


class SeesawSimulation(Node):

    def __init__(self):
        super().__init__('seesaw_simulation')
        self.__slider_position_publisher = self.create_publisher(Float64, 'slider_position_m', 10)
        self.__seesaw_angle_publisher = self.create_publisher(Float64, 'seesaw_angle_rad', 10)

        self.__simulation_time_delta_s = 0.01
        self.__simulation_loop_timer = self.create_timer(self.__simulation_time_delta_s, self.__simulation_loop_cb)

    def __simulation_loop_cb(self):
        pass


def main(args=None):
    rclpy.init(args=args)

    seesaw_simulation = SeesawSimulation()

    rclpy.spin(seesaw_simulation)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    seesaw_simulation.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
