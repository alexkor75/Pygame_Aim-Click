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


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Target Game")
icon = pygame.image.load(ICON_PATH)
pygame.display.set_icon(icon)

try:
    pygame.mixer.music.load(MUSIC_PATH)
    pygame.mixer.music.play(-1)
except pygame.error:
    print("Не удалось загрузить или воспроизвести фоновую музыку.")

try:
    hit_sound = pygame.mixer.Sound(CLICK_SOUND_PATH)
except pygame.error:
    print("Не удалось загрузить звук попадания.")
    hit_sound = None

original_target_img = pygame.image.load(TARGET_PATH)
target_width = original_target_img.get_width() // TARGET_SCALE
target_height = original_target_img.get_height() // TARGET_SCALE
target_img = pygame.transform.scale(original_target_img, (target_width, target_height))

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = random.choice(TARGET_SPEEDS)
target_speed_y = random.choice(TARGET_SPEEDS)

score = 0
font = pygame.font.Font(None, 36)
start_time = time.time()

def move_target():
    global target_x, target_y, target_speed_x, target_speed_y

    target_x += target_speed_x
    target_y += target_speed_y

    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

def draw_score_and_time():
    score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    remaining_time = max(GAME_DURATION - (time.time() - start_time), 0)
    time_text = font.render(f"Время: {remaining_time:.1f}", True, (255, 255, 255))
    screen.blit(time_text, (SCREEN_WIDTH - 150, 10))

def handle_mouse_click(event):
    global score, target_x, target_y, target_speed_x, target_speed_y

    mouse_x, mouse_y = event.pos
    if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
        score += 1
        if hit_sound:
            hit_sound.play()
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        target_speed_x = random.choice(TARGET_SPEEDS)
        target_speed_y = random.choice(TARGET_SPEEDS)

def show_final_screen():
    screen.fill((0, 0, 0))
    final_score_text = font.render(f"Игра окончена! Ваш счет: {score}", True, (255, 255, 255))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
    pygame.display.update()

def main():
    global score, start_time

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(event)

        move_target()
        screen.blit(target_img, (target_x, target_y))
        draw_score_and_time()
        pygame.display.update()

        if time.time() - start_time >= GAME_DURATION:
            running = False

        clock.tick(60)

    show_final_screen()
    pygame.mixer.music.stop()
    pygame.time.wait(3000)


if __name__ == "__main__":
    main()
    pygame.quit()
