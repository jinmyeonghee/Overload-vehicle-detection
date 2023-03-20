import cv2
import torch
from tqdm import tqdm # 아랍어로 Progress라는 의미, 진행률과 시간을 볼 수 있다.

def detection(input_video, output_video, model):
    cap = cv2.VideoCapture(input_video) # 저장된 비디오파일 재생(input_video). 비디오캡쳐를 위해 객체 생성
    
    codec = cv2.VideoWriter_fourcc(*'mp4v') # mp4v->.mp4
    # fourcc : 코덱을 지정하는 함수, 사용할 코덱 생성(4개의 문자를 인수로 취급)
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 프레임 가로 크기
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 프레임 세로 크기
    fps = int(cap.get(cv2.CAP_PROP_FPS)) # 초당 프레임의 수
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 비디오 파일의 총 프레임의 수

    out = cv2.VideoWriter(output_video, codec, fps, (width, height)) # 비디오 저장을 위한 객체 생성

    with tqdm(total=total_frames, desc="Processing", unit="frame") as pbar:
        while cap.isOpened(): # 비디오캡쳐 객체가 열렸는지 확인
            ret, frame = cap.read() 
            # 재생되는 비디오의 한 프레임씩 읽음. 프레임을 읽었다면 ret : True, 읽은 프레임 : frame
            if not ret: # 새로운 프레임을 못 받아 왔을때 break (ret이 False면 중지)
                break
            results = model(frame)
            result_frame = results.render()[0]
            out.write(result_frame) # 프레임 저장
            pbar.update(1)

    cap.release() # 오픈한 cap 객체를 해제
    out.release() # out 객체 해제
    cv2.destroyAllWindows() # 열린 모든 창을 닫음