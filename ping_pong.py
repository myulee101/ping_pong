from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))






#игровая сцена
win_color = (254, 239, 239) #цвет фона
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(win_color)

clock = time.Clock()
fps = 60
game = True

ball = GameSprite('ping_pong_image.png', 200, 200, 4, 50, 50)
#игровой цикл

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.reset()
    display.update()
    clock.tick(fps)        
