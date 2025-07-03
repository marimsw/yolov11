from ultralytics import YOLO

model = YOLO('D:\\Marina_rabota\\runs\\detect\\train\\weights\\best.pt')
results = model('D:\\Marina_rabota\\3_1_frame_2580.jpg')
results[0].show()