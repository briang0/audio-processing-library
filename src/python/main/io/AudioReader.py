import os
import wave
import array

from scipy.io import wavfile


def wav_to_vec(path):
    if path is None:
        raise Exception("Path can't be None.")

    if not isinstance(path, str):
        raise Exception("Path should be string, but was", type(path))

    ext = path.lower()[-4:]
    if ext != ".wav":
        raise Exception("Unexpected path extension! Expected .wav, but was", ext)
        return;

    exists = os.path.isfile(path)
    if not exists:
        raise Exception(path, "does not exist.")
        return

    audio = wave.open(path, 'rb')
    fmt = {1: 'B', 2: 'h', 4: 'i'}
    sample_width = audio.getsampwidth()
    print(sample_width)
    size = fmt[sample_width]
    c_array = array.array(size)
    c_array.fromfile(open(path, 'rb'), os.path.getsize(path) // c_array.itemsize)
    array_bytes = c_array.tolist()
    audio.close()

    return array_bytes, sample_width

def wav_to_vec_sp(path):
    sample_rate, samples = wavfile.read(path)
    return sample_rate, samples