#This class is for testing. It won't be a part of the api

import os, sys
sys.path.insert(0, os.path.abspath("../../.."))
import python.main.io.audio_reader as read
import python.main.signal_processing.fft as fft
import python.main.signal_processing.analyzation as anlyz
import python.main.util.format as fmt
import python.main.util.mapping as mapping

path = "C:/Users/brian/Documents/Smasheo/Audio/King Dedede Sounds/dededehit.wav"

# fft_size = 128
#
# data = read.wav_to_vec(path)
#
# mat = fmt.vec_to_mat(data, fft_size)
#
# cmplx_mat = mapping.real_to_cmplx_obj_mat(mat)
#
# fft_mat = fft.fft_mat(cmplx_mat)
#
# for row in fft_mat:
#     print(anlyz.get_signal_magnitude_similarity(row, row, 1.0))

dat = [1, 2, 3, 4, 5, 6, 7, 8]

dat_cmplx = mapping.real_to_cmplx_obj_vec(dat)

for num in dat_cmplx:
    print(num)

dat_fft = fft.fft(dat_cmplx)

for num in dat_fft:
    print(num)

# transform = fft.fft(data, 256)
