#
#Spectrogram.py
#
#Generates a spectrogram given the path to a .wav file or complex matrix.
#
#Should contain spectrogram_color(...) and spectrogram_bw(...)
#
#Frequency (Hz) will be plotted on the y-axis.
#Intensity (dB) will be plotted by color
#Time (ms) will be plotted on the x-axis
#
#spectrogram_color(...) will plot based on a some custom color scheme where brighter = higher intensity
#spectrogram_bw(...) will plot black, RGB(0, 0, 0), for an intensity of 0 and white, RGB(255, 255, 255) for the maximum intensity,
#which differes per audio file.
#
#Requirements:
# * Both functions output a matrix that represnts an image. It should compatible with OpenCV 4 (cv2) images
# * Scaling on the x-axis. ie, if the maximum length of the monitor is 1080 pixels and the needed pixels is 10x the amount,
#   show every 10th sample.
# * Scaling on the y-axis. Set a parameter to specify the minimum and maximum frequency to show
# * Labeled y-axis from 0 Hz to the sample rate of the audio
# * Labeled x-axis from 0 s to however long the audio is. Ideally, the measurement will adjust based on length.
# * Shows intensity based on the above description
# * Passes tests that we'll figure out later
#
#Nice-to-Haves:
# * Generate the image
#
#How to use the API to get the data you need
#
#1) call python.main.io.audio_reader.wav_to_vec(path) to get the raw audio data
#2) call python.main.util.format.vec_to_mat(raw audio data, N) choose N as a power of two. Play around with different values.
#   256, 512, and 1024 are probably going to be the best choices. This will be your y-axis height. N specifies the number of
#   frequency bins you have.
#3) call python.main.mapping.real_to_cmplx_obj_mat(mat) to convert step 2 to a matrix of complex numbers
#4) call src.python.main.signal_processing.fft.fft_mat(raw audio data) this is the step that turns your audio data into
#   something that's actually useful.
#
#FFT Matrix Structure
#
#   2-dimensional list
#
#                audio samples
#            --------
#           |complex_num, complex_num, ...
#  N (bins) |complex_num, ...,
#           |...,
#
#complex_num Structure
# * see python.main.math.complex_num and python.tests.math.test_complex_num
#
#
#
#Other useful functions
# * You can get the intensity at any given point in your FFT matrix by calling python.main.signal_processing.analyzation.get_intensity(complex_num, int N)
# * You can get the frequency of any frequency bin by calling python.main.singal_processing.bin_to_hz(bin, N, sample_rate)
#   bin is the bin from 0 to N that you want to find the frequency of
#   N is your FFT sizefrom step 2.
#   sample_rate is the audio sampling rate. 44,100 Hz is the most common, so it's best to use initially
#
