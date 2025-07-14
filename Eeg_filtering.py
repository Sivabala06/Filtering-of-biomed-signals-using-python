import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Load EEG data from a CSV file
eeg = np.loadtxt('signals/raw_eeg.csv')  # Make sure the file exists
fs = 250  # Sampling frequency (Hz)

# Bandpass filter design (0.5 to 45 Hz for EEG)
def bandpass_filter(signal, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs  # Nyquist frequency
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal)

# Apply the filter
filtered_eeg = bandpass_filter(eeg, 0.5, 45, fs)

# Plot raw vs filtered EEG
plt.figure(figsize=(10, 4))
plt.plot(eeg, label='Raw EEG', alpha=0.6)
plt.plot(filtered_eeg, label='Filtered EEG', linewidth=2)
plt.title('EEG Signal - Before and After Filtering')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/eeg_before_after.png')
plt.show()
