#pip install spleeter

import os
import time
from spleeter.separator import Separator

def split_audio(input_file, output_dir):
    # 입력 파일의 경로와 분리된 악기 파일을 저장할 디렉토리 경로 생성
    input_path = os.path.abspath(input_file)
    output_path = os.path.abspath(output_dir)
    
    # 디렉토리가 존재하지 않으면 생성
    os.makedirs(output_path, exist_ok=True)
    
    # 분리 작업 수행
    separator = Separator('spleeter:5stems')                # 5가지로 분리 : 보컬, 피아노, 드럼, 기타, others
    separator.separate_to_file(input_path, output_path)
    
    # 분리된 파일의 이름 변경
    filename = os.path.splitext(os.path.basename(input_file))[0]
    os.rename(os.path.join(output_path, 'vocals.wav'), os.path.join(output_path, f'{filename}_vocals.wav'))
    for stem in separator._params['stems'].keys():
        os.rename(os.path.join(output_path, f'{stem}.wav'), os.path.join(output_path, f'{filename}_{stem}.wav'))
    
    print('분리 완료')

# 사용 예시
if __name__ == '__main__':
    
    # for i in range(1, 66):         # 1 ~ 65까지
    for i in range(1, 7):
        input_file = f'{i}.mp3'   # 입력 파일 경로
        output_dir = 'output'     # 분리된 파일 저장 디렉토리 경로
        
        try:
            split_audio(input_file, output_dir)
        except:
            pass
        
        time.sleep(2)

    print("done")