import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

# WAV 파일 경로
wav_file = 'output.wav'

# WAV 파일 로드
sample_rate, audio_data = wavfile.read(wav_file)

# FFT를 위한 설정
frame_size = 1024
hop_size = 256

# Spectrogram 계산
_, _, spectrogram, _ = plt.specgram(audio_data, NFFT=frame_size, Fs=sample_rate, noverlap=frame_size-hop_size)

# Spectrogram 시각화
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Spectrogram')
plt.colorbar(label='Magnitude')
plt.show()