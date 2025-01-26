# vention_robotics

Advanced Robot Motion Planning with NVIDIA CuRobo

This project aims to revolutionize Vention's robot work cell capabilities by leveraging NVIDIA's Jetson Orin and Nano modules in the new Machine Motion V2 (Machine Motion AI) system. The primary objectives are:

Implement CuMotion: Replace the current MoveIt and Pilz setup with NVIDIA's CuRobo library for faster, more efficient robot movements.

  Enhance Motion Planning and Collision Avoidance:
  Utilize CAD environment data from MachineBuilder for comprehensive obstacle awareness
  Develop dynamic spatial awareness for robots, especially in scenarios like 7th-axis movements
  Enable real-time environment adaptation and optimized path planning

Create a Simplified ROS2 Environment: Develop a system that takes the robot environment from CAD, robot type, and robot IP as setup inputs, and generates optimal paths based on the start point, endpoint, and optional vision information.

Improve Performance: Aim for better path quality and faster computation times compared to the current Pilz implementation.

Full Driver Implementation: This includes ROS2 design and implementation, CAD integration (focusing on a 2-axis overhead gantry), robot-specific integration (using URSim for UR20/30), and designing a representative sample work cell.

The project seeks to address current limitations in Vention's robot control system, such as limited intelligence in obstacle avoidance and the need for manual path teaching. By leveraging GPU power and advanced algorithms, the goal is to create a more intelligent, efficient, and adaptable robotic system that significantly reduces manual intervention in complex work cell environments.
