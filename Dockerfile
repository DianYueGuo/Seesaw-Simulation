FROM ros:humble-ros-base-jammy

RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /etc/bash.bashrc

WORKDIR /root/
