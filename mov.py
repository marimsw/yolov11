import cv2
import os

def extract_frames_from_videos(
    video_dir=r"D:/Marina_rabota/тест/тест",  # Папка с видео
    output_dir=r"D:/Marina_rabota/photo",  # Создаем отдельную папку для кадров
    frame_interval=30,
    valid_extensions=('.mov', '.MOV')
):
    """
    Извлекает кадры из видеофайлов с заданным интервалом.
    
    Параметры:
        video_dir (str): Путь к папке с видео.
        output_dir (str): Папка для сохранения кадров.
        frame_interval (int): Сохранять каждый N-й кадр.
        valid_extensions (tuple): Разрешенные расширения видеофайлов.
    """
    # Создаем папку для кадров (если её нет)
    os.makedirs(output_dir, exist_ok=True)
    
    # Перебираем файлы в video_dir
    for video_file in os.listdir(video_dir):
        # Проверяем расширение файла
        if not video_file.lower().endswith(valid_extensions):
            print(f"Пропуск файла {video_file}: неверное расширение")
            continue
        
        video_path = os.path.join(video_dir, video_file)
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print(f"Ошибка: не удалось открыть видео {video_file}")
            continue
        
        frame_count = 0
        saved_count = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Сохраняем каждый N-й кадр
            if frame_count % frame_interval == 0:
                frame_name = f"{os.path.splitext(video_file)[0]}_frame_{frame_count:04d}.jpg"
                frame_path = os.path.join(output_dir, frame_name)
                cv2.imwrite(frame_path, frame)
                saved_count += 1
            
            frame_count += 1
        
        cap.release()
        print(f"Обработано: {video_file} → {frame_count} кадров, сохранено {saved_count}")

# Запуск функции
extract_frames_from_videos()