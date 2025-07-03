from ultralytics import YOLO

model = YOLO('yolo11n.pt')
model.train(
    data='D:\Marina_rabota\my_data.yaml',
    epochs=100,
    imgsz=640
)