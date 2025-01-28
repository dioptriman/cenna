import pandas as pd
import matplotlib.pyplot as plt

# Load the text file into a Pandas DataFrame
file_path = "PPG-Sample.txt"  # Replace with the path to your file
df = pd.read_csv(file_path, sep=";")

# Convert the "Phone timestamp" column to datetime
df["Phone timestamp"] = pd.to_datetime(df["Phone timestamp"])

# Extract data channels
data_channel_0 = df["channel 0"]
data_channel_1 = df["channel 1"]
data_channel_2 = df["channel 2"]

# Plot each channel over time
plt.figure(figsize=(14, 7))
plt.plot(df["Phone timestamp"], data_channel_0, label="Channel 0", marker=".")
plt.plot(df["Phone timestamp"], data_channel_1, label="Channel 1", marker=".")
plt.plot(df["Phone timestamp"], data_channel_2, label="Channel 2", marker=".")

# Customize the plot
plt.title("PPG Data Over Time")
plt.xlabel("Time (Phone Timestamp)")
plt.ylabel("Signal Value")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()