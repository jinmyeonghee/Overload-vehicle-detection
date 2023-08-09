# 과적 차량을 인식하여 단속하는 서비스
**프로젝트기간 : 2023.03.10 ~ 2023.03.21**

**사용 언어 : <img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white"/>**

**개발환경 : macOS Ventura 13.1, <img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=flat&logo=visualstudiocode&logoColor=white"/>**

**사용모델 : yolov5**

***
### 프로젝트 개요
- 해당 프로젝트에서 yolov5를 활용, 주어진 영상 내 과적 차량을 인식하여 박스로 표시하는 모델을 제작

### 프로젝트 배경
- 고속도로에서의 사고위험요소 중 화물자동차의 과적운행은 도로 파손의 원인이 될 뿐만 아니라 주변 운행차량에 사고를 유발하는 등 근절대책이 시급한 실정

   
## 프로젝트 내용
### 1. yolov5 모델 연구
<img width="1046" alt="과적차량1" src="https://github.com/jinmyeonghee/Overload-vehicle-detection/assets/114460314/7d7d5395-977e-4aa1-999e-d1da7eb71a50">

### 2. 학습데이터(대형차의 과적차량과 정상차량)를 학습
<img width="987" alt="스크린샷 2023-08-09 오후 4 56 58" src="https://github.com/jinmyeonghee/Overload-vehicle-detection/assets/114460314/13bae654-56aa-42da-a614-01f499b0c7a7">

### 3. 추가데이터 학습sample데이터로 모델테스트
<img width="1036" alt="스크린샷 2023-08-09 오후 4 57 26" src="https://github.com/jinmyeonghee/Overload-vehicle-detection/assets/114460314/5e184c7f-8ee2-4ed8-8185-302b6d592360">

- 두번째 학습에서 데이터를 추가적으로 학습. 백그라운드 이미지를 활용.
  - 해당 프로젝트는 클래스가 2개밖에 되지 않기때문에 confidence score가 (물체를 잡지 못 하는 것에 대해서) 학습이 잘 되지 않는 경우가 많은데, 백그라운드 이미지를 통해 어느 정도 학습할 수 있기 때문에 성능이 높아졌을 것으로 생각됩니다.

### 프로젝트 한계 및 개선방안

- 학습데이터에 <대형차>만 있었기때문에 소형차, 중형차에 대한 과적차량을 잘 인식하지 못함
  -> 소형차, 중형차도 같이 학습을 시키면 더 높은 성능을 낼 수 있을 것이다.
- 모델의 성능 평가 측면에서 클래스가 적으므로 mPA를 무조건적으로 신뢰할 수 없음
  -> 따라서 다양한 클래스 및 이미지를 추가하여 학습하는 것이 좋을 것이다.



# 패키지 설명

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

