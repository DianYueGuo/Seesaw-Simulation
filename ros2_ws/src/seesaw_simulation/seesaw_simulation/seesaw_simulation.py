import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64

import math


class SeesawSimulation(Node):

    def __init__(self):
        super().__init__('seesaw_simulation')
        self.__slider_position_publisher = self.create_publisher(Float64, 'slider_position_m', 10)
        self.__seesaw_angle_publisher = self.create_publisher(Float64, 'seesaw_angle_rad', 10)

        self.__simulation_time_delta_s = 0.01
        self.__simulation_loop_timer = self.create_timer(self.__simulation_time_delta_s, self.__simulation_loop_cb)

        self.__standard_gravity_m_per_s_squared = 9.80665
        self.__slider_mass_kg = 1.0
        self.__slider_limit_length_m = 1.0

        self.__radial_position_m = 0.5
        self.__radial_velocity_m_per_s = 0.0
        self.__angular_position_rad = 0.0
        self.__angular_velocity_rad_per_s = 0.0

        self.__applied_torque_N_m = 0.0

    def __simulation_loop_cb(self):
        radial_acceleration_m_per_s_squared = (
            - self.__standard_gravity_m_per_s_squared * math.sin(self.__angular_position_rad)
            + self.__radial_position_m * self.__angular_velocity_rad_per_s**2
        )

        angular_acceleration_rad_per_s_squared = (
            self.__applied_torque_N_m / self.__slider_mass_kg / self.__radial_position_m
            - self.__standard_gravity_m_per_s_squared * math.cos(self.__angular_position_rad)
            - 2 * self.__radial_velocity_m_per_s * self.__angular_velocity_rad_per_s
        ) / self.__radial_position_m

        self.__radial_velocity_m_per_s += radial_acceleration_m_per_s_squared * self.__simulation_time_delta_s
        self.__angular_velocity_rad_per_s += angular_acceleration_rad_per_s_squared * self.__simulation_time_delta_s

        if self.__radial_position_m >= self.__slider_limit_length_m and self.__radial_velocity_m_per_s > 0:
            self.__radial_velocity_m_per_s = 0

        self.__radial_position_m += self.__radial_velocity_m_per_s * self.__simulation_time_delta_s
        self.__angular_position_rad += self.__angular_velocity_rad_per_s * self.__simulation_time_delta_s

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
