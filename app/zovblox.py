import pygame
import threading
import ctypes
from win32con import SPI_SETDESKWALLPAPER, SPIF_UPDATEINIFILE, SPIF_SENDCHANGE


# Функция для смены обоев
def change_wallpaper(wallpaper_path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)


# Функция для получения текущих обоев
def get_current_wallpaper():
    # Чтение текущего пути к обоям через реестр
    import winreg
    reg_key = r"Control Panel\Desktop"
    reg_value = "Wallpaper"
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key) as key:
            wallpaper_path, _ = winreg.QueryValueEx(key, reg_value)
        return wallpaper_path
    except Exception as e:
        print(f"ошибка...: {e}")
        return None


# Функция для воспроизведения музыки
def play_music(music_file):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()


# Основная логика
def main():
    original_wallpaper = get_current_wallpaper()
    if not original_wallpaper:
        print("ошибка...")
        return

    new_wallpaper = "img.PNG"
    music_file = "modules/music.mp3"

    # Сменить обои на новые
    change_wallpaper(new_wallpaper)

    # Запустить музыку в отдельном потоке
    music_thread = threading.Thread(target=play_music, args=(music_file,))
    music_thread.start()

    # Ждем, пока пользователь не нажмет Enter или не закроет консоль
    input("ZZZZZZZZZZZZZZZ")

    # Восстановить обои
    if original_wallpaper:
        change_wallpaper(original_wallpaper)

    # Остановить музыку
    pygame.mixer.music.stop()


if __name__ == "__main__":
    main()
