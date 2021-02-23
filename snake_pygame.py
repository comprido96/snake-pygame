import sys
import pygame
from pygame import locals as l
import random as r
from collections import deque
import itertools


pygame.init()
size = width, height = 900, 900
black = (0,0,0) #RGB
white = (255,255,255)
red = (255,0,0)
offset = 20 # length of a single snake cell
score = 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SCORE: {}'.format(score))
font = pygame.font.SysFont('bold',42)
movements = {'UP':[0,-offset],'DOWN':[0,offset],'RIGHT':[offset,0],'LEFT':[-offset,0]}
direction = 'RIGHT' # initial direction (arbitrarily chosen)
TIME_WAIT = 1500 # millisecs
FPS = 10 # game speed
clock = pygame.time.Clock()


# create initial food
food = [20*30,20*r.randint(0,44)]
food_rect = pygame.Rect(food[0],food[1],offset,offset)
# draw food
pygame.draw.rect(screen,red,food_rect)

# create snake
snake = deque()
head = [20*6,20*22]
snake.append(head)
snake.append([head[0]-offset,head[1]])
snake.append([head[0]-2*offset,head[1]])
done = False

# draw snake head
head_rect = pygame.Rect(snake[0][0],snake[0][1],offset,offset)
pygame.draw.rect(screen,white,head_rect)
pygame.display.update()
while not done:

	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				direction = 'UP'
			
			if event.key == pygame.K_DOWN:
				direction = 'DOWN'
	
			if event.key == pygame.K_RIGHT:
				direction = 'RIGHT'
	
			if event.key == pygame.K_LEFT:
				direction = 'LEFT'
			
	movement = movements[direction]
	new_head = [snake[0][0]+movement[0],snake[0][1]+movement[1]]
	snake.insert(0,new_head)
	head_rect = pygame.Rect(new_head[0],new_head[1],offset,offset)
	tail = snake.pop()
	tail_rect = pygame.Rect(tail[0],tail[1],offset,offset)
	pygame.draw.rect(screen,black,tail_rect)

	snake_length = len(snake)
	if snake_length>1 and new_head in list(itertools.islice(snake,1,snake_length)):
		screen.fill(black)
		text = font.render('Game over! Closing game...',1,white)
		text_rect = text.get_rect()
		text_rect.center = width//2, height//2
		screen.blit(text,text_rect)
		pygame.display.update()
		pygame.time.wait(TIME_WAIT)
		done = True	

	if (direction=='UP' and head_rect.bottom == 0) or (direction=='DOWN' and head_rect.top==height) or (direction=='RIGHT' and head_rect.left==width) or (direction=='LEFT' and head_rect.right==0):
		screen.fill(black)
		text = font.render('Game over! Closing game...',1,white)
		text_rect = text.get_rect()
		text_rect.center = width//2, height//2
		screen.blit(text,text_rect)
		pygame.display.update()
		pygame.time.wait(TIME_WAIT)
		done = True		
	
	if head_rect.x == food_rect.x and head_rect.y == food_rect.y:
		score += 1
		pygame.display.set_caption('SCORE: {}'.format(score))
		food = [20*r.randint(0,44),20*r.randint(0,44)]
		while food in snake:
			food = [20*r.randint(0,44),20*r.randint(0,44)]
		pygame.draw.rect(screen,white,tail_rect)
		snake.append(tail)
	food_rect = pygame.Rect(food[0],food[1],offset,offset)

	pygame.draw.rect(screen,red,food_rect)
	pygame.draw.rect(screen,white,head_rect)
	pygame.display.update()
	clock.tick(FPS)

		