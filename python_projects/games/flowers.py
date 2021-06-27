import os
import random
import game_config as gc 
from pygame import image,transform

flowers_count=dict((a,0) for a in gc.ASSET_FILES)

def available_flowers():
	return [a for a,c in flowers_count.items() if c<2]

class Flower:
	def __init__(self,index):
		self.index=index
		self.row-index//gc.NUM_TILES_SIDE

		self.col=index%gc.NUM_TILES_SIDE
		self.name=random.choice(available_flowers())
		flowers_count[self.name]+=1
		self.image_path=os.path.join(gc.ASSET_DIR,self.name)
		self.image=image.load(self.image_path)
		self.image=transform.scale(self.image_path,(gc.IMAZE_SIZE-2*gc.MARGIN,GC.IMAZE_SIZE-2*gc.MARGIN))
		self.box=self.image.copy()
		self.box.fill((200,200,200))
		self.skip=False
		