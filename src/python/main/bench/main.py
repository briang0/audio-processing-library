#This class is for testing. It won't be a part of the api
import numpy as np
import cv2
from src.python.main.graphing import Spectrogram
from src.python.main.io import Reader, AudioReader
from src.python.main.signal_processing import Fft
from src.python.main.signal_processing.Windowing import hanning
from src.python.main.util import Mapping, Formatter

path = "../../../../resources/515.wav"

# fft_size = 128

samples, sample_width = AudioReader.wav_to_vec(path)
sample_rate = 44100
print("Done reading")
num_samples = len(samples)
print(num_samples, "samples at ", sample_rate, " Hz")
complex_samples = Mapping.real_to_cmplx_obj_vec(samples)
fft_size = 128
overlap = fft_size // 2
fft_matrix = Fft.short_time_fft(complex_samples, fft_size, overlap)
print(np.array(fft_matrix).shape)
print("Done transforming")
spectrogram = Spectrogram.plot_spectrogram(fft_matrix, 1000, 500, fft_size)
cv2.imshow("Spectrogram", spectrogram)
while 1:
    cv2.waitKey(500)

# for row in fft_mat:
#     print(anlyz.get_signal_magnitude_similarity(row, row, 1.0))

