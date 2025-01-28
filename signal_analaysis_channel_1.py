from scipy.signal import butter, filtfilt, find_peaks
import matplotlib.pyplot as plt
import pandas as pd

# Load the text file into a Pandas DataFrame
file_path = "PPG-Sample.txt"  # Replace with your actual file path
df = pd.read_csv(file_path, sep=";")

# Define a high-pass filter
def high_pass_filter(data, cutoff, fs, order=4):
    nyquist = 0.5 * fs  # Nyquist frequency
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

# Filter parameters
cutoff_frequency = 0.4  # Cutoff frequency (Hz), adjust based on your signal
sampling_frequency = 1000  # Sampling frequency (Hz), adjust according to your data
order = 4  # Filter order

# Apply high-pass filter to Channel 1
filtered_channel_1 = high_pass_filter(df["channel 1"], cutoff_frequency, sampling_frequency, order)

# Detect peaks in the filtered Channel 1 signal
peaks, properties = find_peaks(filtered_channel_1, height=None, distance=100000)

# Check for detected peaks
if "peak_heights" in properties:
    peak_heights = properties["peak_heights"]
    print(f"Number of peaks detected: {len(peaks)}")
    print(f"Peak indices: {peaks}")
    print(f"Peak heights: {peak_heights}")
else:
    print(f"No peaks detected. Check signal or adjust parameters.")

# Plot the filtered signal and detected peaks
plt.figure(figsize=(14, 7))
plt.plot(df["Phone timestamp"], filtered_channel_1, label="Filtered Signal (Channel 1)", linewidth=2)

# Plot peaks if detected
if len(peaks) > 0:
    plt.plot(
        df["Phone timestamp"].iloc[peaks],  # Use .iloc for DataFrame indexing
        filtered_channel_1[peaks],         # Use standard indexing for NumPy arrays
        "x", label="Detected Peaks", color="red"
    )

plt.title("Peak Detection on Filtered Signal (Channel 1)")
plt.xlabel("Time (Phone Timestamp)")
plt.ylabel("Signal Value")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
