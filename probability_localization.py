# Authors: 
# Aayush Shah (aayushsh@usc.edu)

# Receive input from IMU - A 3d vector. (x,y,z) which is an absolute vector of the distance traveled from the calibrated point (0,0,0)
# For now write a function to generate mock data
import random
import math

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
scale = 1

for i in range(10):
    x_cv.append(random.randint(0, 100))
    y_cv.append(random.randint(0, 100))
    z_cv.append(random.randint(0, 100))
    
    d.append(random.randint(0, 20))
    p.append(random.randint(0, 100))

# Hardcode actual distance of obstacles. x axis to the right, y to the top and z to the bottom
gate1_x = scale * 74
gate1_y = scale * 43
gate1_z = 100

"""
marker1_x = scale * 90
marker1_y = scale * 44
marker1_z = 100

craps_x = scale * 120
craps_y = scale * 85
craps_z = 200

marker2_x = scale * 277
marker2_y = scale * 94
marker2_z = 100

slots_x = scale * 340
slots_y = scale * 274
slots_z = 400

ringer_x = scale * 202
ringer_y = scale * 315
ringer_z = 200

cashInRed_x = scale * 173
cashInRed_y = scale * 446
cashInRed_z = 100

cashInGreen_x = scale * 173
cashInGreen_y = scale * 411
cashInGreen_z = 100

cashInYellow1_x = scale * 136
cashInYellow1_y = scale * 446
cashInYellow1_z = 100

cashInYellow2_x = scale * 136
cashInYellow2_y = scale * 411
cashInYellow2_z = 100"""
# Calculate difference between computer vision + IMU vector and hardcoded vector
result = (x_imu[0] - gate1_x)**2 + (y_imu[0] - gate1_y)**2 + (z_imu[0] - gate1_z)**2
result = math.sqrt(result)
#print(result)

error_percent = 1 - (abs(result-d[0])/(result+d[0]))
print(error_percent*p[0])
# Scale probabiity downwards using Gaussian probability function

# Output - Relative location of the Observed Object, in the format of Angles, distance and probability (x,y,z), d,  p
