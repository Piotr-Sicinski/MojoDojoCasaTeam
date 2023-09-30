from PIL import Image
import numpy as np

# Open an image using Pillow
# Replace with the path to your image
image = Image.open("piotrekDemo\\ball.jpg")

# Convert the image to a NumPy array
image_array = np.array(image)

# Now, 'image_array' contains the pixel data in the form of a NumPy array

# You can access and manipulate the pixel data like any other NumPy array
# For example, to get the dimensions of the image:
height, width, channels = image_array.shape

# To access a specific pixel value at coordinates (x, y):
x, y = 100, 200
pixel_value = image_array[y, x]

# To change the pixel at coordinates (x, y) to a new color (e.g., white):
new_color = [255, 255, 255]  # White color in RGB
image_array[y, x] = new_color

# To save the modified image:
modified_image = Image.fromarray(image_array)
modified_image.save("modified_image.jpg")
