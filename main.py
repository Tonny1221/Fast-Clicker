import pygame
from random import randint
import time

class Area():
    def __init__(self, x , y , width , height , color = (255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def new_color(self, color):
        self.fill_color = color
    
    def new_rect(self):
        pygame.draw.rect(scene, self.fill_color, self.rect)

    def color_frame(self, frame_color , thick_rect):
        pygame.draw.rect(scene, frame_color, self.rect, thick_rect)
    
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Lable(Area):
    def set_text(self, text, fsize=12, text_color = (0 , 0 , 0)):
        self.image = pygame.font.SysFont('V', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.new_rect()
        scene.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
t_timer = 0
tim_mer = 0
difficulty = int(input('Выберите сложность:\n 1 - Лёгкий \n 2 - Средний \n 3 - Сложный'))
if difficulty == 1:
    tim_mer = 45
    t_timer = 15
elif difficulty == 2:
    tim_mer = 25
    t_timer = 11
elif difficulty == 3:
    tim_mer = 19
    t_timer = 11
    
    
    

color_fill = (108, 80, 166)
pygame.init()
scene = pygame.display.set_mode((500, 500))
scene.fill(color_fill)
FPS = pygame.time.Clock()

start_time = time.time()
cur_time = start_time

points = 0
times = 0

c_time = Lable(10,10, 50,30, (108, 80, 166))
c_time.set_text('Время:', 46)
c_time.draw(5,5)
c_time1 = Lable(10,50, 50,30, (108, 80, 166))
c_time1.set_text(times,30)
c_time1.draw(35,5)

c_points = Lable(400,10, 50,30, (108, 80, 166))
c_points.set_text('Счёт:', 46)
c_points.draw(5,5)
c_points1 = Lable(400,50, 50,30, (108, 80, 166))
c_points1.set_text(points, 30)
c_points1.draw(35,5)

cards = list()
num_cards = 4
cord_x = 35
for i in range(num_cards):
    card1 = Lable(cord_x, 150, 80,130, (255, 255, 0))
    card1.set_text('CLICK',28)
    card1.color_frame((12, 196, 240), 15)
    cards.append(card1)
    cord_x += 120

green = (0, 255, 0)
red = (255,0,0)

wait = 0


while True:
    new_time = time.time()
    if new_time - cur_time >= 1:
        c_time1.set_text(str(int(new_time-start_time)), 40)
        c_time1.draw(35,5)
        cur_time = new_time

    if new_time - start_time >= t_timer:
        loss = Lable(0,0,500,500, (255,0 ,0))
        loss.set_text('Время вышло!!!',60)
        loss.draw(110,180)
        break

    if points >= 5:
        win = Lable(0,0,500,500,(0,255,0))
        win.set_text('Ты выйграл!!!',60)
        win.draw(110,180)
        result_time = Lable(90,230,250,250, (0, 255, 0))
        result_time.set_text(
            'Время прохождения ' + str(int(new_time - start_time)) + ' сек' , 40
            )  
        result_time.draw(0,0)
        break

    if wait == 0:   
        click = randint(1,4)   
        for card in range(num_cards):  
            cards[card].new_color((255,255,0))

            if card+1 == click:
                cards[card].draw(12,60)
            else:
                cards[card].new_rect()
        wait = tim_mer
    else:
        wait -= 1

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x,y):
                    if i + 1 == click:
                        cards[i].new_color(green)
                        points += 1
                    else:
                        cards[i].new_color(red)
                        points -= 1
                    cards[i].new_rect()
                    c_points1.set_text(points, 32)
                    c_points1.draw(35,5)

                    
                


    FPS.tick(40)
    pygame.display.update()
pygame.display.update()
