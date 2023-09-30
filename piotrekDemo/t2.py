import numpy as np
from PIL import Image

# Load an image as a NumPy array
# Replace with the path to your image
# image = np.array(Image.open("src\\ball.jpg"))
# image = image.resize((3, 3))
image = np.array(
    [[13, 13, 13], [13, 13, 13], [13, 13, 16]])

# Create a NumPy array of Boolean values (True/False)
# For example, create a Boolean array of the same shape as the image
boolean_array = np.array(
    [[True, False, True], [False, True, False], [True, False, True]])

print(image ^ boolean_array)
