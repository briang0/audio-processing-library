import cv2
import numpy as np

from src.python.main.signal_processing.Analyzation import get_intensity, bin_to_hz


def plot_spectrogram(fft_matrix, length, height, fft_size):
    num_samples = len(fft_matrix)
    if num_samples < length:
        thickness = (length // num_samples)
    else:
        thickness = 1
    sample_rate = 44100
    max_frequency = 44100
    bin_frequency_range = sample_rate / fft_size
    frequency_height_ratio = max_frequency / height
    sample_ratio = num_samples / length
    spectrogram = np.zeros((height, length, 3), np.uint8)

    for i in range(0, num_samples):
        for j in range(0, fft_size):
            current_frequency = j * bin_frequency_range
            amplitude = get_intensity(fft_matrix[i][j])
            color = get_pixel_color(255 - amplitude)
            x1 = int(i / sample_ratio)
            x2 = x1
            y1 = int(current_frequency / frequency_height_ratio)
            y2 = int(frequency_height_ratio + y1)
            print(amplitude)
            # print(x1, x2, y1, y2, current_frequency)
            spectrogram = cv2.rectangle(spectrogram, (x1, y1), (x2 + thickness, y2), color, cv2.FILLED)
    return spectrogram


def get_horizontal_bin(indx, length, num_bins):
    return int((indx / (length - 1)) * num_bins)


def get_vertical_bin(indx, sample_rate, bin_size):
    return int(((bin_size-1) / sample_rate) * indx)


def get_pixel_color(intensity):
    if intensity <= 20:
        return intensity, 0, 0
    elif intensity <= 30:
        return intensity*2, 0, 0
    elif intensity <= 40:
        return intensity*4, 0, 0
    elif intensity <= 50:
        return intensity, intensity/2, 0
    elif intensity <= 60:
        return 0, intensity, 0
    elif intensity <= 70:
        return 0, intensity*2, 0
    elif intensity <= 80:
        return 0, intensity, intensity
    elif intensity <= 90:
        return 0,  intensity, intensity*2
    else:
        return intensity*2, intensity*2, intensity*2
