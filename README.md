# Overload-vehicle-detection

## 과적 차량을 인식하여 단속하는 서비스
고속도로에서의 사고위험요소 중 화물자동차의 과적운행은 도로 파손의 원인이 될 뿐만 아니라 주변 운행차량에 사고를 유발하는 등 근절대책이 시급한 실정입니다.

고속도로 과적차량 단속업무는 도로의 구조 보전과 도로에서의 차량운행으로 인한 위험방지를 목적으로 합니다.

이번에 ‘과적 차량을 인식하여 단속하는 서비스를 개발하는 프로젝트’를 진행해보았습니다.

해당 프로젝트에서 YOLOv5를 활용, 주어진 영상 내 과적 차량을 인식하여 박스로 표시하는 모델을 제작해보겠습니다.


## 개발환경
macOS Ventura 13.1

Visual Studio Code

사용모델 : yolov5
***
### 디렉토리 구조
```
Overload-vehicle-detection
├── models
│   └──best.pt
├── results
│   └──output_video1.mp4
├── sample
│   └──sample.mp4
│   └──sample1.mp4
├── test
│   └── test_cv2.py
├── utils
│   ├── __init__.py
│   └── detect_cv2.py
├── README.md
└── requirements.txt
```

### 폴더 설명

- models : 추론에 사용될 사전 학습된 모델의 가중치 파일(best.pt)이 저장되어 있습니다.

- results : detect_cv2.py에 의해 생성된 결과 영상이 해당 폴더에 저장되게 됩니다.

- sample : 모델 추론의 입력값으로 사용할 영상 파일들이 저장되어 있는 폴더입니다.

- test : 해당 패키지가 정상적으로 작동하는지 확인하는 test_cv2.py 파일을 포함하고 있습니다.

- utils : models 내 모델을 통해 영상 내 객체를 탐지하는 object detection을 진행하고 결과를 .mp4 형태로 생성하는 detect 모듈이 저장되어 있습니다.

- requirements.txt : 프로젝트에 필요한 라이브러리와 모듈 파일들이 작성되어 있습니다

***

### 패키지를 이용해 과적차량(불법차량)을 감지해봅시다. 

1. 먼저 이 레포지토리를 클론해주세요. (약 2분소요)

  - `git clone https://github.com/jinmyeonghee/Overload-vehicle-detection.git`

2. python=3.8 가상환경

  - `pip install -r requirements.txt` 필요한 라이브러리와 모듈을 설치합니다.

3. test_cv2 파일을 연 후 검증할 영상의 경로와 결과영상의 저장이름을 지정해주고 실행합니다.

4. 결과영상은 results 폴더에 있습니다.

