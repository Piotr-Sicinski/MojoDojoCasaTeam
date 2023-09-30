from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

# Create a list to store frames
frames = []

# Create a figure and axis for plotting
fig, ax = plt.subplots()

# Generate and save frames
for i in range(10):
    # Create a new Pillow image for each frame
    img = Image.new("RGB", (256, 256), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Draw a rectangle that moves horizontally
    left = i * 25
    right = left + 50
    top = 100
    bottom = 150
    draw.rectangle([left, top, right, bottom], fill=(0, 0, 255))

    # Append the frame to the list of frames
    frames.append(img)

# Save the frames as an animated GIF
frames[0].save("animated.gif", save_all=True,
               append_images=frames[1:], duration=100, loop=0)

# Show the animated GIF (optional)
plt.imshow(np.array(frames[0]))
plt.axis('off')
plt.show()
