import os
import shutil
from sklearn.model_selection import train_test_split

def organize_dataset():
    # пути
    images_dir = r"D:\Marina_rabota\photo — копия" # Папка с изображениями
    labels_dir = r"D:\Marina_rabota\text_razm"  # Папка с аннотациями
    output_dir = r"D:\Marina_rabota\razmetka"  # Выходная папка
    
    # 1. Проверка существования исходных папок
    print("\nПроверка папок:")
    print(f"Папка с изображениями: {'существует' if os.path.exists(images_dir) else 'НЕ НАЙДЕНА!'}")
    print(f"Папка с аннотациями: {'существует' if os.path.exists(labels_dir) else 'НЕ НАЙДЕНА!'}")
    
    if not os.path.exists(images_dir) or not os.path.exists(labels_dir):
        raise FileNotFoundError("Проверьте пути к папкам с изображениями и аннотациями!")

    # 2. Создаю структуру папок
    print("\nСоздание структуры папок...")
    for folder in ["images/train", "images/val", "images/test", 
                   "labels/train", "labels/val", "labels/test"]:
        path = os.path.join(output_dir, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Создана папка: {path}")

    # 3. Получаем список изображений
    image_files = [f for f in os.listdir(images_dir) 
                  if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    image_basenames = [os.path.splitext(f)[0] for f in image_files]
    
    print(f"\nНайдено {len(image_basenames)} изображений")
    print("Примеры файлов:", image_basenames[:3])

    # 4. Получаем список аннотаций
    label_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]
    label_basenames = [os.path.splitext(f)[0] for f in label_files]
    
    print(f"\nНайдено {len(label_basenames)} аннотаций")
    print("Примеры аннотаций:", label_basenames[:3])

    # 5. Проверяем соответствие имен
    missing_annotations = set(image_basenames) - set(label_basenames)
    if missing_annotations:
        print(f"\nВнимание! Нет аннотаций для {len(missing_annotations)} изображений")
        print("Примеры:", list(missing_annotations)[:3])

    # 6. Разделяем данные
    common_files = list(set(image_basenames) & set(label_basenames))
    print(f"\nОбщих файлов (изображение + аннотация): {len(common_files)}")
    
    train_val, test = train_test_split(common_files, test_size=0.2, random_state=42)
    train, val = train_test_split(train_val, test_size=0.1, random_state=42)

    # 7. Копируем файлы
    print("\nКопирование файлов:")
    for split_name, split_files in [('train', train), ('val', val), ('test', test)]:
        print(f"\nОбработка {split_name} ({len(split_files)} файлов):")
        
        for basename in split_files:
            # Копируем изображение
            img_src = os.path.join(images_dir, f"{basename}.jpg")
            img_dst = os.path.join(output_dir, "images", split_name, f"{basename}.jpg")
            shutil.copy2(img_src, img_dst)
            
            # Копируем аннотацию
            lbl_src = os.path.join(labels_dir, f"{basename}.txt")
            lbl_dst = os.path.join(output_dir, "labels", split_name, f"{basename}.txt")
            shutil.copy2(lbl_src, lbl_dst)
            
            print(f"Скопировано: {basename}")

    print("\nГотово! Проверьте папки:")
    print(f"Изображения train: {len(os.listdir(os.path.join(output_dir, 'images/train')))}")
    print(f"Аннотации train: {len(os.listdir(os.path.join(output_dir, 'labels/train')))}")
    print(f"Изображения val: {len(os.listdir(os.path.join(output_dir, 'images/val')))}")
    print(f"Аннотации val: {len(os.listdir(os.path.join(output_dir, 'labels/val')))}")
    print(f"Изображения test: {len(os.listdir(os.path.join(output_dir, 'images/test')))}")
    print(f"Аннотации test: {len(os.listdir(os.path.join(output_dir, 'labels/test')))}")

# Запускаем функцию
organize_dataset()