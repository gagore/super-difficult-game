import pygame 
import lib.objApi as objs

pygame.init()

# 소리 등록 & 설정
soundScore = pygame.mixer.Sound( "./asset/score.wav" )
soundDeath = pygame.mixer.Sound( "./asset/death.wav" )
soundMusic1 = pygame.mixer.Sound( "./asset/music1.wav" )

#무한 반복
soundMusic1.play(-1)

# 맵 비율 28 : 16(new_height(line55에 있음) 기준)
width = 560
height = 370

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
grey = (200, 200, 220)
dark_grey = (120, 120 ,120)
yellow = (255, 255, 0)
purple = (200, 150, 200)
mint = (190, 255, 230)
fps = pygame.time.Clock()

background = pygame.display.set_mode((width, height))
pygame.display.set_caption("세상에서 가장 어려운 게임 beta")

x_pos = 43
y_pos = 93

to_x_up = 0
to_x_down = 0
to_y_up = 0
to_y_down = 0

death = 0

yellow_balls = []
m = [1, 1, 1, 1, 1] # yellow_ball의 존재 여부(0: x, 1: o), 리스트의 길이 = yellow_ball 개수
is_clear = 0 # 게임 클리어 여부

avatar_size = 15

score_board_height = 50

new_height = height - score_board_height

pixel = 20

map_rect_list = []


def home():
	
	global x_pos
	global y_pos
	global death
	global m
	x_pos = 43
	y_pos = 93
	death += 1
	soundDeath.stop()
	soundDeath.play()

	for i in range (5): # 괄호 안의 숫자는 yellow_ball 개수 
		m[i] = 1 # 죽었을 때 yellow_ball 모두 복원

# objs.createObject(시작위치)    .set_movement(상대 이동 좌표)  .set_speed(편도로 이동까지 걸리는 틱).set_Boomerang(돌아올지 결정 기본값: True)
# objs.createObject(X좌표, Y좌표).set_movement(x증가값, y증가값).set_speed(int입력)                .set_Boomerang(True/False)

