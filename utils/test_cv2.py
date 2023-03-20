import torch
import detection

model_path = '/Users/jinmh/Desktop/CP1/models/best.pt'
model = torch.hub.load('jinmyeonghee/Overload-vehicle-detection', 'custom', path=model_path, force_reload=False, trust_repo=True)

input_video = '/Users/jinmh/Desktop/CP1/sample/sample5.mp4'
output_video = 'output_video5.mp4'

detection.detection(model = model,
          input_video = input_video,
          output_video = output_video)