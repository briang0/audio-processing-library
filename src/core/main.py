#This class is for testing. It won't be a part of the api

import os, sys
sys.path.insert(0, os.path.abspath("../.."))
import src.io.audio_reader as read
import src.signal_processing.fft as fft
import src.signal_processing.analyzation as anlyz
import src.util.format as fmt
import src.util.mapping as mapping

path = "C:/Users/brian/Documents/Smasheo/Audio/King Dedede Sounds/dededehit.wav"

fft_size = 128

data = read.wav_to_vec(path)

mat = fmt.vec_to_mat(data, fft_size)

cmplx_mat = mapping.real_to_cmplx_obj_mat(mat)

fft_mat = fft.fft_mat(cmplx_mat)

for row in fft_mat:
    print(anlyz.get_max_intensity_cmplx_vec(row), anlyz.get_min_intensity_cmplx_vec(row) )

# transform = fft.fft(data, 256)
