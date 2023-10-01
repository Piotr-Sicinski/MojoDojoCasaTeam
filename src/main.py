from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import random
from utils.masks import flip_zeros
from utils.waves import classical_wave_function


def apply_mask(image: np.array, mask : np.array):
    image[mask] = [0, 0, 0]


def generateFrames(image: Image, mask: np.array, count : int):
    frames = []
    buf = np.array(image)

    wave = classical_wave_function(np.linspace(0, 1, count), frequency=2, amplitude=1)
    wave = np.abs(wave)

    for i in range(count):
        delta = int(wave[i] * 100)
        flip_zeros(mask, delta)
        apply_mask(buf, mask)
        frames.append(Image.fromarray(buf))

    return frames



def createGif(frames: list, name: str, fps: int):
    frames[0].save(name, format='GIF', append_images=frames[1:], save_all=True, duration=len(frames)/fps, loop=0)


if __name__ == "__main__":
    frames = 500
    img = Image.open("ball.jpg").resize((256, 256))
    base_mask = np.full((256, 256), False, dtype=bool)

    
    frames = generateFrames(img, base_mask, frames)
    createGif(frames, "test.gif", 20)

