import os, sys
sys.path.insert(0, os.path.abspath("../.."))
import src.io.audio_reader as read
import src.signal_processing.fft as fft
import src.util.format as fmt
import src.util.mapping as mapping

path = "C:/Users/brian/Documents/Smasheo/Audio/King Dedede Sounds/dededehit.wav"

data = read.wav_to_vec(path)

mat = fmt.vec_to_mat(data, 3)

cmplx_mat = mapping.real_to_cmplx_obj_mat(mat)

print(cmplx_mat)

# transform = fft.fft(data, 256)
