import pygame 
import test


pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spritesheet")

'''
#frame = 4
sprite_sheet_image = pygame.image.load
	(
	'/home/lenovo/Desktop/Python/test/herochar_idle_anim_strip_4.png'
	).convert_alpha()
sprite_sheet = test.SpriteSheet(sprite_sheet_image)
'''

#frame = 6
hero_run_image = pygame.image.load(
	'/home/lenovo/Desktop/Python/sprites/platform_metroidvania asset pack v1.01/herochar sprites(new)/herochar_run_anim_strip_6.png'
	).convert_alpha()
hero_run = test.SpriteSheet(hero_run_image)

'''
#frame = 3
hero_jump_image = pygame.image.load(
	'/home/lenovo/Desktop/Python/sprites/platform_metroidvania asset pack v1.01/herochar sprites(new)/herochar_jump_up_anim_strip_3.png'
	).convert_alpha()
hero_jump = test.SpriteSheet(hero_jump_image)
'''

'''
#frame = 3
hero_double_jump_image = pygame.image.load(
	'/home/lenovo/Desktop/Python/sprites/platform_metroidvania asset pack v1.01/herochar sprites(new)/herochar_jump_double_anim_strip_3.png'
	).convert_alpha()
hero_double_jump = test.SpriteSheet(hero_double_jump_image)
'''

'''
#frame = 3
hero_jump_down_image = pygame.image.load(
	'/home/lenovo/Desktop/Python/sprites/platform_metroidvania asset pack v1.01/herochar sprites(new)/herochar_jump_down_anim_strip_3.png'
	).convert_alpha()
hero_jump_down = test.SpriteSheet(hero_jump_down_image)
'''

'''
#frame = 3
hero_get_hit_image = pygame.image.load(
	'/home/lenovo/Desktop/Python/sprites/platform_metroidvania asset pack v1.01/herochar sprites(new)/herochar_hit_anim_strip_3.png'
	).convert_alpha()
hero_get_hit_down = test.SpriteSheet(hero_get_hit_image)
'''


BG = (50,50,50)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (150,150,150)

#create animation list
animation_list = []
animation_steps = 6
last_update = pygame.time.get_ticks()
animation_cd = 150
frame = 0

for x in range(animation_steps):
	animation_list.append(
		#sprite_sheet.get_image(x, 16, 16, 5, BLACK))
		hero_run.get_image(x, 16, 16, 5, BLACK))


run = True
while run:
	screen.fill(GREY)
	###
	current_time = pygame.time.get_ticks()
	if current_time - last_update >= animation_cd:
		frame += 1
		last_update = current_time
		if frame >= len(animation_list):
			frame = 0


	#Show frame image
	for x in range(animation_steps):
		#screen.blit(animation_list[frame],(200,200))
		screen.blit(animation_list[frame],(200,200))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()
	
pygame.quit()