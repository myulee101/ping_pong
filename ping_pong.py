from pygame import *
#игровая сцена
win_color = (254, 239, 239) #цвет фона
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(win_color)

clock = time.Clock()
fps = 60
game = True

#игровой цикл

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(fps)        