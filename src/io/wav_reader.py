import numpy as np

def wav_to_vecD(path):
    if (path is None):
        raise Exception("Path can't be None.")

    if (not isinstance(path, str)):
        raise Exception("Path should be string, but was", type(path))

    ext = path.lower()[:-4]
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
    a = array.array(size)
    a.fromfile(open(path, 'rb'), int(os.path.getsize(path) / a.itemsize))
    bytes = a.tolist()
    audio.close()

    return bytes
