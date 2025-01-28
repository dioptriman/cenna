import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the text file into a Pandas DataFrame
file_path = "PPG-Sample.txt"  # Replace with your file path
df = pd.read_csv(file_path, sep=";")

# Extract Channel 2 data
channel_2 = df["channel 2"]

# Perform FFT
fft_result = np.fft.fft(channel_2)
frequencies = np.fft.fftfreq(len(channel_2), d=1)  # d=1 assumes 1-second intervals; adjust as needed

# Take magnitude of FFT and focus on positive frequencies
magnitude = np.abs(fft_result)
positive_freqs = frequencies[:len(frequencies) // 2]
positive_magnitude = magnitude[:len(magnitude) // 2]

# Plot the FFT result
plt.figure(figsize=(14, 7))
plt.plot(positive_freqs, positive_magnitude, label="FFT Magnitude (Channel 2)")
plt.title("Frequency Analysis of Channel 2")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
