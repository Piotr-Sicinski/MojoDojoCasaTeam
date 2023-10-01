from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import random

COLOR = [255, 0, 255]
SIZE = 64
SHAPE = (SIZE, SIZE)
# grid = np.zeros((SIZE, SIZE))
grid = np.random.choice([0, 0, 0.4, 0.8, 1], size=SHAPE)


def map_to_color(x: int):
    return COLOR * x


def apply_mask(image: np.array, mask: np.array):
    image[mask] = [0, 0, 0]


def generateFrames(count: int):
    frames = []
    buf = np.full((SIZE, SIZE, 3), COLOR, dtype=np.uint8)
    grid_expanded = np.expand_dims(grid, axis=-1)

    buf = buf * grid_expanded

    for _ in range(count):
        frames.append(Image.fromarray(buf.astype(np.uint8)
                                      ).resize((512, 512), Image.NEAREST))

    return frames


def createGif(frames: list, name: str, fps: int):
    frames[0].save(name, format='GIF', append_images=frames[1:],
                   save_all=True, duration=len(frames)/fps, loop=0)


if __name__ == "__main__":

    frames = generateFrames(5)
    createGif(frames, "test.gif", 1)
