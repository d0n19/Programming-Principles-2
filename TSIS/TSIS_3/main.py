import pygame
import sys
import random
import time
import json
import os

pygame.init()

WIDTH, HEIGHT = 400, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Pro: TSIS 3 Edition")
FPS = 60
CLOCK = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
GRAY = (50, 50, 50)
GOLD = (255, 215, 0)

FONT_SM = pygame.font.SysFont("Verdana", 15)
FONT_MD = pygame.font.SysFont("Verdana", 25)
FONT_LG = pygame.font.SysFont("Verdana", 40)

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"

def load_settings():
    default_settings = {"sound": True, "car_color": RED, "difficulty": "Medium"}
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as f:
                content = f.read().strip()
                if not content:
                    return default_settings
                return json.loads(content)
        except (json.JSONDecodeError, IOError):
            return default_settings
    return default_settings

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def save_score(username, score):
    data = []
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, "r") as f:
                data = json.load(f)
        except:
            data = []
    
    data.append({"name": username, "score": score, "date": time.strftime("%Y-%m-%d")})
    data = sorted(data, key=lambda x: x['score'], reverse=True)[:10]
    
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), -50)
        self.speed = random.randint(3, 6)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if (self.rect.top > HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH-40), -50)
            return True
        return False

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), -50)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > HEIGHT:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)
        self.speed = 7

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(self.speed, 0)

class Game:
    def __init__(self):
        self.settings = load_settings()
        self.state = "MENU"
        self.score = 0
        self.coins_collected = 0
        self.username = "Player 1"
        
        self.player = Player(self.settings.get("car_color", BLUE))
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.INC_SPEED = pygame.USEREVENT + 1
        pygame.time.set_timer(self.INC_SPEED, 1000)

    def reset_game(self):
        self.score = 0
        self.coins_collected = 0
        self.player = Player(self.settings.get("car_color", BLUE))
        self.enemies.empty()
        self.coins.empty()
        self.all_sprites.empty()
        self.all_sprites.add(self.player)
        self.enemies.add(Enemy())
        for e in self.enemies: self.all_sprites.add(e)

    def draw_text(self, text, font, color, x, y):
        img = font.render(text, True, color)
        SCREEN.blit(img, (x, y))

    def menu_screen(self):
        SCREEN.fill(GRAY)
        self.draw_text("RACER PRO", FONT_LG, WHITE, 80, 100)
        
        play_rect = pygame.draw.rect(SCREEN, GREEN, (100, 250, 200, 50))
        set_rect = pygame.draw.rect(SCREEN, BLUE, (100, 320, 200, 50))
        
        self.draw_text("ИГРАТЬ", FONT_MD, WHITE, 155, 260)
        self.draw_text("НАСТРОЙКИ", FONT_MD, WHITE, 130, 330)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    self.reset_game()
                    self.state = "PLAYING"
                if set_rect.collidepoint(event.pos):
                    self.state = "SETTINGS"

    def game_over_screen(self):
        SCREEN.fill(RED)
        self.draw_text("GAME OVER", FONT_LG, WHITE, 80, 200)
        self.draw_text(f"Счёт: {self.score}", FONT_MD, WHITE, 140, 300)
        self.draw_text(f"Монеты: {self.coins_collected}", FONT_MD, WHITE, 120, 350)
        self.draw_text("Нажми 'M' для меню", FONT_SM, WHITE, 110, 500)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                save_score(self.username, self.score)
                self.state = "MENU"

    def settings_screen(self):
        SCREEN.fill(WHITE)
        self.draw_text("НАСТРОЙКИ", FONT_LG, BLACK, 80, 50)
        self.draw_text(f"Сложность: {self.settings['difficulty']}", FONT_MD, BLACK, 50, 200)
        self.draw_text("Нажми 'D' для изменения", FONT_SM, GRAY, 50, 240)
        self.draw_text("Нажми 'B' для выхода", FONT_MD, RED, 50, 450)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b: self.state = "MENU"
                if event.key == pygame.K_d:
                    modes = ["Easy", "Medium", "Hard"]
                    cur = modes.index(self.settings['difficulty'])
                    self.settings['difficulty'] = modes[(cur + 1) % 3]
                    save_settings(self.settings)

    def play_game(self):
        SCREEN.fill(GRAY)
        pygame.draw.line(SCREEN, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)
        
        for entity in self.all_sprites:
            SCREEN.blit(entity.image, entity.rect)
            if hasattr(entity, 'move'):
                if isinstance(entity, Enemy):
                    if entity.move():
                        self.score += 1
                else:
                    entity.move()

        if random.randint(1, 100) < 3:
            new_coin = Coin()
            self.coins.add(new_coin)
            self.all_sprites.add(new_coin)

        for coin in self.coins:
            coin.move()
            if pygame.sprite.collide_rect(self.player, coin):
                self.coins_collected += 1
                self.score += 5
                coin.kill()

        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.state = "GAME_OVER"

        self.draw_text(f"Score: {self.score}", FONT_SM, BLACK, 10, 10)
        self.draw_text(f"Coins: {self.coins_collected}", FONT_SM, BLACK, 10, 30)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == self.INC_SPEED:
                for enemy in self.enemies:
                    enemy.speed += 0.1

    def main_loop(self):
        while True:
            if self.state == "MENU":
                self.menu_screen()
            elif self.state == "SETTINGS":
                self.settings_screen()
            elif self.state == "PLAYING":
                self.play_game()
            elif self.state == "GAME_OVER":
                self.game_over_screen()
            
            CLOCK.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.main_loop()