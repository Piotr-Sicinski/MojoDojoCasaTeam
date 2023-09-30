import numpy as np
import matplotlib.pyplot as plt

def quantum_wave_function(x, k, x0, t=0, hbar=1, m=1):
    """
    Generates a wave function Psi(x, t) for a free particle.
    :param x: Position (numpy array)
    :param k: Wave number
    :param x0: Initial position of the particle
    :param t: Time
    :param hbar: Reduced Planck's constant
    :param m: Mass of the particle
    :return: Wave function (numpy array)
    """
    # Calculate the wave function using the free particle solution to Schrodinger's equation
    return np.exp(1j * (k * x - hbar * k**2 * t / (2 * m))) * np.exp(-((x - x0) ** 2) / (4 * hbar * t / m + 1))

def classical_wave_function(x, frequency, amplitude, phase=0):
    """
    Generates a classical wave function.
    :param x: Position (numpy array)
    :param frequency: Frequency of the wave
    :param amplitude: Amplitude of the wave
    :param phase: Phase shift of the wave
    :return: Wave function (numpy array)
    """
    return amplitude * np.sin(2 * np.pi * frequency * x + phase)


if __name__ == "__main__":
    # Generate the wave function
    x = np.linspace(-10, 10, 1000)
    psi = quantum_wave_function(x, k=1, x0=0)
    print(psi)

    # Plot the Real and Imaginary Parts of the Wave Function
    plt.plot(x, psi.real, label='Real part')
    plt.plot(x, psi.imag, label='Imaginary part')
    plt.title('Quantum Wave Function')
    plt.xlabel('Position')
    plt.ylabel('Wave Function')
    plt.legend()
    plt.show()

    # Generate the classical wave function
    x = np.linspace(0, 1, 1000)
    wave = classical_wave_function(x, frequency=2, amplitude=1)

    # Plot the Wave Function
    plt.plot(x, wave)
    plt.title('Classical Wave Function')
    plt.xlabel('Position')
    plt.ylabel('Amplitude')
    plt.show()