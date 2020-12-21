#calculate the area of a triangle
#first; prompt 'find the area of a triangle' && prompt for the base & height
#second; use str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹") for SUB && SUPER script
#thrid; print the area of the triangle

import math

print('Find the area of a triangle!')

height_str = input('the height : ')
height_float = float(height_str)
base_str = input('the base : ')
base_float = float(base_str)

SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
meters = 'm2'.translate(SUP)
feet = 'ft2'.translate(SUP)

m_type_str = input("what is the mesurment type : ")
if(m_type_str == meters):
    print(meters)
if(m_type_str == feet):
    print(feet)

triarea = (base_float * height_float) / 2

print(triarea, m_type_str, 'is the area of the triangle')
