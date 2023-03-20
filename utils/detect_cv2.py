import cv2
import torch
from tqdm import tqdm

def detection(input_video, output_video, model):
    cap = cv2.VideoCapture(input_video)
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


    out = cv2.VideoWriter(output_video, codec, fps, (width, height))

    with tqdm(total=total_frames, desc="Processing", unit="frame") as pbar:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame)
            result_frame = results.render()[0]
            out.write(result_frame)
            pbar.update(1)

    cap.release()
    out.release()
    cv2.destroyAllWindows()