def objappear():
	objs.createObject(4 * pixel + 6 + 4, pixel + 6).set_size(6).set_movement(0, 7 * pixel + 10).set_speed(150).set_Boomerang(True)
	objs.createObject(6 * pixel + 6 + 4, pixel + 6).set_size(6).set_movement(0, 7 * pixel + 10).set_speed(150).set_Boomerang(True)
	objs.createObject(8 * pixel + 6 + 4, pixel + 6).set_size(6).set_movement(0, 7 * pixel + 10).set_speed(150).set_Boomerang(True)
	objs.createObject(10 * pixel + 6 + 4, pixel + 6).set_size(6).set_movement(0, 7 * pixel + 10).set_speed(150).set_Boomerang(True)
	objs.createObject(12 * pixel + 6 + 4, pixel + 6).set_size(6).set_movement(0, 7 * pixel + 10).set_speed(150).set_Boomerang(True)
	objs.createObject(14 * pixel + 6 + 4, pixel + 6).set_size(6).set_movement(0, 7 * pixel + 10).set_speed(150).set_Boomerang(True)

	objs.createObject(5 * pixel + 6 + 4, 8 * pixel + 6 + 6 + 4).set_size(6).set_movement(0, -7 * pixel - 10).set_speed(150).set_Boomerang(True)
	objs.createObject(7 * pixel + 6 + 4, 8 * pixel + 6 + 6 + 4).set_size(6).set_movement(0, -7 * pixel - 10).set_speed(150).set_Boomerang(True)
	objs.createObject(9 * pixel + 6 + 4, 8 * pixel + 6 + 6 + 4).set_size(6).set_movement(0, -7 * pixel - 10).set_speed(150).set_Boomerang(True)
	objs.createObject(11 * pixel + 6 + 4, 8 * pixel + 6 + 6 + 4).set_size(6).set_movement(0, -7 * pixel - 10).set_speed(150).set_Boomerang(True)
	objs.createObject(13 * pixel + 6 + 4, 8 * pixel + 6 + 6 + 4).set_size(6).set_movement(0, -7 * pixel - 10).set_speed(150).set_Boomerang(True)
	objs.createObject(15 * pixel + 6 + 4, 8 * pixel + 6 + 6 + 4).set_size(6).set_movement(0, -7 * pixel - 10).set_speed(150).set_Boomerang(True)

	objs.createObject(21 * pixel + 6 + 4, 2 * pixel + 6).set_size(6).set_movement(0, 7 * pixel + 10).set_speed(180).set_Boomerang(True)
	objs.createObject(23 * pixel + 6 + 4, 2 * pixel + 6).set_size(6).set_movement(0, 7 * pixel + 10).set_speed(180).set_Boomerang(True)

	objs.createObject(26 * pixel + 6 + 4 + 4, 4 * pixel + 6 + 4).set_size(6).set_movement(-7 * pixel - 10, 0).set_speed(180).set_Boomerang(True)
	objs.createObject(26 * pixel + 6 + 4 + 4, 6 * pixel + 6 + 4).set_size(6).set_movement(-7 * pixel - 10, 0).set_speed(180).set_Boomerang(True)

	objs.createObject(19 * pixel + 6, 5 * pixel + 6 + 4).set_size(6).set_movement(7 * pixel + 10, 0).set_speed(180).set_Boomerang(True)
	objs.createObject(19 * pixel + 6, 7 * pixel + 6 + 4).set_size(6).set_movement(7 * pixel + 10, 0).set_speed(180).set_Boomerang(True)

	objs.createObject(22 * pixel + 6 + 4 , 9 * pixel + 6 + 4 + 4).set_size(6).set_movement(0, -7 * pixel -4 -4).set_speed(180).set_Boomerang(True)
	objs.createObject(24 * pixel + 6 + 4, 9 * pixel + 6 + 4 + 4).set_size(6).set_movement(0, -7 * pixel -4 -4).set_speed(180).set_Boomerang(True)

	objs.createObject(4 * pixel + 6 + 4, 14 * pixel + 6 + 4 + 4).set_size(6).set_movement(0, -4 * pixel - 4 - 4).set_speed(150).set_Boomerang(True)
	objs.createObject(6 * pixel + 6 + 4, 14 * pixel + 6 + 4 + 4).set_size(6).set_movement(0, -4 * pixel - 4 - 4).set_speed(150).set_Boomerang(True)
	objs.createObject(8* pixel + 6 + 4, 14 * pixel + 6 + 4 + 4).set_size(6).set_movement(0, -4 * pixel - 4 - 4).set_speed(150).set_Boomerang(True)
	objs.createObject(10 * pixel + 6 + 4, 14 * pixel + 6 + 4 + 4).set_size(6).set_movement(0, -4 * pixel - 4 - 4).set_speed(150).set_Boomerang(True)
	objs.createObject(12 * pixel + 6 + 4, 14 * pixel + 6 + 4 + 4).set_size(6).set_movement(0, -4 * pixel - 4 - 4).set_speed(150).set_Boomerang(True)
	objs.createObject(14 * pixel + 6 + 4, 14 * pixel + 6 + 4 + 4).set_size(6).set_movement(0, -4 * pixel - 4 - 4).set_speed(150).set_Boomerang(True)
	objs.createObject(16 * pixel + 6 + 4, 14 * pixel + 6 + 4 + 4).set_size(6).set_movement(0, -4 * pixel - 4 - 4).set_speed(150).set_Boomerang(True)
	objs.createObject(18 * pixel + 6 + 4, 14 * pixel + 6 + 4 + 4).set_size(6).set_movement(0, -4 * pixel - 4 - 4).set_speed(150).set_Boomerang(True)

	objs.createObject(5 * pixel + 6 + 4, 10 * pixel + 6).set_size(6).set_movement(0, 4 * pixel + 10).set_speed(150).set_Boomerang(True)
	objs.createObject(7 * pixel + 6 + 4, 10 * pixel + 6).set_size(6).set_movement(0, 4 * pixel + 10).set_speed(150).set_Boomerang(True)
	objs.createObject(9 * pixel + 6 + 4, 10 * pixel + 6).set_size(6).set_movement(0, 4 * pixel + 10).set_speed(150).set_Boomerang(True)
	objs.createObject(11 * pixel + 6 + 4, 10 * pixel + 6).set_size(6).set_movement(0, 4 * pixel + 10).set_speed(150).set_Boomerang(True)
	objs.createObject(13 * pixel + 6 + 4, 10 * pixel + 6).set_size(6).set_movement(0, 4 * pixel + 10).set_speed(150).set_Boomerang(True)
	objs.createObject(15 * pixel + 6 + 4, 10 * pixel + 6).set_size(6).set_movement(0, 4 * pixel + 10).set_speed(150).set_Boomerang(True)
	objs.createObject(17 * pixel + 6 + 4, 10 * pixel + 6).set_size(6).set_movement(0, 4 * pixel + 10).set_speed(150).set_Boomerang(True)

	objs.createObject(4 * pixel + 6 + 4, 11 * pixel + 6 + 4).set_size(6).set_movement(4 * pixel, 0).set_speed(150).set_Boomerang(True)
	objs.createObject(4 * pixel + 6 + 4, 12 * pixel + 6 + 4).set_size(6).set_movement(4 * pixel, 0).set_speed(150).set_Boomerang(True)
	objs.createObject(4 * pixel + 6 + 4, 13 * pixel + 6 + 4).set_size(6).set_movement(4 * pixel, 0).set_speed(150).set_Boomerang(True)
	objs.createObject(4 * pixel + 6 + 4, 14 * pixel + 6 + 4).set_size(6).set_movement(4 * pixel, 0).set_speed(150).set_Boomerang(True)

	objs.createObject(9 * pixel + 6 + 4, 10 * pixel + 6 + 4).set_size(6).set_movement(4 * pixel, 0).set_speed(150).set_Boomerang(True)
	objs.createObject(9 * pixel + 6 + 4, 11 * pixel + 6 + 4).set_size(6).set_movement(4 * pixel, 0).set_speed(150).set_Boomerang(True)
	objs.createObject(9 * pixel + 6 + 4, 12 * pixel + 6 + 4).set_size(6).set_movement(4 * pixel, 0).set_speed(150).set_Boomerang(True)
	objs.createObject(9 * pixel + 6 + 4, 13 * pixel + 6 + 4).set_size(6).set_movement(4 * pixel, 0).set_speed(150).set_Boomerang(True)

	objs.createObject(14 * pixel + 6 + 4, 11 * pixel + 6 + 4).set_size(6).set_movement(4 * pixel, 0).set_speed(150).set_Boomerang(True)
	objs.createObject(14 * pixel + 6 + 4, 12 * pixel + 6 + 4).set_size(6).set_movement(4 * pixel, 0).set_speed(150).set_Boomerang(True)
	objs.createObject(14 * pixel + 6 + 4, 13 * pixel + 6 + 4).set_size(6).set_movement(4 * pixel, 0).set_speed(150).set_Boomerang(True)
	objs.createObject(14 * pixel + 6 + 4, 14 * pixel + 6 + 4).set_size(6).set_movement(4 * pixel, 0).set_speed(150).set_Boomerang(True)


