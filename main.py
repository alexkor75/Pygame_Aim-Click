import pygame
import random
import time

pygame.init()
pygame.mixer.init()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Настройки игры
GAME_DURATION = 40  # секунд
TARGET_SCALE = 7  # Коэффициент уменьшения мишени

# Пути к ресурсам
ICON_PATH = "img/icon.png"
TARGET_PATH = "img/target.png"
MUSIC_PATH = "sounds/music.mp3"
CLICK_SOUND_PATH = "sounds/click.mp3"

# Скорости мишени
TARGET_SPEEDS = [-3, -2, -1, 1, 2, 3]


# Основной игровой цикл
def main():
    global score, start_time

    running = True
    clock = pygame.time.Clock()


    while running:
        pass


if __name__ == "__main__":
    main()
    pygame.quit()