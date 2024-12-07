import os
import sys
import ctypes
import pygame
import customtkinter as ctk
import tempfile
import shutil
import random


def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)


def reset_wallpaper(original_wallpaper=None):
    default_wallpaper = os.path.expanduser("C:\\Windows\\Web\\Wallpaper\\Windows\\img0.jpg")
    wallpaper_to_set = original_wallpaper if original_wallpaper and os.path.exists(original_wallpaper) else default_wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_to_set, 3)


def play_music(music_path):
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)


def stop_music():
    pygame.mixer.music.stop()


def extract_resource(file_name):
    resource_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(resource_path, file_name)
    return file_path


def show_window():
    # Настройка темы и цветовой схемы
    ctk.set_appearance_mode("dark")  # Темная тема
    ctk.set_default_color_theme("blue")  # Цветовая тема

    root = ctk.CTk()  # Создаем окно с использованием customtkinter
    root.title("ZOVblox")
    root.geometry("600x300")
    root.resizable(False, False)

    # Закругленные края окна
    root.overrideredirect(True)  # Убираем стандартные кнопки управления окна
    root.after(10, lambda: root.wm_attributes("-transparentcolor", "#2b2b2b"))
    root.configure(bg="#2b2b2b")

    # Основной контейнер
    frame = ctk.CTkFrame(root, corner_radius=20, fg_color=("gray75", "gray30"))
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Заголовок
    label = ctk.CTkLabel(frame, text="ZOVblox к сожалению не готов\n(и некогда не будет)\nмогу предложить только это",
                         font=ctk.CTkFont("Arial", size=16, weight="bold"))
    label.pack(pady=20)

    # Кнопка
    button = ctk.CTkButton(frame, text="ну ладно(", command=root.quit, corner_radius=15)
    button.pack(pady=20)

    # Градиентный фон для кнопки (дополнительно)
    def gradient_button_hover(event):
        button.configure(fg_color=("#1f6aa5", "#144a70"))  # Меняем цвет при наведении

    def gradient_button_leave(event):
        button.configure(fg_color=("#3a7ebf", "#1f6aa5"))  # Возвращаем исходный цвет

    button.bind("<Enter>", gradient_button_hover)
    button.bind("<Leave>", gradient_button_leave)

    # Функция для закрытия окна при клике на любую часть окна
    def on_close(event=None):
        root.quit()

    # Закрытие по нажатию на ESC
    root.bind("<Escape>", on_close)

    root.mainloop()


def main(image_filenames, music_filename):
    chosen_image_filename = random.choice(image_filenames)

    image_path = extract_resource(chosen_image_filename)
    music_path = extract_resource(music_filename)

    original_wallpaper_path = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper")
    original_wallpaper = None
    if os.path.exists(original_wallpaper_path):
        original_wallpaper = tempfile.mktemp(suffix=".jpg")
        shutil.copy(original_wallpaper_path, original_wallpaper)

    set_wallpaper(image_path)
    play_music(music_path)

    show_window()

    reset_wallpaper(original_wallpaper)
    stop_music()


if __name__ == "__main__":
    image_filenames = ["zov_1.jpg", "zov_2.jpg", "zov_3.jpg", "zov_4.jpg"]
    music_filename = "music.mp3"

    main(image_filenames, music_filename)

# команда для создания exe
# выполните в терминале проекта
# pyinstaller --add-data "assets\img\zov_1.jpg;." --add-data "assets\img\zov_2.jpg;." --add-data "assets\img\zov_3.jpg;." --add-data "assets\img\zov_4.jpg;." --add-data "assets\music\music.mp3;." --onefile --windowed --icon=assets\img\icon.ico app\zovblox.py
# все временные файлы после удалите
