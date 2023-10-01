import numpy as np
from utils import digital_alive, quantum_alive
from PIL import Image
import argparse

SIZE = 32

COLOR = [255, 0, 255]


def initialize_board(n):
    """Initialize the Game of Life board with random states."""
    return np.random.choice([0, 1], size=(n, n))


def initialize_board_from_img(img):
    """Initialize the Game of Life board with pattern from file."""
    img_array = np.array(img)
    board = np.where(np.all(img_array[:, :, :3] != [
                     255, 255, 255], axis=2), 1, 0)
    return board


def evolve(board, alive_fn):
    """Evolve the board to the next generation."""
    new_board = np.zeros_like(board)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            new_board[i, j] = alive_fn(board, i, j)
    return new_board


def play(board, alive_fn, steps=10):
    """Play the Game of Life for n generations."""
    frames = [board]
    for i in range(steps):
        board = evolve(board, alive_fn)
        frames.append(board)

    return frames


def save_to_gif(frames, name, fps):

    images = []
    buf = np.full((SIZE, SIZE, 3), COLOR, dtype=np.uint8)

    for frame in frames:
        frame_expanded = np.expand_dims(frame, axis=-1)

        tmp = buf * frame_expanded
        images.append(Image.fromarray(tmp.astype(np.uint8)
                                      ).resize((512, 512), Image.NEAREST))

    images[0].save(
        name,
        format="GIF",
        append_images=images[1:],
        save_all=True,
        duration=len(images) / fps,
        loop=0,
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Load starting pattern')
    parser.add_argument('-l', '--load',
                        action='store_true',
                        help='Load starting pattern from pattern.png file instead of random patern')
    params = parser.parse_args()

    if params.load:
        img = Image.open("pattern.png")

        if img.size != (SIZE, SIZE):
            print(
                f"pattern.png has size different then {SIZE},{SIZE}! Using random pattern.")
            params.load = False
        else:
            print("Starting pattern loaded!")

        board = initialize_board_from_img(img)

    if not params.load:
        board = initialize_board(SIZE)

    print("Art is being created ... ")

    frames = play(board, digital_alive, steps=100)
    save_to_gif(frames, "digital.gif", fps=10)

    if params.load:
        board = initialize_board_from_img(img)
    else:
        board = initialize_board(SIZE)
    frames = play(board, quantum_alive, steps=20)
    save_to_gif(frames, "quantum.gif", fps=10)

    print("Your art is ready!  ... ")
