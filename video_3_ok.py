from ultralytics import YOLO
import cv2

model = YOLO(r'D:\Marina_rabota\runs\detect\train\weights\best.pt')
video_path = r'D:\Marina_rabota\тест\тест\3_1.MOV'

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Ошибка открытия видеофайла")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

output_path = r'D:\Marina_rabota\output2.mp4'  # лучше использовать mp4
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # или 'avc1'
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

if not out.isOpened():
    print("Не удалось открыть видео для записи")
    cap.release()
    exit()

# Размер окна для отображения
display_width = 800
display_height = 600

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    # Проверка формата изображения для записи
    if annotated_frame.dtype != 'uint8':
        annotated_frame = annotated_frame.astype('uint8')
    if len(annotated_frame.shape) == 2:
        annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_GRAY2BGR)

    # Записываем в файл
    out.write(annotated_frame)

    # Масштабируем для отображения
    display_frame = cv2.resize(annotated_frame, (display_width, display_height))
    cv2.imshow('Обнаружение объектов', display_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
