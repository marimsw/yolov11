from ultralytics import YOLO

model = YOLO(r'D:\\Marina_rabota\\runs\\detect\\train\\weights\\best.pt')
results = model(r'D:\\Marina_rabota\\3_1_frame_2580.jpg')

# Показываем изображение с результатами
results[0].show()

# Обработка каждого объекта
for box in results[0].boxes:
    class_id = int(box.cls)
    class_name = model.names[class_id]
    confidence = box.conf.item()  # преобразуем тензор в число
    print(f'Объект: {class_name}, confidence: {confidence:.2f}')