# Particles Filter

A visualization of 1-D particles filter localization 
in 2-D space using sensor readings curve. 

A robot is located on a long corridor (1 dimensional) 
and is moving along it. It uses sensor 
information that helps it find its location.

The following figure shows an example of sensor values 
(the curve in blue) at each position in the corridor,
The robot and its direction are also shown in red. 
The particles are shown in blue. The robot and 
each particle can obtain the sensor value from 
the blue curve based on their position.

The figure below shows the behaviour of the particles 
along with the robot, with each step, more particles will 
surround the robot, and more particles will vanish if they're 
too far from the robot.

![particles movement with the robot](https://github.com/SuhairShareef/particles_filter/blob/main/blobs/particles%20movement%20along%20with%20the%20robot.png?raw=true)
