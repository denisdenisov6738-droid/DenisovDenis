import os
import datetime
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox

def get_image_info(image_path):
    """Получает информацию об изображении."""
    if not os.path.isfile(image_path):
        return None, f"Ошибка: Файл не найден по пути {image_path}"
    
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            size = os.path.getsize(image_path)
            creation_time = datetime.datetime.fromtimestamp(os.path.getctime(image_path)).strftime('%Y-%m-%d %H:%M:%S')
            return {
                'width': width,
                'height': height,
                'size': size,
                'creation_time': creation_time
            }, None
    except Exception as e:
        return None, f"Ошибка: {e}"

def rename_image(image_path, new_name):
    """Переименовывает изображение."""
    if not os.path.isfile(image_path):
        return None, f"Ошибка: Файл не найден по пути {image_path}"
    
    dir_name = os.path.dirname(image_path)
    ext = os.path.splitext(image_path)[1]
    new_image_path = os.path.join(dir_name, new_name + ext)

    if os.path.isfile(new_image_path):
        return None, f"Ошибка: