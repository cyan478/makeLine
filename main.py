from display import *
from draw import *

screen = new_screen()
color = [ 0, 0, 0 ]

'''
draw_line(0, 0, 250, 500, screen, color )
draw_line(250, 500, 500, 0, screen, color)
draw_line(500, 0, 0, 250, screen, color)
draw_line(0, 250, 500, 500, screen, color)
draw_line(500, 500, 250, 0, screen, color)
draw_line(250, 0, 0, 500, screen, color)
draw_line(0, 500, 500, 250, screen, color)
draw_line(500, 250, 0, 0, screen, color)

draw_line(0, 0, 500, 500, screen, color)
draw_line(0, 500, 500, 0, screen, color)
draw_line(250, 0, 250, 500, screen, color)
draw_line(0, 250, 500, 250, screen, color)
'''
for i in range(0,500):
	for j in range(0,500):
		color[2] = (i^j * j^700) % 256
    	draw_line(250,500,i,0,screen,color)
    	draw_line(500,250,0,i,screen,color)


display(screen)
save_extension('img.png')


