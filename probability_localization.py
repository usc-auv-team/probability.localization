# Authors: 
# Aayush Shah (aayushsh@usc.edu)
#

# Receive input from IMU - A 3d vector. (x,y,z) which is an absolute vector of the distance traveled from the calibrated point (0,0,0)
# For now write a function to generate mock data
import random

x_imu = []
y_imu = []
z_imu = []

for i in range(10):
    x_imu.append(random.randint(0, 100))
    y_imu.append(random.randint(0, 100))
    z_imu.append(random.randint(0, 100))

# Receive computer vision data - Computer Vision Data: 3d Vector that includes the angles of the object’s center from the AUV, the distance and probability, e.g. (x,y,z), d, p
# For now write a function to generate mock data
x_cv = []
y_cv = []
z_cv = []
d = []
p = []

for i in range(10):
    x_cv.append(random.randint(0, 100))
    y_cv.append(random.randint(0, 100))
    z_cv.append(random.randint(0, 100))
    
    d.append(random.randint(0, 20))
    p.append(random.randint(0, 100))

# Hardcode actual distance of obstacles

# Calculate difference between computer vision + IMU vector and hardcoded vector

# Algorithm for next step

# Output - Relative location of the Observed Object, in the format of Angles, distance and probability (x,y,z), d,  p
