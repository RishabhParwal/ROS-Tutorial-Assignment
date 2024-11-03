import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rishabh/Desktop/MRT/Assignments/Assignment2/ros2_ws/install/rover_odometry'
