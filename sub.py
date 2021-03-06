import pygame 
import random 
import os

WIDTH = 1080
HEIGHT = 720
FPS = 60 

#Color
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0) 
GREEN = (0,255,0)
BLUE = (0,0,255)

#Set up assets folders

class Player(pygame.sprite.Sprite):
	#sprite for the Player
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50,50))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT/2)

	def update(self):
		self.rect.x += 5 
		if self.rect.left > WIDTH:
			self.rect.right = 0


# Initialize pygame window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#Game loop
running = True
while running:

	#Keep loop runs at same FPS
	clock.tick(FPS)

	#Process input (event)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#Update 
	all_sprites.update()

	#Draw/ render
	screen.fill(BLACK)
	all_sprites.draw(screen)

	#After drawing everything
	pygame.display.flip() 


pygame.quit()