import sys
import pygame
from pygame.locals import *



def main():
	pygame.init()
				
	(w,h) = (800,800)
	(x,y) = (w/2,h/2)
	
	pygame.display.set_mode((w,h),0,32)
	screen = pygame.display.get_surface()
	img = pygame.image.load("image.png")
	img_rect = img.get_rect()
	img_rect.center=(300,200)
	
	font = pygame.font.Font(None,55)

	
	while(1):
		screen.fill((50,50,50))

		screen.blit(img,img_rect)
		pygame.display.update()
		
		for event in pygame.event.get():
			if event.type== QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
if __name__ == "__main__":
	main()