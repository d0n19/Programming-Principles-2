import pygame
import sys
import random
import time
import json
import os

WIDTH, HEIGHT = 600, 500
BLOCK_SIZE = 20
INITIAL_FPS = 10

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
GRAY = (50, 50, 50)

def load_settings():
    default = {
        "color": [0, 255, 0], 
        "grid": True, 
        "sound": True, 
        "personal_best": 0
    }
    if os.path.exists("settings.json"):
        try:
            if os.path.getsize("settings.json") == 0:
                return default
            with open("settings.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, Exception):
            return default
    return default

def save_settings(data):
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

class Snake:
    def __init__(self, color):
        self.body = [[100, 100], [80, 100], [60, 100]]
        self.direction = "RIGHT"
        self.color = color
        self.shield = False

    def move(self):
        head = list(self.body[0])
        if self.direction == "UP": head[1] -= BLOCK_SIZE
        elif self.direction == "DOWN": head[1] += BLOCK_SIZE
        elif self.direction == "LEFT": head[0] -= BLOCK_SIZE
        elif self.direction == "RIGHT": head[0] += BLOCK_SIZE
        self.body.insert(0, head)
        return self.body.pop()

class GameObject:
    def __init__(self, color, weight=1):
        self.color = color
        self.weight = weight
        self.pos = [0, 0]
        self.spawn_time = 0
        self.lifetime = 8000 

    def randomize(self, obstacles, snake_body):
        while True:
            self.pos = [random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                        random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]
            if self.pos not in obstacles and self.pos not in snake_body:
                break
        self.spawn_time = pygame.time.get_ticks()

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Pro: No DB Edition")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.large_font = pygame.font.SysFont("Verdana", 40)
        
        self.settings = load_settings()
        self.personal_best = self.settings.get("personal_best", 0)
        self.state = "MENU"
        self.username = "Игрок"
        self.reset_game()

    def reset_game(self):
        self.snake = Snake(tuple(self.settings["color"]))
        self.food = GameObject(GREEN, 1)
        self.poison = GameObject(DARK_RED, -2)
        self.powerup = None
        self.obstacles = []
        self.score = 0
        self.level = 1
        self.speed = INITIAL_FPS
        self.active_powerup = None
        self.powerup_end = 0
        self.generate_food()

    def generate_food(self):
        self.food.randomize(self.obstacles, self.snake.body)
        self.poison.randomize(self.obstacles, self.snake.body)

    def generate_obstacles(self):
        self.obstacles = []
        if self.level >= 3:
            for _ in range(self.level * 2):
                while True:
                    wall = [random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                            random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]
                    if wall not in self.snake.body and wall != self.food.pos:
                        self.obstacles.append(wall)
                        break

    def check_record(self):
        if self.score > self.personal_best:
            self.personal_best = self.score
            self.settings["personal_best"] = self.personal_best
            save_settings(self.settings)

    def draw_text(self, text, x, y, color=WHITE, center=False, large=False):
        f = self.large_font if large else self.font
        surf = f.render(str(text), True, color)
        rect = surf.get_rect(center=(x, y)) if center else surf.get_rect(topleft=(x, y))
        self.screen.blit(surf, rect)

    def handle_menu(self):
        self.screen.fill(BLACK)
        self.draw_text("SNAKE PRO", WIDTH//2, 80, GREEN, True, True)
        self.draw_text(f"Имя: {self.username}_", WIDTH//2, 180, WHITE, True)
        self.draw_text("ENTER - Начать", WIDTH//2, 260, WHITE, True)
        self.draw_text("[S] Настройки", WIDTH//2, 320, GRAY, True)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.reset_game()
                    self.state = "PLAYING"
                elif event.key == pygame.K_BACKSPACE: self.username = self.username[:-1]
                elif event.key == pygame.K_s: self.state = "SETTINGS"
                else:
                    if len(self.username) < 12 and event.unicode.isalnum():
                        self.username += event.unicode

    def handle_playing(self):
        now = pygame.time.get_ticks()
        
        if not self.powerup and random.random() < 0.01:
            ptype = random.choice(["SPEED", "SLOW", "SHIELD"])
            color = CYAN if ptype == "SPEED" else PURPLE if ptype == "SLOW" else YELLOW
            self.powerup = GameObject(color)
            self.powerup.type = ptype
            self.powerup.randomize(self.obstacles, self.snake.body)
        
        if self.powerup and now - self.powerup.spawn_time > self.powerup.lifetime:
            self.powerup = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != "DOWN": self.snake.direction = "UP"
                elif event.key == pygame.K_DOWN and self.snake.direction != "UP": self.snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT": self.snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT": self.snake.direction = "RIGHT"

        self.snake.move()
        head = self.snake.body[0]

        if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or 
            head in self.snake.body[1:] or head in self.obstacles):
            if self.snake.shield:
                self.snake.shield = False
                self.active_powerup = None
            else:
                self.check_record()
                self.state = "GAME_OVER"
                return

        if head == self.food.pos:
            self.score += 1
            self.snake.body.append(list(self.snake.body[-1]))
            if self.score % 5 == 0:
                self.level += 1
                self.speed += 2
                self.generate_obstacles()
            self.generate_food()
        
        elif head == self.poison.pos:
            if len(self.snake.body) > 2:
                self.snake.body.pop(); self.snake.body.pop()
                self.generate_food()
            else:
                self.check_record()
                self.state = "GAME_OVER"

        if self.powerup and head == self.powerup.pos:
            self.active_powerup = self.powerup.type
            self.powerup_end = now + 5000
            if self.active_powerup == "SHIELD": self.snake.shield = True
            self.powerup = None

        if self.active_powerup and now > self.powerup_end:
            self.active_powerup = None

        self.screen.fill(BLACK)
        if self.settings["grid"]:
            for x in range(0, WIDTH, BLOCK_SIZE): pygame.draw.line(self.screen, GRAY, (x, 0), (x, HEIGHT))
            for y in range(0, HEIGHT, BLOCK_SIZE): pygame.draw.line(self.screen, GRAY, (0, y), (WIDTH, y))

        for b in self.snake.body: pygame.draw.rect(self.screen, self.snake.color, [b[0], b[1], BLOCK_SIZE-1, BLOCK_SIZE-1])
        for o in self.obstacles: pygame.draw.rect(self.screen, WHITE, [o[0], o[1], BLOCK_SIZE, BLOCK_SIZE])
        pygame.draw.rect(self.screen, self.food.color, [self.food.pos[0], self.food.pos[1], BLOCK_SIZE, BLOCK_SIZE])
        pygame.draw.rect(self.screen, self.poison.color, [self.poison.pos[0], self.poison.pos[1], BLOCK_SIZE, BLOCK_SIZE])
        if self.powerup: pygame.draw.circle(self.screen, self.powerup.color, (self.powerup.pos[0]+10, self.powerup.pos[1]+10), 8)

        self.draw_text(f"Счёт: {self.score}  Уровень: {self.level}  Рекорд: {self.personal_best}", 10, 10)
        pygame.display.flip()

    def run(self):
        while True:
            if self.state == "MENU":
                self.handle_menu()
            elif self.state == "PLAYING":
                self.handle_playing()
            elif self.state == "GAME_OVER":
                self.screen.fill(RED)
                self.draw_text("GAME OVER", WIDTH//2, 150, WHITE, True, True)
                self.draw_text(f"Счёт: {self.score} | Рекорд: {self.personal_best}", WIDTH//2, 230, WHITE, True)
                self.draw_text("R - Заново  M - Меню", WIDTH//2, 320, WHITE, True)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r: self.reset_game(); self.state = "PLAYING"
                        if event.key == pygame.K_m: self.state = "MENU"
            
            elif self.state == "SETTINGS":
                self.screen.fill(BLACK)
                self.draw_text("НАСТРОЙКИ", WIDTH//2, 50, CYAN, True)
                self.draw_text(f"[G] Сетка: {'ВКЛ' if self.settings['grid'] else 'ВЫКЛ'}", WIDTH//2, 150, WHITE, True)
                self.draw_text("[B] Назад", WIDTH//2, 300, GRAY, True)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_g: self.settings["grid"] = not self.settings["grid"]
                        if event.key == pygame.K_b: 
                            save_settings(self.settings)
                            self.state = "MENU"

            curr_fps = self.speed
            if self.active_powerup == "SPEED": curr_fps *= 1.5
            elif self.active_powerup == "SLOW": curr_fps *= 0.6
            self.clock.tick(curr_fps)

if __name__ == "__main__":
    SnakeGame().run()