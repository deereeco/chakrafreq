import os
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt

folder = "./soundFiles"

files = os.listdir(folder)

for file in files:

  currentDirectory = os.getcwd()
  print(currentDirectory + "/" + folder + "/"  + file)
  s_rate, signal = wavfile.read(currentDirectory + "/" + folder + "/"  + file)    # read file
  FFT = abs(scipy.fft(signal))                              # do FFT
  freqs = fftpk.fftfreq(len(FFT),(1.0/s_rate))              # make frequency vector

  #plot
  plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])
  plt.xlabel("Frequency (Hz)")
  plt.ylabel("Amplitude")
  plt.Text(0, 0.5, 'Amplitude')
  plt.show()

