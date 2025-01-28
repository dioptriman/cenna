from scipy.signal import savgol_filter, find_peaks
import matplotlib.pyplot as plt
import pandas as pd

# Load the text file into a Pandas DataFrame
file_path = "PPG-Sample.txt"  # Replace with your actual file path
df = pd.read_csv(file_path, sep=";")

# Apply Savitzky-Golay filter to denoise Channel 1
window_length = 51  # Ensure this is an odd number and smaller than the signal length
polyorder = 3       # Order of the polynomial
denoised_channel_1 = savgol_filter(df["channel 1"], window_length, polyorder)

# Detect peaks in the denoised Channel 1 signal
peaks, properties = find_peaks(denoised_channel_1, height=None, distance=100)

# Check if 'peak_heights' exists before accessing it
if "peak_heights" in properties:
    peak_heights = properties["peak_heights"]
    print(f"Number of peaks detected: {len(peaks)}")
    print(f"Peak indices: {peaks}")
    print(f"Peak heights: {peak_heights}")
else:
    print(f"No peaks detected. Check signal or adjust parameters.")

# Plot the signal and detected peaks
plt.figure(figsize=(14, 7))
plt.plot(df["Phone timestamp"], denoised_channel_1, label="Denoised Signal (Channel 1)", linewidth=2)

# Plot peaks if detected
if len(peaks) > 0:
    plt.plot(
        df["Phone timestamp"].iloc[peaks],  # Use .iloc for DataFrame indexing
        denoised_channel_1[peaks],         # Use standard indexing for NumPy arrays
        "x", label="Detected Peaks", color="red"
    )

plt.title("Peak Detection on Denoised Signal (Channel 1)")
plt.xlabel("Time (Phone Timestamp)")
plt.ylabel("Signal Value")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
