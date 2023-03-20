# Overload-vehicle-detection

## 과적 차량을 인식하여 단속하는 서비스

### 폴더 설명

- sample : 모델 추론의 입력값으로 사용할 영상 파일들이 저장되어 있는 폴더입니다.

- models : 추론에 사용될 사전 학습된 모델의 가중치 파일(best.pt)이 저장되어 있습니다.

- utils : models 내 모델을 통해 영상 내 객체를 탐지하는 object detection을 진행하고 결과를 .mp4 형태로 생성하는 detect 모듈이 저장되어 있습니다.

- results : detect_cv2.py에 의해 생성된 결과 영상이 해당 폴더에 저장되게 됩니다.

- test : 해당 패키지가 정상적으로 작동하는지 확인하는 test_cv2.py 파일을 포함하고 있습니다.


### 패키지를 이용해 과적차량(불법차량)을 감지해봅시다. 

1. 먼저 이 레포지토리를 클론해주세요. (약 2분소요)

  -  `git clone https://github.com/jinmyeonghee/Overload-vehicle-detection.git`

2. 해당폴더에 들어간 후(`cd Overload-vehicle-detection`) python=3.8로 가상환경을 만들고,

  - `pip install -r requirements.txt` 필요한 라이브러리와 모듈을 설치합니다.

3. test_cv2 파일을 연 후 검증할 영상의 경로와 결과영상의 저장이름을 지정해주고 실행합니다.

4. 결과영상은 results 폴더에 있습니다.

