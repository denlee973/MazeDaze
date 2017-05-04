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
BLUE = (0, 0, 255)
DBLUE = (28,74,175)
LBLUE = (158,221,255)
LLBLUE = (235,245,255)
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
x = 30
y = 770
d = 20
spdx = 3
spdy = 3

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

# vline()
# @param: x:int,y:int,l:int,colour:int()
# @return: none
def vline(x,y,l,colour):
	pygame.draw.rect(screen,colour,(x,y,2,l),0)
		
# hline()
# @param:x:int,y:int,l:int,colour:int()
# @return:none
def hline(x,y,l,colour):
	pygame.draw.rect(screen,colour,(x,y,l,2),0)

# level_1()
# @param: none
# @return: borders:int[]
def level_1():
	screen.fill(LLBLUE)
	pygame.draw.rect(screen,DBLUE,(0,0,WIDTH,HEIGHT),7)
	#left to right, top to bottom
	vline(944,0,201,DBLUE)
	vline(944,335,67,DBLUE)
	vline(881,67,268,DBLUE)
	vline(881,402,67,DBLUE)
	vline(818,134,268,DBLUE)
	vline(755,67,67,DBLUE)
	vline(755,202,268,DBLUE)
	vline(692,134,134,DBLUE)
	vline(692,335,134,DBLUE)
	vline(629,0,67,DBLUE)
	vline(629,268,268,DBLUE)
	#right to left, top to bottom
	hline(567,66,63,DBLUE)
	hline(567,201,63,DBLUE)
	hline(567,401,63,DBLUE)
	hline(630,133,189,DBLUE)
	hline(630,267,63,DBLUE)
	hline(693,66,63,DBLUE)
	hline(693,334,63,DBLUE)
	hline(756,468,63,DBLUE)
	hline(819,66,63,DBLUE)
	hline(819,401,126,DBLUE)
	hline(882,267,126,DBLUE)
	#updating
	pygame.display.update()

# start()
# @param: none
# @return: none
def start():
	level_1()
	pass

# instructions()
# @param: none
# @return: none
def instructions():
	screen.fill(LLBLUE)
	line1 = pfont.render("Welcome to Maze Daze 2.0!",True,BLACK)
	screen.blit(line1,(300,300))
	buttons("PLAY",ssfont,250,650,200,80,LBLUE,LLBLUE,mpos)
	buttons("TITLE",ssfont,550,650,200,80,LBLUE,LLBLUE,mpos)
	#updating
	pygame.display.update()

#title()
#@param: none
#@return: none
def title(mpos):
	screen.blit(background,[0,0])
	pygame.draw.rect(screen,WHITE,(0,300,1000,100),0)
	title = tfont.render("MAZE DAZE 2.0",True,BLACK)
	screen.blit(title,(400,310))
	play = buttons("START",stfont,400,470,200,80,LBLUE,LLBLUE,mpos)
	instruc = buttons("INSTRUCTIONS",stfont,300,640,400,80,LBLUE,LLBLUE,mpos)
	#updating
	pygame.display.update()
	#button pressed
	if play == True:
		start()
	if instruc == True:
		instructions()




inPlay = True
print "Hit ESC to end the program."


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
