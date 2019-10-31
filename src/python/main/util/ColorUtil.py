def intensity_to_bgr_bw(intensity, max_intensity):
    val = (intensity / max_intensity) * 255
    r, g, b = int(val)
    return [b, g, r]


def intensity_to_rgb_bw(intensity, max_intensity):
    val = (intensity / max_intensity) * 255
    r, g, b = int(val)
    return [r, g, b]
