import pygame
import game_config as gc 
from pygame import display, event, image
from flowers import Flower
from time import sleep

def find_index(x,y):
	row=y//gc.IMAGE_SIZE
	col=x//gc.IMAGE_SIZE
	index=row*gc.NUM_TILES_SIDE +col
	return index

pygame.init()
display.set_caption('My 1st game')
screen=display.set_mode((512,512))
matched=image.load('asserts/matched.png')
gameover=image.load('asserts/gameover.png')


running=True
tiles=[Flower(i) for i in range(0,gc.NUM_TILES_TOT)]
current_img=[]
while running:
	current_events=event.get()
	for e in current_events:
		if e.type==pygame.QUIT:
			running=False
		if e.type ==pygame.KEYDOWN:
			if e.key ==pygame.K_ESCAPE:
				running=False
		if e.type ==pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			index=find_index(mouse_x,mouse_y)
			if index not in current_img:
				current_img.append(index)

			if len(current_img) >2:
				current_img=current_img[1:]
	screen.fill((225,225,225))
	total_skipped=0
	for _, tile in enumerate(tiles):
		image_i = tile.image if tile.index in current_img else tile.box
		if not tile.skip:
			screen.blit(image_i,(tile.col*gc.IMAGE_SIZE+gc.MARGIN,tile.row*gc.IMAGE_SIZE+gc.MARGIN))

		else:
			total_skipped+=1
	display.flip()

	if len(current_img)==2:
		idx1,idx2=current_img
		if tiles[idx1].name==tiles[idx2].name:
			tiles[idx1].skip=True
			tiles[idx2].skip=True
			sleep(0.4)
			screen.blit(matched,(0,0))
			display.flip()
			sleep(0.4)

			current_img=[]
	if total_skipped==16:
		screen.blit(gameover,(0,0))
		display.flip()
		running=False
print('Thankyou and play again')

