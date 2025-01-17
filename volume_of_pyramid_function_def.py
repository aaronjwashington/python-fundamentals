#Define a function calc_pyramid_volume with parameters base_length, base_width, and pyramid_height, that returns as a number the volume of a pyramid with a rectangular base.

#Sample output with inputs: 4.5 2.1 3.0
#Volume for 4.5 2.1 3.0 is: 9.45
#Relevant geometry equations:
#Volume = base area x height x 1/3
#Base area = base length x base width

def calc_pyramid_volume(base_length, base_width, pyramid_height):
    return (1 /3 * base_width) * (pyramid_height * base_length)

length = float(input())
width = float(input())
height = float(input())
print(f'Volume for {length} {width} {height} is: {calc_pyramid_volume(length, width, height):.2f}')