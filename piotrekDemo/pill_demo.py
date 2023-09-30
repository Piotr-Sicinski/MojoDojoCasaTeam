from PIL import Image
import numpy as np

# Create a sample 2D NumPy array (e.g., grayscale image)
width, height = 256, 256
gray_array = np.random.randint(0, 256, (height, width), dtype=np.uint8)

# Create an image from the NumPy array
image = Image.fromarray(gray_array, 'L')  # 'L' mode for grayscale

# Save the image (optional)
image.save("output_image.png")

# Show the image (optional)
image.show()
