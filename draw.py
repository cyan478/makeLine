from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
	x = x0
	y = y0

	A = y1 - y0
	B = x0 - x1

	A = 2*A
	B = 2*B

	if (x0 > x1):
		draw_line(x1, y1, x0, y0, screen, color)
		return 0

	if A >= 0:
		# ============================= I
		if 	-B >= A:
			d = 2*A + B
			while x < x1:
				plot(screen,color,x,y)
				if d > 0:
					y += 1
					d += B
				x += 1
				d += A

	# ============================= II
		else:
			d = A + 2*B
			while y < y1:
				plot(screen,color,x,y)
				if d < 0:
					x += 1
					d += A
				y += 1
				d += B

	# ============================= VIII
	else:
		if B <= A:
			d = 2*A - B
			while x < x1:
				plot(screen,color,x,y)
				if d < 0:
					y -= 1
					d -= B
				x +=1
				d += A

	# ============================= VII
		else:
			d = A - 2*B
			while y > y1:
				plot(screen,color,x,y)
				if d > 0:
					x += 1
					d += A
				y -= 1
				d -= B

