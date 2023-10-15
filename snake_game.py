import sys

import pygame
from random import randrange

RES = 600
SIZE = 30


def close_game():
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()


def main():
    x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    length = 1
    snake = [(x, y)]
    dx, dy = 0, 0
    fps = 60
    dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
    score = 0
    speed_count, snake_speed = 0, 15

    pygame.init()
    pygame.display.set_caption('Snake Game')
    surface = pygame.display.set_mode([RES, RES])
    clock = pygame.time.Clock()
    font_score = pygame.font.SysFont('arial', 26, bold=True)
    font_end1 = pygame.font.SysFont('arial', 66, bold=True)
    font_end2 = pygame.font.SysFont('arial', 35, bold=True)
    img = pygame.image.load('background.jpg').convert()

    while True:
        surface.blit(img, (0, 0))
        # drawing snake, apple
        [pygame.draw.rect(surface, pygame.Color('purple'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
        pygame.draw.rect(surface, pygame.Color('white'), (*apple, SIZE, SIZE))
        # show score
        render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('white'))
        surface.blit(render_score, (7, 8))
        # snake movement
        speed_count += 1
        if not speed_count % snake_speed:
            x += dx * SIZE
            y += dy * SIZE
            snake.append((x, y))
            snake = snake[-length:]
        # eating food
        if snake[-1] == apple:
            apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
            length += 1
            score += 1
            snake_speed -= 1
            snake_speed = max(snake_speed, 3)
        # game over
        if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
            while True:
                render_end1 = font_end1.render('GAME OVER', 1, pygame.Color('white'))
                render_end2 = font_end2.render('PRESS [ENTER]', 1, pygame.Color('white'))
                # Calculate the center position for the text
                center_x = RES // 2
                center_y = RES // 2
                # Calculate the text positions
                text1_x = center_x - render_end1.get_width() // 2
                text1_y = center_y - render_end1.get_height() // 2
                text2_x = center_x - render_end2.get_width() // 2
                text2_y = text1_y + render_end1.get_height()

                surface.blit(render_end1, (text1_x, text1_y))
                surface.blit(render_end2, (text2_x, text2_y))
                pygame.display.flip()
                close_game()
                key = pygame.key.get_pressed()
                if key[pygame.K_RETURN]:
                    main()

        pygame.display.flip()
        clock.tick(fps)
        close_game()
        # controls
        key = pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP]:
            if dirs['W']:
                dx, dy = 0, -1
                dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
        elif key[pygame.K_s] or key[pygame.K_DOWN]:
            if dirs['S']:
                dx, dy = 0, 1
                dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
        elif key[pygame.K_a] or key[pygame.K_LEFT]:
            if dirs['A']:
                dx, dy = -1, 0
                dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            if dirs['D']:
                dx, dy = 1, 0
                dirs = {'W': True, 'S': True, 'A': False, 'D': True, }


if __name__ == "__main__":
    main()