play = True # 게임 중이란 뜻

objappear()

while play:
	
	deltaTime = fps.tick(120) # 1초에 whlie 문을 120번 돌림

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			play = False
		if is_clear == 0:
			# wasd 지원 추가
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					to_y_up = -1
				elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
					to_y_down = 1
				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					to_x_up = 1
				elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
					to_x_down = -1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					to_y_up = 0
				elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
					to_y_down = 0
				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					to_x_up = 0
				elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
					to_x_down = 0

		if is_clear == 1:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					x_pos = 43
					y_pos = 93
					to_x_down = 0
					to_x_up = 0
					to_y_down = 0
					to_y_up = 0
					death = 0
					is_clear = 0
					objappear()
				if event.key == pygame.K_e:
					pygame.quit()

	background.fill(grey)

	map_rect_pos = []
	map_rect_pos.append((0, 0, width, pixel))
	map_rect_pos.append((width - pixel, pixel, pixel, new_height - 2 * pixel))
	map_rect_pos.append((0, new_height - pixel, width, pixel))
	map_rect_pos.append((0, pixel, pixel,  new_height - 2 * pixel))

	map_rect_pos.append((pixel, pixel, 3 * pixel, 3 * pixel))
	map_rect_pos.append((width * 16/28, pixel, 5 * pixel, 3 * pixel))
	map_rect_pos.append((width * 21/28, pixel, 4 * pixel, pixel))
	map_rect_pos.append((width * 25/28, pixel, 2 * pixel, 3 * pixel))

	map_rect_pos.append((pixel, 6 * pixel, 3 * pixel, 3 * pixel))
	map_rect_pos.append((width * 16/28, 6 * pixel, 3 * pixel, 3 * pixel))

	map_rect_pos.append((pixel, 9* pixel, 19 * pixel, pixel))
	map_rect_pos.append((width * 19/28, 8 * pixel, 2 * pixel, 4 * pixel))
	map_rect_pos.append((width * 25/28, 8 * pixel, 2 * pixel, 6 * pixel))

	map_rect_pos.append((pixel, 12* pixel, 3 * pixel, 3 * pixel))
	map_rect_pos.append((width * 19/28, 14 * pixel, 8 * pixel, pixel))

   
	for i in range(15):
		map_rect = pygame.draw.rect(background, dark_grey, map_rect_pos[i])
		map_rect_list.append(map_rect)


	start_rect = pygame.draw.rect(background, mint, (pixel, 4 * pixel, 3 * pixel, 2 * pixel))
	
	restzone_rect1 = pygame.draw.rect(background, purple, (width * 16/28, 4 * pixel, 3 * pixel, 2 * pixel))
	restzone_rect2_1 = pygame.draw.rect(background, purple, (width * 19/28, 12 * pixel, 2 * pixel, 2 * pixel))
	restzone_rect2_2 = pygame.draw.rect(background, purple, (width * 21/28, 10 * pixel, 4 * pixel, 4 * pixel))

	goal_rect = pygame.draw.rect(background, mint, (pixel, 10* pixel, 3 * pixel, 2 * pixel))


	if m[0] == 1: # 첫 번째 yellow_ball이 1이라면 yellow_ball 그려라
		yellow_ball1 = pygame.draw.circle(background, yellow, (4 * pixel + 5 + 5, pixel + 5 + 5), 5)
		yellow_balls.append(yellow_ball1)

	if m[1] == 1:
		yellow_ball2 = pygame.draw.circle(background, yellow, (15 * pixel + 5 + 5, pixel + 5 + 5), 5)
		yellow_balls.append(yellow_ball2)
		
	if m[2] == 1:
		yellow_ball3 = pygame.draw.circle(background, yellow, (23 * pixel, 6 * pixel), 5)
		yellow_balls.append(yellow_ball3)

	if m[3] == 1:
		yellow_ball4 = pygame.draw.circle(background, yellow, (4 * pixel + 5 + 5, 8 * pixel + 5 + 5), 5)
		yellow_balls.append(yellow_ball4)

	if m[4] == 1:
		yellow_ball5 = pygame.draw.circle(background, yellow, (15 * pixel + 5 + 5, 8 * pixel + 5 + 5), 5)
		yellow_balls.append(yellow_ball5)


	score_board = pygame.draw.rect(background, black, (0, new_height, 560, score_board_height))

	avatar = pygame.draw.rect(background, red, (x_pos, y_pos , avatar_size, avatar_size))
	avatar_b = pygame.draw.rect(background, (0, 0 , 0), (x_pos, y_pos , avatar_size, avatar_size), 2)

	font1 = pygame.font.SysFont(None,30)
	deaths_text = font1.render('DEATHS: %d' %death, True, white)
	background.blit(deaths_text, (width*3/4, new_height + 15))


	for i in range (15):
		if avatar_b.colliderect(map_rect_list[i]):
			home()


	for i in range (5):
		if avatar_b.colliderect(yellow_balls[i]):
			if m[i] != 0:
				soundScore.play()
			m[i] = 0
	
	
	if avatar_b.colliderect(goal_rect) and m == [0, 0, 0, 0, 0]:
		
		is_clear = 1

		background.fill(black)

		font1 = pygame.font.SysFont(None,40)
		img1 = font1.render('DEATHS: %d' %death, True, white)
		background.blit(img1, (200,200))

		font2 = pygame.font.SysFont(None,100)
		img2 = font2.render("YOU WIN", True, white)
		background.blit(img2, (120,120))

		
		font3 = pygame.font.SysFont(None, 25)
		img3 = font3.render('PRESS R ON YOUR KEYBOARD TO RESTART', True, (0, 0, 255))
		background.blit(img3, (100, 250))

		font4 = pygame.font.SysFont(None, 25)
		img4 = font3.render('PRESS E ON YOUR KEYBOARD TO QUIT THE GAME', True, red)
		background.blit(img4, (70, 280))

		objs.deleteAllObjects()


	if objs.refreshObjets(avatar_b, background) == False:
		home()

	if is_clear == 0:
		x_pos += to_x_up + to_x_down 
		y_pos += to_y_up + to_y_down 
	
	pygame.display.update()

pygame.quit()