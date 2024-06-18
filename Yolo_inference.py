from ultralytics import YOLO

model = YOLO('yolov8m')

results = model.predict('input_videos/DJI_0025 (1).MOV/', save = True)
print(results[0])
for box in results.boxes:
    print(box)

