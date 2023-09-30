from PIL import Image

# Load the image from a PNG file
image = Image.open("ball.jpg")

# Resize the image to 256x256 pixels (optional)
image = image.resize((256, 256))

# Display the image
image.show()

image2 = Image.open("ball.jpg")

# Resize the image to 256x256 pixels (optional)
image2 = image2.resize((256, 256))

# Display the image
image2.show()

# Keep the window open until the user closes it
input("Press Enter to close the image...")
