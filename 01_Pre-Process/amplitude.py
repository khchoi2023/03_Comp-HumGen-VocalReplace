import numpy as np
import matplotlib.pyplot as plt
import wave

# WAV 파일 경로
wav_file = "input.wav"

# WAV 파일 로드
with wave.open(wav_file, 'rb') as wav:
    # 오디오 정보 추출
    params = wav.getparams()
    num_channels = params.nchannels
    sample_width = params.sampwidth
    num_frames = params.nframes
    sample_rate = params.framerate

    # 오디오 데이터 읽기
    frames = wav.readframes(num_frames)

# 오디오 데이터 변환 (바이너리 -> 숫자)
audio_data = np.frombuffer(frames, dtype=np.int16)

# 시간 계산 (오디오 샘플 수 / 샘플 속도)
duration = num_frames / sample_rate
time = np.linspace(0, duration, num=len(audio_data))

# 시각화
plt.figure(figsize=(10, 4))
plt.plot(time, audio_data, color='b')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Waveform')
plt.show()