from display import *
from draw import *
from parser import *
from matrix import *
import math, threading

color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

def make_script(x):
	s = '''#BODY
	push
	rotate
	y -30
	move
	350 250 0
	box
	-100 125 50 200 250 100
	#HEAD
	push
	rotate
	y %s
	move
	0 175 0
	sphere
	0 0 0 50
	pop
	#LEFT ARM
	push
	move
	-100 125 0
	rotate
	x %s
	box
	-40 0 40 40 100 80
	#LEFT LOWER ARM
	push
	move
	-20 -100 0
	box
	-10 0 10 20 125 20
	pop
	pop
	#RIGHT ARM
	push
	move
	100 125 0
	rotate
	x %s
	box
	0 0 40 40 100 80
	#RIGHT LOWER ARM
	push
	move
	20 -100 0
	box
	-10 0 10 20 125 20
	pop
	pop
	#LEFT LEG
	push
	move
	-100 -125 0
	box
	0 0 40 50 120 80
	pop
	#RIGHT LEG
	push
	move
	100 -125 0
	box
	-50 0 40 50 120 80
	save
	robot%s.png''' %(x,-1*x if x < 90 else -90,-1*x if x < 90 else -90,x/10)
	f = open('script', 'w')
	f.write(s)
	f.close()

def make_script_2(x):
	s = '''#BODY
	push
	rotate
	y -30
	move
	350 250 0
	box
	-100 125 50 200 250 100
	#HEAD
	push
	rotate
	y %s
	move
	0 175 0
	sphere
	0 0 0 50
	pop
	#LEFT ARM
	push
	move
	-100 125 0
	rotate
	x -90
	box
	-40 0 40 40 100 80
	#LEFT LOWER ARM
	push
	move
	-20 -100 0
	box
	-10 0 10 20 125 20
	#PROJECTILE LEFT
	push
	move
	%s 0 0
	box
	-10 0 10 20 20 20
	pop
	pop
	pop
	#RIGHT ARM
	push
	move
	100 125 0
	rotate
	x -90
	box
	0 0 40 40 100 80
	#RIGHT LOWER ARM
	push
	move
	20 -100 0
	box
	-10 0 10 20 125 20
	#PROJECTILE RIGHT
	push
	move
	%s 0 0
	box
	-10 0 10 20 20 20
	pop
	pop
	pop
	#LEFT LEG
	push
	move
	-100 -125 0
	box
	0 0 40 50 120 80
	pop
	#RIGHT LEG
	push
	move
	100 -125 0
	box
	-50 0 40 50 120 80
	save
	robot%s.png
	''' %((x+5)*20,-1*x*10,-1*x*10+10,(x+5)*2)
	f = open('script', 'w')
	f.write(s)
	f.close()

def main():
	for x in [y*20 for y in range(5)]:
		screen = new_screen()
		make_script(x)
		parse_file( 'script', edges, transform, screen, color )
	for x in range(13):
		screen = new_screen()
		make_script_2(x)
		parse_file('script',edges,transform,screen,color)
		
main()