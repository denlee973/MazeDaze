import pygame, sys
from pygame.locals import *

#initialize pygame
pygame.init()

#Set Screen Dimensions
WIDTH = 1000
HEIGHT= 800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Maze Daze 2.0')

#Define Colour Values
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0, 0, 255)
LBLUE = (158,221,255)
LLBLUE = (235,245,255)
PINK = (245, 54, 188)
WHITE = (255,255,255)
BLACK = (0,0,0)
BGREY = (78,117,130)
LGREY = (240,240,240)

#fonts
tfont = pygame.font.SysFont("Century Gothic",80,False,False)
stfont = pygame.font.SysFont("Century Gothic",70,False,False)
ssfont = pygame.font.SysFont("Century Gothic",50,False,False)
pfont = pygame.font.SysFont("//Library//Fonts//Microsoft//MS Gothic.ttf",20,False,False)
#initializing things
background = pygame.image.load("maxresdefault.jpg")
pressed = False
mpos = (0,0)

#buttons()
#@param: word:str,font,x:int,y:int,w:int,h:int,c1:int(),c2:int()
#@return: pressed:bool
def buttons(word,font,x,y,w,h,c1,c2,mpos):
	pressed = pygame.mouse.get_pressed()
	push = False
	pygame.draw.rect(screen,c1,(x,y,w,h),0)
	if mpos[0]>=x and mpos[0]<=x+w and mpos[1]>=y and mpos[1]<=y+h:
		pygame.draw.rect(screen,c2,(x,y,w,h),0)
		if pressed[0] == 1:
			push = True
	word = font.render(word,True,BLACK)
	if font == stfont:
		screen.blit(word,(x+20,y+15))
	elif font == ssfont:
		screen.blit(word,(x+10,y+5))
	return push

# instructions()
# @param: none
# @return: none
def instructions():
	screen.fill(LLBLUE)
	line1 = pfont.render("Welcome to Maze Daze 2.0!")
	screen.blit(line1,(300,300))
	buttons("PLAY",ssfont,250,650,200,80,LBLUE,LLBLUE,mpos)
	buttons("TITLE",ssfont,550,650,200,80,LBLUE,LLBLUE,mpos)
	

#title()
#@param: none
#@return: none
def title(mpos):
	screen.blit(background,[0,0])
	play = buttons("START",stfont,400,470,200,80,LBLUE,LLBLUE,mpos)
	instruc = buttons("INSTRUCTIONS",stfont,300,640,400,80,LBLUE,LLBLUE,mpos)
	#updating
	pygame.display.update()	
	if play == True:
		pass #play game
	if instruc == True:
		pass #print instructions




inPlay = True
print "Hit ESC to end the program."
x = 0
y = 0
d = 0
spdx = 0
spdy = 0

while inPlay:
	
    #deals with any keyboard options once program is run
    #looks for the event (action of using keyboard)
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			print "PRESSED"
			pressed = True
		if event.type == pygame.MOUSEMOTION:
			mpos = pygame.mouse.get_pos()
			print "Mouse position:",mpos
		if event.type == pygame.MOUSEBUTTONUP:
			print "RELEASED"
			pressed = False
    #looks for escape to be pressed
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE:
				inPlay = False  
    # get_pressed() method generates a True/False list for the status of all keys
	keys = pygame.key.get_pressed()    
	if keys[pygame.K_LEFT]:
		x -= spdx
	if keys[pygame.K_RIGHT]:
		x += spdx
	if keys[pygame.K_UP]:
		y -= spdy
	if keys[pygame.K_DOWN]:
		y += spdy
	if x<=0:
		x = 0
	if (x+d)>=(WIDTH+1):
		x = WIDTH
	if y<=0:
		y = 0
	if (y+d)>=(HEIGHT+1):
		y = HEIGHT

	title(mpos)                     # the screen window must be constantly redrawn - animation
	pygame.time.delay(2)                # pause for 2 miliseconds
#---------------------------------------#                                        
pygame.quit()                           # always quit pygame when done!
