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
        return None, f"Ошибка: Файл с именем {new_image_path} уже существует."
    
    try:
        os.rename(image_path, new_image_path)
        return new_image_path, None
    except Exception as e:
        return None, f"Ошибка: {e}"

def open_file():
    """Открывает диалог выбора файла и загружает изображение."""
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
    if image_path:
        show_image(image_path)
        info, error = get_image_info(image_path)
        if error:
            messagebox.showerror("Ошибка", error)
            return

        # Печатаем информацию об изображении
        info_text.set(f"Ширина: {info['width']} пикселей\n"
                      f"Высота: {info['height']} пикселей\n"
                      f"Размер: {info['size']} байт\n"
                      f"Дата создания: {info['creation_time']}")

        global current_image_path
        current_image_path = image_path

def show_image(image_path):
    """Отображает изображение в окне."""
    img = Image.open(image_path)
    img.thumbnail((400, 400))  # Уменьшаем размер изображения для отображения
    img_tk = ImageTk.PhotoImage(img)

    # Обновляем метку с изображением
    image_label.config(image=img_tk)
    image_label.image = img_tk  # Сохраняем ссылку на изображение

def rename_and_display():
    """Переименовывает изображение и обновляет отображение."""
    new_name = new_name_entry.get()
    if not new_name:
        messagebox.showwarning("Предупреждение", "Введите новое имя для изображения.")
        return

    new_image_path, error = rename_image(current_image_path, new_name)
    if error:
        messagebox.showerror("Ошибка", error)
        return

    messagebox.showinfo("Успех", f"Изображение успешно переименовано в: {new_image_path}")
    show_image(new_image_path)  # Обновляем отображаемое изображение

# Создаем главное окно
root = tk.Tk()
root.title("Просмотр изображений")

# Создаем элементы интерфейса
frame = tk.Frame(root)
frame.pack()

open_button = tk.Button(frame, text="Открыть изображение", command=open_file)
open_button.pack()

image_label = tk.Label(frame)
image_label.pack()

info_text = tk.StringVar()
info_label = tk.Label(frame, textvariable=info_text)
info_label.pack()

new_name_entry = tk.Entry(frame)
new_name_entry.pack()
new_name_entry.insert(0, "Введите новое имя")

rename_button = tk.Button(frame, text="Переименовать изображение", command=rename_and_display)
rename_button.pack()

# Переменная для хранения текущего пути к изображению
current_image_path = ""
# Запускаем главный цикл приложения
root.mainloop()