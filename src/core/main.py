import os, sys
sys.path.insert(0, os.path.abspath(".."))
import src.io.wav_reader as wr

path = "C:/Users/brian/Documents/Smasheo/Audio/King Dedede Sounds/dededehit.wav"

wr.wav_to_vec(path)
