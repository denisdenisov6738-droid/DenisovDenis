import os
from PIL import Image

current_path = None

while True:
    print("\n1 - Выбрать изображение")
    print("2 - Информация") 
    print("3 - Переименовать")
    
    choice = input("Выбор: ") #UI
    
    if choice == "1":
        path = input("Путь к файлу: ")
        if os.path.isfile(path):
            current_path = path
            print("Файл выбран")
        else:
            print("Файл не найден")
            
    elif choice == "2":
        if not current_path:
            print("Сначала выберите файл")
            continue
            
        try:
            with Image.open(current_path) as img:
                size = os.path.getsize(current_path)
                print(f"Файл: {os.path.basename(current_path)}")
                print(f"Размер: {img.size[0]}x{img.size[1]} пикселей")
                print(f"Вес: {size} байт")
                print(f"Формат: {img.format}")
        except:
            print("Ошибка открытия файла")
            
    elif choice == "3":
        if not current_path:
            print("Сначала выберите файл")
            continue
            
        new_name = input("Новое имя: ")
        if not new_name:
            print("Имя не может быть пустым")
            continue
            
        ext = os.path.splitext(current_path)[1]
        new_path = os.path.join(os.path.dirname(current_path), new_name + ext)
        
        if os.path.exists(new_path):
            print("Файл уже существует")
        else:
            os.rename(current_path, new_path)
            current_path = new_path
            print("Файл переименован")
            
    else:
        print("Неверный выбор")