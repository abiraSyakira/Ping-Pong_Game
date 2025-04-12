from pygame import *
init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        
class Player(GameSprite):
    def update1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 600
win_height = 500
back = (20, 255, 255)
window = display.set_mode((win_width,win_height))
window.fill(back)
display.set_caption('Ping-Pong')

font.init()
main_font = font.Font(None, 35)
small_font = font.Font(None, 28)

game = True
finish = False
FPS = 60
clock = time.Clock()

racket1 = Player("papanping-pong.png", 30, 200, 25, 65, 15)
racket2 = Player("papanping-pong.png", 520, 200, 25, 65, 15)
ball = GameSprite("bolaping-pong.png", 200, 200, 30, 30, 10)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speedx = 3
speedy = 3

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
        
    if finish != True:
        window.fill(back)
        racket1.update1()
        racket2.update()
        ball.rect.x += speedx
        ball.rect.y += speedy

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speedx *= -1
            speedy *= 1
        #if the ball reaches screen edges, change its movement direction
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speedy *= -1
        #if ball flies behind this paddle, display loss condition for player 1
        if ball.rect.x < 0 :
            finish = True
            window.blit(lose1, (200,200))
            game_over = True
        #if ball flies behind this paddle, display loss condition for player 2
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))
            game_over = True
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)