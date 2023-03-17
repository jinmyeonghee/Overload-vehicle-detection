import os
import json

# train box txt파일로 추출
# 폴더 내 JSON 파일 리스트 가져오기
json_files = [f for f in os.listdir('/Users/jinmh/Desktop/overload_data2/train/json_data') if f.endswith('.json')]

# data에 labels 폴더 생성
os.makedirs('/Users/jinmh/Desktop/overload_data2/train/labels', exist_ok=True)

for json_file in json_files:
    with open(os.path.join('/Users/jinmh/Desktop/overload_data2/train/json_data', json_file)) as f:
        data = json.load(f)
        items = data['FILE'][0]['ITEMS']  # items에 라벨 정보 저장
        img_width, img_height = map(int, data['FILE'][0]['RESOLUTION'].split("*"))

        classes = {'불법차량': 0, '정상차량': 1}  # 클래스 ID 매핑 정보

        for item in items:
            class_name = item["PACKAGE"]
            class_id = classes[class_name]

            # X1, Y1, X2, Y2 (라벨링구분이 Box인 경우 필수)
            box = item['BOX'].split(',')
            x1, y1, x2, y2 = float(box[0]), float(box[1]), float(box[2]), float(box[3])
            
            # 바운딩 박스 좌표값을 이용하여 YOLO 형식의 라벨 정보 생성
            dw = 1. / img_width
            dh = 1. / img_height

            x = x1 + x2 / 2.0
            y = y1 + y2 / 2.0
            w = x2
            h = y2
        
            x_center = x * dw
            width = w * dw
            y_center = y * dh
            height = h * dh

            yolo_label = f"{class_id} {x_center} {y_center} {width} {height}"

            # 라벨 파일 생성 및 저장
            filename = os.path.splitext(json_file)[0] + '.txt'  # 이미지 파일 이름과 동일한 이름으로 .txt 파일 생성
            with open(os.path.join('/Users/jinmh/Desktop/overload_data2/train/labels', filename), 'w') as f:
                f.write(yolo_label)

# ============================
# valid box txt파일로 추출
# 폴더 내 JSON 파일 리스트 가져오기
json_files = [f for f in os.listdir('/Users/jinmh/Desktop/overload_data2/valid/json_data') if f.endswith('.json')]

# data에 labels 폴더 생성
os.makedirs('/Users/jinmh/Desktop/overload_data2/valid/labels', exist_ok=True)

for json_file in json_files:
    with open(os.path.join('/Users/jinmh/Desktop/overload_data2/valid/json_data', json_file)) as f:
        data = json.load(f)
        items = data['FILE'][0]['ITEMS']  # items에 라벨 정보 저장
        img_width, img_height = map(int, data['FILE'][0]['RESOLUTION'].split("*"))

        classes = {'불법차량': 0, '정상차량': 1}  # 클래스 ID 매핑 정보

        for item in items:
            class_name = item["PACKAGE"]
            class_id = classes[class_name]

            # X1, Y1, X2, Y2 (라벨링구분이 Box인 경우 필수)
            box = item['BOX'].split(',')
            x1, y1, x2, y2 = float(box[0]), float(box[1]), float(box[2]), float(box[3])
            
            # 바운딩 박스 좌표값을 이용하여 YOLO 형식의 라벨 정보 생성
            dw = 1. / img_width
            dh = 1. / img_height

            x = x1 + x2 / 2.0
            y = y1 + y2 / 2.0
            w = x2
            h = y2
        
            x_center = x * dw
            width = w * dw
            y_center = y * dh
            height = h * dh

            yolo_label = f"{class_id} {x_center} {y_center} {width} {height}"

            # 라벨 파일 생성 및 저장
            filename = os.path.splitext(json_file)[0] + '.txt'  # 이미지 파일 이름과 동일한 이름으로 .txt 파일 생성
            with open(os.path.join('/Users/jinmh/Desktop/overload_data2/valid/labels', filename), 'w') as f:
                f.write(yolo_label)