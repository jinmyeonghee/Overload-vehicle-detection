import torch
import sys

sys.path.append('./utils')
import detect_cv2


# models의 가중치(best.pt)의 경로.
model_path = './models/best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=False, trust_repo=True)


# 검증 할 영상의 경로를 입력하세요. 샘플영상이 없다면 sample폴더의 영상을 사용하세요.
input_video = 'sample/sample.mp4'


# 결과영상의 저장이름을 지정해주세요.(results폴더에 저장 됨)
output_video = './results/output_video123.mp4'

detect_cv2.detection(model = model,
          input_video = input_video,
          output_video = output_video)

# 결과영상 파일은 /results 폴더에 있습니다.
