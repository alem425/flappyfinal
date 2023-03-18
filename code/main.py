from sys import exit
import pygame
import random


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Flappy Coins")
clock = pygame.time.Clock()
game_active = True

#Timer Surface init
counter, text = 15, '15'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.Font('text/PressStart2P-Regular.ttf', 15)

#Sky and Ground Surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert_alpha()

#"Score" Text surface
test_font = pygame.font.Font('text/PressStart2P-Regular.ttf',35)
score_surf = test_font.render('Score',False, (64,64,64))
score_rect = score_surf.get_rect(center = (380,50))

#Gold Coin
gold_coin = pygame.image.load('graphics/coins/coin_gold.png').convert_alpha()
gold_coin_rect = gold_coin.get_rect(topleft = (600,200))

#Bird
bird_up = pygame.image.load('graphics/bird/up.png').convert_alpha()
bird_up = pygame.transform.scale(bird_up,(50,32.5))
bird_rec = bird_up.get_rect(topleft= (80, 200))
bird_up_ypos = 200

#Game Over screen
bird_static = pygame.image.load('graphics/bird/up.png').convert_alpha()
bird_static_scaled = pygame.transform.scale(bird_static,(150, 100))
bird_static_rect = bird_static_scaled.get_rect(center =(400,200))

gameO_text = pygame.font.Font('text/PressStart2P-Regular.ttf',35)
gameO_text_surf = gameO_text.render('GAME OVER', False, ('#7303fc'))
gameO_text_rect = gameO_text_surf.get_rect(center = (380,50))

restart =  pygame.font.Font('text/PressStart2P-Regular.ttf',15)
restart_surf = restart.render('Press Space Bar to continue', False, ('#7303fc'))
restart_rect = restart_surf.get_rect(center = (380, 120))

#Sounds
jump_sound = pygame.mixer.Sound('sound/jumpland.wav')
music = pygame.mixer.Sound('sound/chills.wav')
jump_sound.set_volume(1)
pygame.mixer.music.load('sound/chills.wav')
pygame.mixer.music.play(-1)



score_counter =0
bird_gravity = 0
score_counter = 0
GRAVVAL = .5
JUMPVAL = -10

pygame.mixer.music.play(-1)

while True:
   scoreVal_surf = test_font.render(f'Score: {score_counter}', False, (64,64,64))
   scoreVal_rect = scoreVal_surf.get_rect(center = (600,50))

#Conditionals for WheneVer a button is pressed
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()
      if game_active:
         if event.type == pygame.MOUSEBUTTONDOWN:
            bird_gravity = JUMPVAL
            jump_sound.play()
               
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               bird_gravity = JUMPVAL
               jump_sound.play()
         
         if event.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > -1 else 'Times Up' 

            if text == 'Times Up':
               print(text)
               game_active = False
      else:
         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
            counter, text = 15, '15'.rjust(3)
            bird_rec.y = 200
            score_counter =0
            gold_coin_rect.x = 800

     
   if game_active:
      #creates the sky, ground, player, coin, and score
      screen.blit(sky_surface, (0,0))
      screen.blit(ground_surface,(0,320))
      screen.blit(font.render(text, False, (0,0,0)), (32, 48))
      screen.blit(scoreVal_surf,scoreVal_rect)

      gold_coin_rect.x -=4
      if (gold_coin_rect.x <= -100):
         gold_coin_rect.x = 800 
         gold_coin_rect.y = random.randint(20,310)
      screen.blit(gold_coin,(gold_coin_rect))

      #Player 
      bird_gravity += GRAVVAL
      bird_rec.y += bird_gravity
      if bird_rec.bottom >= 321:
         bird_rec.bottom = 321
      if bird_rec.top <= 0:
         bird_rec.top = 0
      screen.blit(bird_up, bird_rec)

      #Collision
      if gold_coin_rect.colliderect(bird_rec): 
            score_counter += 1 
      screen.blit(scoreVal_surf,scoreVal_rect)
   #Game oVer screen
   else:
      game_oVer()
      


   #draw all our elements and it will be continously updating
   pygame.display.update()
   clock.tick(60)

   def game_oVer():
      screen.fill((94,129,162))
      screen.blit(bird_static_scaled,bird_static_rect)
      screen.blit(gameO_text_surf,gameO_text_rect)
      screen.blit(restart_surf,restart_rect)
      screen.blit(scoreVal_surf,(100,300))