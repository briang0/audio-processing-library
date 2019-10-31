
def intensity_to_bgr_bw(intensity, max):
    val = (intensity / max) * 255
    r, g, b = int(val)
    return [b, g, r]

def intensity_to_rgb_bw(intensity, max):
    val = (intensity / max) * 255
    r, g, b = int(val)
    return [r, g, b]
