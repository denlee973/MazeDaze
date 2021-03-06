import pygame, sys
from pygame.locals import *
import random

#initialize pygame
pygame.init()

#Set Screen Dimensions
WIDTH = 1000
HEIGHT= 800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Maze Daze 2.0')

#Define Colour Values
DBLUE = (28,74,175)
LBLUE = (158,221,255)
LLBLUE = (235,245,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
BGREY = (78,117,130)
LGREY = (240,240,240)

#music
pygame.mixer.music.load("soundtrack.mp3")
pygame.mixer.music.play(-1,0.0)

#fonts
tfont = pygame.font.SysFont("Century Gothic",80,False,False)	#doesn't actually use century gothic
stfont = pygame.font.SysFont("Century Gothic",70,False,False)
ssfont = pygame.font.SysFont("Century Gothic",50,False,False)
pfont = pygame.font.SysFont("//Library//Fonts//Microsoft//MS Gothic.ttf",30,False,False)

#initializing things
#load images
background = pygame.image.load("title_background.jpg")
spiral = pygame.image.load("spiral.png")
arrow = pygame.image.load("arrow.png")
flag = pygame.image.load("finish_flag.png")
fullstar = pygame.image.load("fullstar.png")
emptystar = pygame.image.load("emptystar.png")
cursor = pygame.image.load("pointer.png")
#keeps track of which dizzy spinners you have passed
#so you don't spin multiple times on one spinner
spin = [False,False,False,False]
pressed = False
#mouse position
mpos = (0,0)

#circle dimensions
x = 30
y = 770
d = 20
spdx = 1
spdy = 1


#buttons()
#@param: word:str,font,x:int,y:int,w:int,h:int,c1:int(),c2:int(),mpos:int()
#@return: push:bool
def buttons(word,font,x,y,w,h,c1,c2,mpos):
	#gets mouse press
	pressed = pygame.mouse.get_pressed()
	push = False
	#draw button
	pygame.draw.rect(screen,c1,(x,y,w,h),0)
	pygame.draw.circle(screen,c1,(x,y),10,0)
	pygame.draw.circle(screen,c1,(x+w,y),10,0)
	pygame.draw.circle(screen,c1,(x,y+h),10,0)
	pygame.draw.circle(screen,c1,(x+w,y+h),10,0)
	pygame.draw.rect(screen,c1,(x,y-10,w,10),0)
	pygame.draw.rect(screen,c1,(x-10,y,10,h),0)
	pygame.draw.rect(screen,c1,(x,y+h,w,10),0)
	pygame.draw.rect(screen,c1,(x+w,y,10,h),0)
	#lights up button when rolled over
	if mpos[0]>=x and mpos[0]<=x+w and mpos[1]>=y and mpos[1]<=y+h:
		pygame.draw.rect(screen,c2,(x,y,w,h),0)
		#if button is pushed
		if pressed[0] == 1:
			push = True
	#print word on top
	word = font.render(word,True,BLACK)
	if font == stfont:
		screen.blit(word,(x+20,y+15))
	elif font == ssfont:
		screen.blit(word,(x+10,y+5))
	return push


# move()
# @param: vertical:int[], horizontal:int[], directions:str, form:int
# @return: window:int,form:int
def move(vertical,horizontal,directions,form):
	global x
	global y

	#screen boundaries
	if x-d-2<0:
		x = d+2
	elif x+d+2>WIDTH:
		x = WIDTH-d-2
	if y-d-2<0:
		y = d+2
	elif y+d+2>HEIGHT:
		y = HEIGHT-d-2

	#boundaries moving right
	if directions == "R":
		#for vertical lines,
		for v in range(len(vertical)):
			#if the right side of the circle is 'touching' a line
			if x+d == vertical[v][0] or x+d == vertical[v][0]+1:
				#if there is a line in that y range
				if y-d<= vertical[v][1]+vertical[v][2] and y-d >= vertical[v][1]:
					x = vertical[v][0]-d
				elif y+d >= vertical[v][1] and y+d <= vertical[v][1]+vertical[v][2]-1:
					x = vertical[v][0]-d
		#for horizontal lines,
		for h in range(len(horizontal)):
			#if it hits a horizontal line's short side
			if x+d == horizontal[h][0] or x+d == horizontal[h][0]+1:
				if y-d <= horizontal[h][1] and y+d >= horizontal[h][1]:
					x = horizontal[h][0]-d
	
	#boundaries moving left
	if directions == "L":
		for v in range(len(vertical)):
			if  x-d == vertical[v][0] or x-d == vertical[v][0]-1:
				if y-d<= vertical[v][1]+vertical[v][2] and y-d >= vertical[v][1]:
					x = vertical[v][0]+d
				elif y+d >= vertical[v][1] and y+d <= vertical[v][1]+vertical[v][2]:				
					x = vertical[v][0]+d
		for h in range(len(horizontal)):
			if x-d == horizontal[h][0]+horizontal[h][2] or x-d == horizontal[h][0]+horizontal[h][2]-1:
				if y-d <= horizontal[h][1] and y+d >= horizontal[h][1]:
					x = horizontal[h][0]+horizontal[h][2]+d

	#boundaries moving down
	if directions == "D":
		for h in range(len(horizontal)):
			if y+d == horizontal[h][1] or y+d == horizontal[h][1]+1:
				if x+d >= horizontal[h][0] and x+d <= horizontal[h][0]+horizontal[h][2]:
					y = horizontal[h][1]-d
				elif x-d >= horizontal[h][0]+horizontal[h][2] and x-d <= horizontal[h][0]:
					y = horizontal[h][1]-d
		for v in range(len(vertical)):
			if y+d == vertical[v][1] or y+d == vertical[v][1]+1:
				if x-d <= vertical[v][0] and x+d >= vertical[v][0]:
					y = vertical[v][1]-d

	#boundaries moving up
	if directions == "U":
		for h in range(len(horizontal)):
			if y-d == horizontal[h][1] or y-d == horizontal[h][1]-1 or y-d == horizontal[h][1]+1:
				if x+d >= horizontal[h][0] and x+d <= horizontal[h][0]+horizontal[h][2]:
					y = horizontal[h][1]+d+2
				elif x-d >= horizontal[h][0]+horizontal[h][2] and x-d <= horizontal[h][0]:
					y = horizontal[h][1]+d+2
		for v in range(len(vertical)):
			if y-d == vertical[v][1]+vertical[v][2] or y-d == vertical[v][1]+vertical[v][2]-1:
				if x-d <= vertical[v][0] and x+d >= vertical[v][0]:
					y = vertical[v][1]+vertical[v][2]+d
	
	pygame.draw.circle(screen,BLACK,(x,y),d,0)
	pygame.draw.circle(screen,BGREY,(x,y),d-5,0)

	window = 1
	#if you get to the finish then run endscreen
	if x>=969 and y<=30:
		window = 3
	#if you have yet to go through the first spinner
	if spin[0] == False:
		#if you go through the spinner
		if x>=255 and x<=315 and y>=205 and y<=265:
			#random rotation value
			form = random.randint(1,4)
			spin[0] = True
	if spin[1] == False:
		if x>=505 and x<=566 and y>=469 and y<=535:
			form = random.randint(1,4)
			spin[1] = True
	if spin[2] == False:
		if x>=640 and x<=670 and y>=220 and y<=250:
			form = random.randint(1,4)
			spin[2] = True
	if spin[3] == False:
		if x>=882 and x<=945 and y>=335 and y<=400:
			form = random.randint(1,4)
			spin[3] = True

	return window,form


# fin_screen()
# @param: mpos:int(),score:int
# @return: play:bool,menu:bool
def fin_screen(mpos,score):
	print "CONGRATULATIONS!"
	screen.fill(WHITE)
	pygame.draw.rect(screen,WHITE,(0,200,1000,100),0)
	title = tfont.render("FINISH!",True,BLACK)
	screen.blit(title,(410,225))
	
	#scoring: based on number of times you press they key down
	if score <= 60:
		screen.blit(fullstar,[150,300])
		screen.blit(fullstar,[400,300])
		screen.blit(fullstar,[650,300])
	elif score > 60 and score < 100:
		screen.blit(fullstar,[150,300])
		screen.blit(fullstar,[400,300])
		screen.blit(emptystar,[650,300])
	elif score >= 100 and score <=150:
		screen.blit(fullstar,[150,300])
		screen.blit(emptystar,[400,300])
		screen.blit(emptystar,[650,300])
	else:
		screen.blit(emptystar,[150,300])
		screen.blit(emptystar,[400,300])
		screen.blit(emptystar,[650,300])

	#buttons
	play = buttons("PLAY AGAIN",ssfont,250,570,230,50,LBLUE,LLBLUE,mpos)
	menu = buttons("MENU",ssfont,600,570,115,50,LBLUE,LLBLUE,mpos)
	return play, menu
	
# vline()
# @param: x:int,y:int,l:int,colour:int()
# @return: none
def vline(x,y,l,colour):
	#draw a vertical line (rectangle) with width 2
	pygame.draw.rect(screen,colour,(x,y,2,l),0)

		
# hline()
# @param:x:int,y:int,l:int,colour:int()
# @return:none
def hline(x,y,l,colour):
	#horizontal line with height 2
	pygame.draw.rect(screen,colour,(x,y,l,2),0)

# level_1()
# @param: none
# @return: vertical:int[],horizontal:int[]
def level_1():
	screen.fill(LLBLUE)
	pygame.draw.rect(screen,DBLUE,(0,0,WIDTH,HEIGHT),7)

	#print finish lag
	screen.blit(flag,[947,15])
	#print dizzy spinners
	screen.blit(spiral,[260,210])
	screen.blit(spiral,[515,485])
	screen.blit(spiral,[640,220])
	screen.blit(spiral,[890,350])

	#line coordinates
	#right to left, top to bottom
	vertical = [[944,0,201],[944,335,67],[944,603,201],[881,67,286],[881,402,134],[818,134,268],[818,469,134],[755,67,67],[755,202,268],[755,536,268],[692,134,134],[692,335,67],[692,469,201],[629,0,67],[629,268,268],[629,670,67],[566,67,201],[566,335,67],[566,536,67],[566,737,67],[503,67,67],[503,469,67],[503,603,201],[440,134,201],[440,670,67],[377,67,67],[377,335,134],[377,536,67],[377,737,67],[314,134,67],[314,469,201],[251,0,134],[251,402,134],[251,603,134],[188,0,67],[188,134,67],[188,268,134],[188,536,268],[125,67,67],[125,201,67],[125,536,67],[125,670,67],[62,134,67],[62,268,67],[62,469,201]]
	#left to right, top to bottom	
	horizontal = [[0,267,63],[0,468,189],[63,66,63],[63,200,63],[63,334,63],[63,401,252],[63,669,63],[63,736,63],[126,133,63],[126,267,315],[126,535,126],[189,200,189],[252,133,63],[252,334,126],[252,669,189],[315,66,63],[315,468,252],[315,736,63],[378,133,63],[378,401,126],[378,535,126],[378,602,126],[441,66,63],[441,200,63],[441,334,126],[504,133,63],[504,267,63],[504,669,189],[567,66,63],[567,201,63],[567,401,63],[567,535,63],[567,602,63],[630,133,189],[630,267,63],[693,66,63],[693,334,63],[693,736,63],[756,468,63],[756,669,126],[819,66,63],[819,401,126],[819,602,126],[819,736,126],[882,267,126],[882,536,63],[945,468,63],[945,669,63]]

	#right to left, top to bottom
	for i in range(len(vertical)):
		vline(vertical[i][0],vertical[i][1],vertical[i][2],DBLUE)

	for k in range(len(horizontal)):
		hline(horizontal[k][0],horizontal[k][1],horizontal[k][2],DBLUE)

	return vertical,horizontal



# instructions()
# @param: rules:bool,controls:bool,mpos:int()
# @return: play:bool,menu:bool,page:bool
def instructions(rules,controls,mpos):
	screen.fill(LLBLUE)
	#rules screen
	if rules == True:
		#printing multiple lines of text
		text = ["It's a race to the end of the maze!","Along the way, you'll have to deal with some", "dizzy spinners. Try to get there","by pressing as little buttons as possible.","Which way is up?"]
		tbblit = []
		#render loop
		for t in range(5):
			line = ssfont.render(text[t],True,BLACK)
			tbblit.append(line)
		#blit loop
		for l in range(len(tbblit)):
			screen.blit(tbblit[l],(130,290+(l*50+15)))
		buttons("RULES",stfont,130,200,200,70,LLBLUE,LLBLUE,mpos)
		page = buttons("CONTROLS",stfont,500,200,320,70,LBLUE,LLBLUE,mpos)
	#controls screen
	if controls == True:
		#images
		pygame.draw.circle(screen,BLACK,(520,475),d,0)
		pygame.draw.circle(screen,BGREY,(520,475),d-5,0)
		screen.blit(arrow,[380,450])
		screen.blit(flag,[500,525])
		screen.blit(arrow,[380,525])
		screen.blit(spiral,[500,600])
		screen.blit(arrow,[380,600])
		
		#rendering multiple lines
		labels = ["You","Finish","Dizzy Spinner"]
		nlabels = []
		for i in range (len(labels)):
			label = ssfont.render(labels[i],True,BLACK)
			nlabels.append(label)
		screen.blit(nlabels[0],(300,450))
		screen.blit(nlabels[1],(250,525))
		screen.blit(nlabels[2],(130,600))
		word1 = stfont.render("Control your circle with your",True,BLACK)
		word2 = stfont.render("arrow keys.",True,BLACK)
		screen.blit(word1,(130,290))
		screen.blit(word2,(130,290+85))
		page = buttons("RULES",stfont,130,200,200,70,LBLUE,LLBLUE,mpos)
		buttons("CONTROLS",stfont,500,200,320,70,LLBLUE,LLBLUE,mpos)
		

	play = buttons("PLAY",stfont,760,650,160,70,LBLUE,LLBLUE,mpos)

	menu = buttons("MENU",stfont,750,540,180,70,LBLUE,LLBLUE,mpos)
	return play, menu,page

#title()
#@param: mpos:int()
#@return: play:bool,instruc:bool,end:bool
def title(mpos):
	screen.blit(background,[0,0])
	pygame.draw.rect(screen,WHITE,(0,300,1000,100),0)
	title = tfont.render("MAZE DAZE 2.0",True,BLACK)
	screen.blit(title,(300,325))
	play = buttons("START",stfont,410,500,200,70,LBLUE,LLBLUE,mpos)
	instruc = buttons("INSTRUCTIONS",stfont,300,650,420,70,LBLUE,LLBLUE,mpos)
	end = buttons("QUIT",ssfont,880,740,105,45,LBLUE,LLBLUE,mpos)

	#button pressed
	return play,instruc,end

# main()
# @param: none
# @return: none
def main():
	print "Hit ESC to end the program."
	inPlay = True
	window = 0
	mpos = (0,0)
	directions = "R"
	form = 1
	score = 0
	global x
	global y

	while inPlay == True:
		#window0 --> title screen
		if window==0:
			play,instruc,end = title(mpos)             # the screen window must be constantly redrawn - animation
			
			#start game
			if play == True:
				x = 30
				y = 770
				form = 1
				score = 0
				window = 1
				vertical,horiontal = level_1()
				continue
			#show instructions
			if instruc == True:
				window = 2
				rules = True
				controls = False
				play,menu,page = instructions(rules,controls,mpos)
				continue
			#quit button
			if end == True:
				inPlay = False
				break
		#window1 --> game
		if window == 1:
			vertical,horizontal = level_1()
			window,form = move(vertical,horizontal,directions,form)
		#window2 --> instructions-rules
		if window == 2:
			rules = True
			controls = False
			play,menu,page = instructions(rules,controls,mpos)
			if page == True:
				window = 4
			if play == True:
				x = 30
				y = 770
				form = 1
				score = 0
				window = 1

			elif menu == True:
				window = 0
		#window4 --> instructions-controls
		if window == 4:
			rules = False
			controls = True
			play,menu,page = instructions(rules,controls,mpos)
			if page == True:
				window = 2
			if play == True:
				x = 30
				y = 770
				form = 1
				score = 0
				window = 1

			elif menu == True:
				window = 0

		#window3 --> end screen
		if window == 3:
			play,menu = fin_screen(mpos,score)
			if play == True:
				x = 30
				y = 770
				form = 1
				score = 0
				window = 1

			elif menu == True:
				window = 0

				
				


	    #deals with any keyboard options once program is run
	    #looks for the event (action of using keyboard)
		mpos = pygame.mouse.get_pos()
		if window == 0 or window == 2 or window == 3:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					pressed = True
				if event.type == pygame.MOUSEBUTTONUP:
					pressed = False
		    #looks for escape to be pressed
				if event.type == pygame.KEYDOWN:
					if event.key==pygame.K_ESCAPE:
						inPlay = False  
	    # get_pressed() method generates a True/False list for the status of all keys
		elif window == 1:

			directions = ""
			keys = pygame.key.get_pressed()
			#no direction rotation    
			if form == 1:
				if keys[pygame.K_LEFT] or keys[pygame.K_w]:
					directions =  "L"
					x -= spdx
				elif keys[pygame.K_RIGHT]:
					directions =  "R"
					x += spdx
				elif keys[pygame.K_UP]:
					directions = "U"
					y -= spdy
				elif keys[pygame.K_DOWN]:
					directions = "D"
					y += spdy

			#1 direction rotation to the left
			elif form == 2:
				if keys[pygame.K_LEFT]:
					directions =  "U"
					y -= spdx
				elif keys[pygame.K_RIGHT]:
					directions =  "D"
					y += spdx
				elif keys[pygame.K_UP]:
					directions = "R"
					x += spdy
				elif keys[pygame.K_DOWN]:
					directions = "L"
					x -= spdy

			#2 direction rotations
			elif form == 3:
				if keys[pygame.K_LEFT]:
					directions =  "R"
					x += spdx
				elif keys[pygame.K_RIGHT]:
					directions =  "L"
					x -= spdx
				elif keys[pygame.K_UP]:
					directions = "D"
					y += spdy
				elif keys[pygame.K_DOWN]:
					directions = "U"
					y -= spdy
		
			#3 direction rotations to the left
			elif form == 4:
				if keys[pygame.K_LEFT]:
					directions =  "D"
					y += spdx
				elif keys[pygame.K_RIGHT]:
					directions =  "U"
					y -= spdx
				elif keys[pygame.K_UP]:
					directions = "L"
					x -= spdy
				elif keys[pygame.K_DOWN]:
					directions = "R"
					x += spdy

			#score counter
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					score +=1
					print "Score =",score
			
			#escape quit
			if keys[pygame.K_ESCAPE]:
				inPlay = False

		#fancy cursor
		screen.blit(cursor,[mpos[0]-10,mpos[1]])
		#updating
		pygame.display.update()
		pygame.event.pump()
		pygame.time.delay(1)                # pause for 2 miliseconds

main()
#---------------------------------------#                                        
pygame.quit()                           # always quit pygame when done!
quit()
