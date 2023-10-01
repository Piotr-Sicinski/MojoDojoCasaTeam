import numpy as np
from utils import digital_alive, quantum_alive
from PIL import Image


def initialize_board(n):
    """Initialize the Game of Life board with random states."""
    return np.random.choice([0, 1], size=(n, n))


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
    for _ in range(steps):
        board = evolve(board, alive_fn)
        frames.append(board)

        print(board)
        breakpoint()

    return frames


def save_to_gif(frames, name, fps):
    frames = [Image.fromarray(frame.astype(np.uint8)) for frame in frames]
    frames[0].save(
        name,
        format="GIF",
        append_images=frames[1:],
        save_all=True,
        duration=len(frames) / fps,
        loop=0,
    )


if __name__ == "__main__":
    board = initialize_board(10)
    frames = play(board, digital_alive, n=100)
    save_to_gif(frames, "digital.gif", fps=10)
    frames = play(board, quantum_alive, n=100)
    save_to_gif(frames, "quantum.gif", fps=10)
