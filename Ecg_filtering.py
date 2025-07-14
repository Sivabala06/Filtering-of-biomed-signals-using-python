import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Load ECG data
ecg = np.loadtxt('signals/raw_ecg.csv')  # Simple .csv signal
fs = 250  # Sampling frequency in Hz

# Bandpass filter design
def bandpass_filter(signal, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal)

# Filter the ECG signal
filtered_ecg = bandpass_filter(ecg, 0.5, 40, fs)

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(ecg, label='Raw ECG', alpha=0.6)
plt.plot(filtered_ecg, label='Filtered ECG', linewidth=2)
plt.title('ECG Signal - Before and After Filtering')
