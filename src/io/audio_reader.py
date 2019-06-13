import numpy as np
import os
import wave
import array

def wav_to_vec(path):
    if (path is None):
        raise Exception("Path can't be None.")

    if (not isinstance(path, str)):
        raise Exception("Path should be string, but was", type(path))

    ext = path.lower()[-4:]
    if (ext != ".wav"):
        raise Exception("Unexpected path extension! Expected .wav, but was", ext)
        return;

    exists = os.path.isfile(path)
    if (not exists):
        raise Exception(path, "does not exist.")
        return

    audio = wave.open(path, 'rb')
    fmt = {1:'B',2:'h',4:'i'}
    size = fmt[audio.getsampwidth()]
    c_array = array.array(size)
    c_array.fromfile(open(path, 'rb'), os.path.getsize(path) // c_array.itemsize)
    bytes = c_array.tolist()
    audio.close()

    print(bytes)

    return bytes
