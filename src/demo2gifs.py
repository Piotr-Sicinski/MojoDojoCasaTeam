from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import random


SIZE = 256
TIME = 10
FPS = 20
SHAPE = (SIZE, SIZE)

# Create a list to store frames
frames1 = []
frames2 = []

image1 = Image.open("src\\ball.jpg")
image2 = Image.open("src\\bricks.jpg")

image1 = image1.resize((SIZE, SIZE))
image2 = image2.resize((SIZE, SIZE))

ARR1 = np.array(image1)
ARR2 = np.array(image2)

mask1 = np.full(SHAPE, True, dtype=bool)
mask2 = np.full(SHAPE, False, dtype=bool)


# Create a figure and axis for plotting
fig, ax = plt.subplots()

image1.show()


def changePixels(arr):
    for _ in range(1000):
        x, y = random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)
        arr[x][y] = not arr[x][y]
        # a2[x][y] = not a2[x][y]


buf = np.zeros((SIZE, SIZE, 3))

# Generate and save frames
for i in range(TIME * FPS):
    # Draw a rectangle that moves horizontally
    changePixels(mask1)
    buf = ARR1

    # for j in [0, 1, 2]:
    #     buf[:, :, j] = ARR1[:, :, j] ^ mask1
    buf[~mask1] = [0, 0, 0]

    image1 = Image.fromarray(buf, mode='RGB')

    # Append the frame to the list of frames
    frames1.append(image1)

# Save the frames as an animated GIF
frames1[0].save("animated.gif", save_all=True,
                append_images=frames1[1:], duration=1000/FPS, loop=0)

# Show the animated GIF (optional)
plt.imshow(np.array(frames1[0]))
plt.axis('off')
plt.show()
