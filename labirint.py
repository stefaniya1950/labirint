# Разработай свою игру в этом файле!
from pygame import *
WIDTH = 700
HEIGHT = 500
BLUE = (155, 213, 248)
BLACK = (0,0,0)
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption ("лабиринт")
window.fill(BLUE)

class Gamesprite(sprite.Sprite):
    def __init__(self,picture ,w,h,x,y):
        super().__init__()
        self.image = image.load(picture)
        self.image = transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset (self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Bullet (Gamesprite):
    def __init__(self,picture,w,h,x,y,x_speed): 
        super().__init__(picture,w,h,x,y)
        self.speed_x= x_speed
    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x > WIDTH + 10:
            self.kill()
   
    


        


class Player (Gamesprite):
    def __init__(self,picture ,w,h,x,y,x_speed,y_speed):
        super().__init__(picture ,w,h,x,y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def  update(self):
        if self.rect.right > WIDTH :
            self.rect.x -= 3
        elif self.rect.x < 0:
            self.rect.x +=3
        if self.rect.  bottom > HEIGHT:
            self.rect.y-=3
        elif self.rect.y < 0:
            self.rect.y +=3
        self.rect.x +=self.x_speed
        platforms_touched = sprite.spritecollide(self,barriers,False)
        if  self.x_speed > 0:
            for i in platforms_touched:
                self.rect.right = min(self.rect.right,i.rect.left)
        elif self.x_speed < 0:
            for i in platforms_touched:
                self.rect.left = max(self.rect.left,i.rect.right)
        self.rect.y +=self.y_speed
        platforms_touched = sprite.spritecollide(self,barriers,False)
        if self.y_speed > 0 :
            for i in platforms_touched:
                self.rect.bottom = min(self.rect.bottom,i.rect.top)
        if self.y_speed < 0:
            for i in platforms_touched:
                self.rect.top = max(self.rect.top,i.rect.bottom)
    def fire(self):
        bullet = Bullet('weapon.png',15,20, self.rect.right, self.rect.centery, 15)
        bullets.add (bullet)

        

class Enemy(Gamesprite):
    def __init__(self,picture ,w,h,x,y):
        super().__init__(picture ,w,h,x,y)
        self.speed = 2
        self.direction = "down"
    def update (self) :
        
        if self.rect.y <= 0:
            self.direction = "down"
        if self.rect.y >= 320:
            self.direction = "up"
        if self.direction == "down": 
            self.rect.y += self.speed
        else :
            self.rect.y -= self.speed





cherry = Gamesprite('cherry.png',80,80,600,400)
wall_1  = Gamesprite('platform_h.png', 180,80,100,100)
wall_2  = Gamesprite('platform_v.png',200,80,400,300)
wall_3  =Gamesprite("platform_v.png",30,500,400,150)
barriers = sprite.Group()
bullets = sprite.Group()
barriers.add (wall_1)
barriers.add (wall_2)
barriers.add (wall_3)
player = Player("pacman.png",80,80,100,400,0,0)
enemy = Enemy("enemy.png",80,80,600,0)
enemies = sprite.Group() 
enemies.add(enemy)
win = Gamesprite("win.jpg",WIDTH,HEIGHT,0,0)
game_over = Gamesprite("game-over.png",WIDTH,HEIGHT,0,0)
finish = False


run = True
while run:
    time.delay(50)
    for i in event.get():
        if i.type == QUIT:
            run = False
        elif i.type == KEYDOWN:
            if i.key==K_DOWN:
                player.y_speed = 3
            if i.key ==K_UP:
                player.y_speed = -3
            if i.key ==K_LEFT:
                player.x_speed = -3
            if i.key == K_RIGHT:
                player.x_speed = 3
            if i.key == K_SPACE:
                player.fire()
        elif i.type  == KEYUP:
            if i.key==K_DOWN:
                player.y_speed = 0
            if i.key ==K_UP:
                player.y_speed = 0
            if i.key ==K_LEFT:
                player.x_speed = 0
            if i.key == K_RIGHT:
                player.x_speed = 0
            
        




    if finish  == False:

        window.fill(BLUE)
        barriers.draw(window)
        player.update()
        player.reset()
        sprite.groupcollide(enemies,bullets,True,True)
        sprite.groupcollide(barriers,bullets,False,True)
        enemies.update()
        enemies.draw(window)
        cherry.reset()
        bullets.update()
        bullets.draw(window)
        if sprite.collide_rect(player,cherry):
            finish = True
            win.reset()
        if sprite.spritecollide(player,enemies,False):
            finish = True
            window.fill(BLACK)
            game_over.reset()
           
    display.update()
    


