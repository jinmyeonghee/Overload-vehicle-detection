from utils.detect import Detection
import cv2

# .onnx 파일로부터 모델 불러오기
model = cv2.dnn.readNetFromONNX('./models/best.onnx')

# 입력데이터(동영상) 열기
cap = cv2.VideoCapture('./sample/sample1.mp4')
# 검증하고자 하는 영상의 경로를 적어주세요. 샘플영상이 없다면 sample폴더의 영상을 사용하면 됩니다.

# 동영상 프레임 단위 추론
# 결과 동영상을 저장할 VideoWriter 객체 생성
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./results/output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))


while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    # 입력데이터 전처리
    resized_frame = cv2.resize(frame, (416, 416))
    preprocessed_frame = cv2.dnn.blobFromImage(resized_frame, 
                                               scalefactor=1.0/255.0, 
                                               size=(416, 416), 
                                               mean=(0, 0, 0), 
                                               swapRB=True, 
                                               crop=False)
    # 모델추론
    model.setInput(preprocessed_frame)
    output = model.forward()

    # 출력데이터 후 처리
    # 출력 데이터가 바운딩 박스인 경우
    for bbox in output:
        x, y, w, h = bbox
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 결과 동영상에 프레임 추가
    out.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()