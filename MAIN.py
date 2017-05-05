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
	vertical = [[944,0,201],[944,335,67],[881,67,286],[881,402,67],[818,134,268],[755,67,67],[755,202,268],[692,134,134,],[692,335,134],[629,0,67],[629,268,268]]
	horizontal = [[567,66,63],[567,201,63],[567,401,63],[630,133,189],[630,267,63],[693,66,63],[693,334,63],[756,468,63],[819,66,63],[819,401,126],[882,267,126]]
	#left to right, top to bottom
	for i in range(11):
		vline(vertical[i][0],vertical[i][1],vertical[i][2],DBLUE)
	#right to left, top to bottom
	for k in range(11):
		hline(horizontal[k][0],horizontal[k][1],horizontal[k][2],DBLUE)



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
	play = buttons("START",stfont,400,470,200,80,LBLUE,LLBLUE,mpos)
	instruc = buttons("INSTRUCTIONS",stfont,300,640,400,80,LBLUE,LLBLUE,mpos)
	#updating
	pygame.display.update()
	#button pressed
	return play,instruc




window = 0
inPlay = True
def main():
	print "Hit ESC to end the program."
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
	vertical = [[944,0,201],[944,335,67],[881,67,286],[881,402,67],[818,134,268],[755,67,67],[755,202,268],[692,134,134,],[692,335,134],[629,0,67],[629,268,268]]
	horizontal = [[567,66,63],[567,201,63],[567,401,63],[630,133,189],[630,267,63],[693,66,63],[693,334,63],[756,468,63],[819,66,63],[819,401,126],[882,267,126]]
	#left to right, top to bottom
	for i in range(11):
		vline(vertical[i][0],vertical[i][1],vertical[i][2],DBLUE)
	#right to left, top to bottom
	for k in range(11):
		hline(horizontal[k][0],horizontal[k][1],horizontal[k][2],DBLUE)



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
	play = buttons("START",stfont,400,470,200,80,LBLUE,LLBLUE,mpos)
	instruc = buttons("INSTRUCTIONS",stfont,300,640,400,80,LBLUE,LLBLUE,mpos)
	#button pressed
	return play,instruc





def main():
	print "Hit ESC to end the program."
	inPlay = True
	window = 0
	global x
	global y

	while inPlay == True:
	    #deals with any keyboard options once program is run
	    #looks for the event (action of using keyboard)
		mpos = pygame.mouse.get_pos()
		if window == 0 or window == 2:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					print "PRESSED"
					pressed = True
				if event.type == pygame.MOUSEMOTION:
					print "Mouse position:",mpos
				if event.type == pygame.MOUSEBUTTONUP:
					print "RELEASED"
					pressed = False
		    #looks for escape to be pressed
				if event.type == pygame.KEYDOWN:
					if event.key==pygame.K_ESCAPE:
						inPlay = False  
	    # get_pressed() method generates a True/False list for the status of all keys
		elif window == 1:
			keys = pygame.key.get_pressed()    
			if keys[pygame.K_LEFT]:
				print "L"
				x -= spdx
			if keys[pygame.K_RIGHT]:
				print "R"
				x += spdx
			if keys[pygame.K_UP]:
				print "U"
				y -= spdy
			if keys[pygame.K_DOWN]:
				print "D"
				y += spdy
			if x<=0:
				x = 0
			if (x+d)>=(WIDTH+1):
				x = WIDTH
			if y<=0:
				y = 0
			if (y+d)>=(HEIGHT+1):
				y = HEIGHT
			if keys[pygame.K_ESCAPE]:
				inPlay = False
			print x
			print y


		if window==0:
			play,instruc = title(mpos)                     # the screen window must be constantly redrawn - animation
			if play==True:
				window=1
				level_1()
			if instruc == True:
				window = 2
				instructions()
		if window==1:
			level_1()

		if window == 2:
			instructions()
		#updating
		pygame.display.update()
		pygame.event.pump()
		pygame.time.delay(2)                # pause for 2 miliseconds

main()
#---------------------------------------#                                        
pygame.quit()                           # always quit pygame when done!
quit()
