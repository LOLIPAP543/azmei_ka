import pygame
import random

# Инициализация pygame
pygame.init()

# Определение цветов
BLACK = (0, 255, 0) #зМЕЯ
WHITE = (92, 145, 74)
RED = (0, 219, 38)
GREEN = (184, 35, 72) #СЧЁТ

# Определение размеров окна и блока
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
BLOCK_SIZE = 20

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Змейка")

img = pygame.transform.scale(pygame.image.load('back_ground.jpg'), (WINDOW_WIDTH, WINDOW_HEIGHT))


clock = pygame.time.Clock()

# Определение функции для отображения счета
def display_score(score):
    font = pygame.font.Font(None, 27)
    text = font.render("Счет: " + str(score), True, GREEN)
    window.blit(text, [10, 10])

# Определение функции для отрисовки змейки
def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(window, BLACK, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Определение функции для обновления змейки
def update_snake(snake, direction):
    new_head = [snake[0][0], snake[0][1]]

    if direction == "left":
        new_head[0] -= BLOCK_SIZE
    elif direction == "right":
        new_head[0] += BLOCK_SIZE
    elif direction == "up":
        new_head[1] -= BLOCK_SIZE
    elif direction == "down":
        new_head[1] += BLOCK_SIZE

    snake.insert(0, new_head)
    return snake

# Определение функции для обновления позиции еды
def update_food():
    food_x = random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    return food_x, food_y

# Определение функции для обработки столкновений
def check_collision(snake):
    if snake[0][0] < 0 or snake[0][0] >= WINDOW_WIDTH or snake[0][1] < 0 or snake[0][1] >= WINDOW_HEIGHT:
        return True
    
    if snake[0] in snake[1:]:
        return True

    return False

# Инициализация змейки и еды
snake = [[200, 200]]
direction = "right"
food_x, food_y = update_food()

score = 0

# Основной игровой цикл
game_over = False
while not game_over:
    # Отрисовка игрового окна
    window.blit(img, (0, 0))
    pygame.draw.rect(window, WHITE, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
    draw_snake(snake)
    display_score(score)
    pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"

    # Обновление позиции змейки
    snake = update_snake(snake, direction)

    # Проверка столкновений
    if check_collision(snake):
        game_over = True

    # Проверка на съедение еды
    if snake[0][0] == food_x and snake[0][1] == food_y:
        score += 1
        food_x, food_y = update_food()
    else:
        snake.pop()

    # Ограничение количества обновления кадров в секунду
    clock.tick(7)

# Завершение pygame
pygame.quit()