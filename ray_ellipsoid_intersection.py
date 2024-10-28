# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
# Determines the intersection point (if it exists) between a ray and the Earth reference ellipsoid
#
# Parameters:
#  d_l_x: x-component of the origin-referenced ray direction
#  d_l_y: y-component of the origin-referenced ray direction
#  d_l_z: z-component of the origin-referenced ray direction
#  c_l_x: x-component offset of ray origin
#  c_l_y: y-component offset of ray origin
#  c_l_z: z-component offset of ray origin
#
# Output:
#  Prints the x, y, and z components of the intersection point if it exists.
#
# Written by Nick Davis
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# Import necessary modules
import sys
import math

# Constants
R_E_Km = 6378.137  # Semi-major axis in kilometers (equatorial radius)
E_E    = 0.081819221456

# Function to calculate ray-ellipsoid intersection
def ray_ellipsoid_intersection(d_l, c_l):
    # Coefficients for the quadratic
    A = d_l_x**2.0+d_l_y**2.0+(d_l_z**2/(1-E_E**2))
    B = 2.0*(d_l_x*c_l_x+d_l_y*c_l_y+d_l_z*(c_l_z/(1-E_E**2)))
    C = c_l_x**2+c_l_y**2+(c_l_z**2/(1-E_E**2))-R_E_Km**2

    # Solves the quadratic
    discriminant = B**2 - 4 * A * C
    if discriminant>=0:
        d=(-B-math.sqrt(discriminant))/(2.0*A)
    if d<0:
        d=(-B+math.sqrt(discriminant))/(2.0*A)

    # Calculate the intersection point for x, y, z axis
    l_d = [
        c_l[0] + d * d_l[0],
        c_l[1] + d * d_l[1],
        c_l[2] + d * d_l[2],
    ]

    return l_d

# Parse script arguments
if len(sys.argv) == 7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
    print('Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z')
    exit()

# Create direction and offset vectors
d_l = [d_l_x, d_l_y, d_l_z]
c_l = [c_l_x, c_l_y, c_l_z]

# Calculate the intersection point
intersection_point = ray_ellipsoid_intersection(d_l, c_l)

print(intersection_point[0])  # x-component of intersection point
print(intersection_point[1])  # y-component of intersection point
print(intersection_point[2])  # z-component of intersection point