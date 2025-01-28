from scipy.signal import butter, filtfilt, find_peaks
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the text file into a Pandas DataFrame
file_path = "PPG-Sample.txt"  # Replace with your actual file path
df = pd.read_csv(file_path, sep=";")

# Define a high-pass filter
def high_pass_filter(data, cutoff, fs, order=4):
    nyquist = 0.5 * fs  # Nyquist frequency
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype="high", analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

# Filter parameters
cutoff_frequency = 0.1  # Adjust based on your signal
sampling_frequency = 50  # Sampling frequency in Hz
order = 4

# Apply high-pass filter to Channel 1
filtered_channel_1 = high_pass_filter(df["channel 1"], cutoff_frequency, sampling_frequency, order)

# Peak detection parameters
height_threshold = (-320000, 290000)  # Adjust range for valid peaks
distance_between_peaks = 100000  # Minimum distance between peaks in samples

# Detect peaks
peaks, properties = find_peaks(filtered_channel_1, height=height_threshold, distance=distance_between_peaks)

# Reset index to ensure peaks indices align with the DataFrame
df = df.reset_index(drop=True)

# Create a new column for stress labels
df["label"] = 0  # Default to 0 (not stressed)

# Mark detected peaks as 1 (stressed)
df.loc[peaks, "label"] = 1

# Create the dataset for SVM (filtered signal and labels)
svm_data = pd.DataFrame({
    "signal": filtered_channel_1,  # Feature: the filtered signal
    "label": df["label"],          # Label: 1 for stress, 0 otherwise
})

# Plotting the filtered signal with labeled peaks
plt.figure(figsize=(16, 8))
plt.plot(filtered_channel_1, label="Filtered Signal (Channel 1)", linewidth=2, color="blue")

# Highlight detected peaks
plt.scatter(
    peaks,
    filtered_channel_1[peaks],
    color="red",
    label="Detected Peaks (Stress)",
    s=50,
)

plt.title("Stress Detection: Peaks Labeled as Stress (1)")
plt.xlabel("Sample Index")
plt.ylabel("Signal Value")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Save SVM-compatible dataset
output_path = "svm_data.csv"
svm_data.to_csv(output_path, index=False)
print(f"SVM data saved to {output_path}")
