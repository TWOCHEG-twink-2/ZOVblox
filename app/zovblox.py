import os
import sys
import ctypes
import pygame
import tkinter as tk
from tkinter import messagebox
import tempfile
import shutil
import random


# Функция для установки обоев
def set_wallpaper(image_path):
    # Windows API для изменения обоев
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)


# Функция для возврата обоев в исходное состояние
def reset_wallpaper(original_wallpaper):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, original_wallpaper, 3)


# Функция для воспроизведения музыки в цикле
def play_music(music_path):
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)  # -1 означает зацикливание музыки


# Функция для остановки музыки
def stop_music():
    pygame.mixer.music.stop()


# Функция для извлечения файлов из встроенного архива
def extract_resource(file_name):
    # Получаем путь к временной папке, где хранятся ресурсы при запуске .exe
    resource_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(resource_path, file_name)
    return file_path


# Функция для отображения окна с кнопкой
def show_window():
    root = tk.Tk()
    root.title("ZOVblox")

    # Настроим окно так, чтобы оно не было растягиваемым
    root.geometry("600x200")
    root.resizable(False, False)

    # Добавим текст
    label = tk.Label(root, text="ZOVblox к сожалению не готов\n(и некогда не будет)\nмогу предложить только это", font=("Arial", 12))
    label.pack(pady=20)

    # Кнопка для завершения
    button = tk.Button(root, text="ну ладно(", font=("Arial", 12), command=root.quit)
    button.pack(pady=10)

    # Ожидание закрытия окна
    root.mainloop()


# Основная функция
def main(image_filenames, music_filename):
    # Случайный выбор изображения для обоев
    chosen_image_filename = random.choice(image_filenames)

    # Извлекаем путь к встроенным файлам
    image_path = extract_resource(chosen_image_filename)
    music_path = extract_resource(music_filename)

    # Сохраняем текущие обои
    original_wallpaper_path = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper")
    original_wallpaper = None
    if os.path.exists(original_wallpaper_path):
        # Сохраняем текущие обои, чтобы восстановить их позже
        original_wallpaper = tempfile.mktemp(suffix=".jpg")
        shutil.copy(original_wallpaper_path, original_wallpaper)

    # Устанавливаем новые обои и начинаем воспроизведение музыки
    set_wallpaper(image_path)
    play_music(music_path)

    # Показываем окно с кнопкой и ждем его закрытия
    show_window()

    # После закрытия окна восстанавливаем старые обои и останавливаем музыку
    if original_wallpaper:
        reset_wallpaper(original_wallpaper)
    stop_music()


if __name__ == "__main__":
    # Укажите имена файлов с изображениями и музыкой, которые будут встраиваться в .exe
    image_filenames = ["zov_1.PNG", "zov_2.jpg", "zov_3.jpg"]  # Имена файлов с изображениями
    music_filename = "music.mp3"  # Имя файла с музыкой

    main(image_filenames, music_filename)
