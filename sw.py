import pygame
#initialize
pygame.init()
#height and width
x= 1280
y= 700

#color
white=(255,255,255)
black=(0,0,0)

#first window
screen = pygame.display.set_mode((x,y))

screen.fill(white)

#logic and game
game = True
fps = 30
s = 0
m = s/fps
player=[100,y/2,50,30]
up, left, right, down = False, False, False, False

#shoot
bullet = []
nbullet = [player[0]+50,player[1]+10,10,10]
#enemy

epos =[]
ep =[x-90,10,True, True]
ebullet = []
enbullet = [x-90]
class enemy:
	def __init__(self, posx, posy):
		self.x = posx
		self.y = posy

	def draw(self):
		pygame.draw.ellipse(screen, black, pygame.Rect(self.x,self.y, 50, 30))



#looping
while game:
	screen.fill(white)

	#event key
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_UP:
				up = True
			if e.key == pygame.K_LEFT:
				left = True
			if e.key == pygame.K_RIGHT:
				right = True
			if e.key == pygame.K_DOWN:
				down = True
			if e.key == pygame.K_SPACE:
				nbullet = [player[0]+50,player[1]+10,10,10]
				bullet.insert(0, list(nbullet))
		if e.type == pygame.KEYUP:
			if e.key == pygame.K_UP:
				up = False
			if e.key == pygame.K_LEFT:
				left = False
			if e.key == pygame.K_RIGHT:
				right = False
			if e.key == pygame.K_DOWN:
				down = False


	if player[0]>=0 and player[0]+50<=x and player[1]>=0 and player[1]+30<=y:
		if up == True:
			player[1]-=10
		if left == True:
			player[0]-=10
		if right == True:
			player[0]+=10
		if down == True:
			player[1]+=10
	if player[0]<0:
		player[0]=0
	if player[0]+50>x:
		player[0]=x-50
	if player[1]<0:
		player[1]=0
	if player[1]+30>y:
		player[1]=y-30

	#draw enemy

	for a in epos:
		e1 = enemy(a[0],a[1])
		e1.draw()
		i = epos.index(a)

		if epos[i][0]>x-100:
			epos[i][2] = True
		if epos[i][0]<x-400:
			epos[i][2] = False
		if epos[i][1]>y-100:
			epos[i][3]=False
		if epos[i][1]<100:
			epos[i][3]=True

		if epos[i][2] == True:
			epos[i][0]-=5
		elif epos[i][2] == False:
			epos[i][0]+=5
		if epos[i][3] == True:
			epos[i][1] +=5
		if epos[i][3] == False:
			epos[i][1] -=5

		if epos[i][1] == player[1]:
			enbullet = [epos[i][0],epos[i][1]+10,10,10]
			ebullet.insert(0, list(enbullet))



	#draw
	pygame.draw.ellipse(screen, black, pygame.Rect(player))
	for b in bullet:
		pygame.draw.ellipse(screen,black,pygame.Rect(b))
		b[0]+=10
		f = bullet.index(b)
		if b[0]>x:
			bullet.pop()
		for c in epos:
			d = epos.index(c)
			if b[0]+10 >= epos[d][0] and b[0]<=epos[d][0]+50 and b[1]<=epos[d][1]+30 and b[1]+10>=epos[d][1]:
				epos.pop(d)
				bullet.pop(f)
	for eb in ebullet:
		pygame.draw.ellipse(screen, black, pygame.Rect(eb))
		eb[0]-=5
		if eb[0]<0:
			ebullet.pop()
		if eb[0]<=player[0]+50 and eb[0]+10>=player[0] and eb[1]<=player[1]+50 and eb[1]+10 >= player[1]:
			game = False
	#update

	s+=1
	m = int(s/fps)
	if s<5000:
		if s%100 == 0:
			epos.insert(0, list(ep))
	elif s>=5000 and s<10000:
		if s%80 == 0:
			epos.insert(0, list(ep))
	elif s>=10000:
		if s%50 == 0:
			epos.insert(0, list(ep))
#	print(int(m))
	pygame.time.Clock().tick(fps)
	pygame.display.update()