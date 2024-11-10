#Создай собственный Шутер!
from pygame import *
import pygame
import random
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.play()
miss = 0
def game ():
    global miss
    Windows = pygame.display.set_mode((700,500))

    #pygame.display.set_caption('Гонка')

    FPS = pygame.time.Clock()
        
    fon = pygame.image.load("galaxy.jpg")
    fon = pygame.transform.scale(fon,(700,500))
    class gameObjekt(pygame.sprite.Sprite):
        def __init__(self, image, visota, shirina, x,y, speed):
            super().__init__()
            self.img_sprite = pygame.image.load(image)
            self.img_sprite = pygame.transform.scale(self.img_sprite,(visota,shirina))
            self.rect = self.img_sprite.get_rect()
            self.rect.x = x
            self.rect.y = y 
            self.speed = speed
            self.move = ''
        def show(self):
            Windows.blit(self.img_sprite, self.rect)

    class  gamePlaer(gameObjekt): 
        def ypravlenie(self):
            keys = pygame.key.get_pressed()
            
                
            if keys[pygame.K_d]  and self.rect.x < 650:
                self.rect.x += self.speed
            if keys[pygame.K_a]  and self.rect.x > 0 :
                self.rect.x -= self.speed
        def vistril(self):
            fire = Fire("bullet.png", 15, 20, self.rect.x, self.rect.y, 10)   
            fires.add(fire) 
        
    class Enemy(gameObjekt):
        def forward(self):
            global miss
            self.rect.y += 2
            if self.rect.y > 400:
                miss += 1
                self.rect.y = -20
                self.rect.x = random.randint(50, 650)
            
                                            
                    

    miss = 0


    class Fire (gameObjekt):
        def update(self):
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.kill()
        
            
            
    score = 0
    miss = 0

    player = gamePlaer('rocket.png',60,60, 20, 420,3)

    money = gameObjekt('bullet.png',60,60, 400, 90, 0)
    
    fires = sprite.Group()

    run = True
    monstrers = pygame.sprite.Group()
    for i in range(5):
        monstrer = Enemy('ufo.png', 60, 60, random.randint(80, 1120), -100, 1)  
        monstrers.add(monstrer)      
    while run:
        Windows.blit(fon,(0,0))   
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            elif i.type == KEYDOWN:
                if i.key == K_SPACE:
                    player.vistril()
        kill = pygame.sprite.groupcollide(fires, monstrers , True, True)
        for i in kill:
            score += 1
            monstrer = Enemy('ufo.png', 60, 60, random.randint(80, 1120), -100, 1)  
            monstrers.add(monstrer)   

        result = f'Вы уничтожили:{str(score)}'
        bed = font.Font(None, 35).render(result, True, (255,255, 250))

        Windows.blit(bed,(50,250))

        result1 = f'Лохов прошло в тыл:{str(miss)}'
        bed1 = font.Font(None, 35).render(result1, True, (255,255, 250))

        Windows.blit(bed1,(50,10))
        
        player.show()
        player.ypravlenie()
        for i in fires:
            i.show()
            i.update()
        
        if miss > 10:
            run = False


        for i in monstrers:
            i.show()
            i.forward()
            if player.rect.colliderect(i.rect):
                run = False

        pygame.display.update()
        FPS.tick(100)
