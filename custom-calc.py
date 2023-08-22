# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the description. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!

print("Enter length, width, and height to calculate the volume of a pyramid.\n")

length = (float(input("Length: ")))
# print("Length: ", length)

width = (float(input("Width: ")))
# print("Width: ", width)

height = (float(input("Height: ")))
# print("Height: ", height)

pyramid_volume = (length * width * height) / 3

print(f"\nA pyramid with a length of {length}, width of {width}, and height of {height} has a volume of {pyramid_volume:.2f}, rounded to nearest hundredth.")
