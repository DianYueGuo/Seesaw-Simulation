# Seesaw-Simulation

## How to Run Simulation

1. `docker compose up --build`
1. To another terminal, run `docker exec -it seesaw-simulation-ros-1 bash` to enter the container.
1. `cd ros2_ws`
1. `apt-get update`
1. `rosdep install --from-paths src -y`
1. `colcon build --symlink-install`
1. `source install/setup.bash` (Remember to run this every time you open a new terminal. Or, you can add it to your `/etc/bash.bashrc` file.)
1. `ros2 launch seesaw_simulation seesaw_simulation_launch.py`
1. Open [http://127.0.0.1/](http://127.0.0.1/) in your browser to see the GUI. You can use the left, right arrow keys to test the simulation.

## Discovery

Enter the container from a new terminal using `docker exec -it seesaw-simulation-ros-1 bash` (and remember to run `source ros2_ws/install/setup.bash`).

You can run `ros2 node list` to see the two nodes running:
```
/seesaw_simulation/gui_node
/seesaw_simulation/seesaw_simulation
```

You can run `ros2 topic list` to see the list of all the topics present:
```
/parameter_events
/rosout
/seesaw_simulation/applied_torque_N_m
/seesaw_simulation/slider_angular_position_rad
/seesaw_simulation/slider_angular_velocity_rad_per_s
/seesaw_simulation/slider_radial_position_m
/seesaw_simulation/slider_radial_velocity_m_per_s
```
You can run `ros2 topic echo <topic_name>` to see the data of the topics.
