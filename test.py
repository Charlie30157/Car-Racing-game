from tkinter import *
from tkinter import PhotoImage
from PIL import ImageTk,Image
win = Tk()
win.title("Games")
win.geometry('500x500')

def game_2():	
	import pygame
	from random import randint
	from pygame import image
	from pygame import font
	from pygame import transform
	pygame.init()
	screen = pygame.display.set_mode((800,400))
	pygame.display.set_caption('Circuit 0')
	game_active = False
	def display_score():
		global current_time
		current_time = int(pygame.time.get_ticks() / 1000) - start_time
		score_surf = test_font.render(f'Score: {current_time}',True,(64,64,64))
		score_rect = score_surf.get_rect(topleft = (600,0))
		screen.blit(score_surf,score_rect)
		return current_time
	def collisions(player,obstacles):
		if obstacles:
			for obstacle_rect in obstacles: 
				if player.colliderect(obstacle_rect) : 
					crash_music = pygame.mixer.Sound('crash_sound.wav')
					crash_music.play(0)
					crash_music.set_volume(0.3)
					return False
		return True
	test_font =font.Font(None, 50)
	start_time = 0
	#music
	bg_music = pygame.mixer.Sound('bg_sound.mp3')
	bg_music.play()
	bg_music.set_volume(0.09)
	def scale_image(img, factor):
		size = round(img.get_width() * factor), round(img.get_height() * factor)
		return transform.scale(img, size)
	def obstacles_movement(obstacle_list):
		if obstacle_list:
			for obstacle_rect in obstacle_list:
				if display_score()>30:
					obstacle_rect.y+=12
				elif display_score()>10:
					obstacle_rect.y+=5
				elif display_score()>40:
					obstacle_rect.y+=15
				elif display_score()>15:
					obstacle_rect.y+=9
				else:
					obstacle_rect.y += 2
				if obstacle_rect.right >= 330 and obstacle_rect.right <= 450 :
					screen.blit(taxi,obstacle_rect)
				elif obstacle_rect.right >= 460 and obstacle_rect.right <= 550:
					screen.blit(truck,obstacle_rect)
				else:
					screen.blit(green_car,obstacle_rect)
			obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.y >= -50]
			return obstacle_list
		else : return []
	clock = pygame.time.Clock()
	left_part = pygame.Surface((200,400)) 
	left_part.fill('bisque1')
	center = pygame.Surface((400,400))
	center.fill('antiquewhite4')
	right_part = pygame.Surface((200,400))
	right_part.fill('bisque1')
	bush = scale_image(image.load('bush.png'),0.22)
	bush_rect = bush.get_rect(midbottom = (50,220))
	bush_rect2 = bush.get_rect(midbottom = (150,80))
	bush_rect3 = bush.get_rect(midbottom = (650,50))
	bush_rect4 = bush.get_rect(midbottom = (750,190))
	red_car = pygame.image.load('red-car.png')
	rc_rect = red_car.get_rect(midbottom = (300,390))
	green_car = pygame.image.load('green-car.png')
	gc_rect = green_car.get_rect(midtop = (230,0))
	taxi = scale_image(pygame.image.load('taxi.png'),0.62)
	truck = scale_image(pygame.image.load('truck.png'),0.62)
	text_surf = test_font.render('Score',True,'Green')
	#front page
	f1 = pygame.image.load('f1.png')
	f1 = pygame.transform.scale2x(f1)
	f1_rect = f1.get_rect(center = (400,200))
	#end page
	game_name = test_font.render('Circuit0',False,'cyan3')
	game_name_rect = game_name.get_rect(topleft = (350,100))
	run = test_font.render('Click on space to run',False,'cyan3')
	over = test_font.render('Game Over',False,'black')
	over_rect = over.get_rect(center = (400,150))
	run_rect = run.get_rect(topleft = (250,300))
	score = 0
	obstacles_rect_list = []
	obstacle_timer = pygame.USEREVENT + 1
	pygame.time.set_timer(obstacle_timer,1700)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				
				pygame.quit()
				exit()
			if game_active :
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						rc_rect.y -= 50
						if rc_rect.top <= 0 : rc_rect.top = 0 
					if event.key == pygame.K_s:
						rc_rect.y += 50
						if rc_rect.bottom >= 400 : rc_rect.bottom = 400
					if event.key == pygame.K_d:
						rc_rect.x += 50
						if rc_rect.right >=600 : rc_rect.right = 600
					if event.key == pygame.K_a:
						rc_rect.x -= 50
						if rc_rect.left <=200 : rc_rect.left = 200
			else:
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
					rc_rect.x +=50
					game_active = True 
					start_time = int(pygame.time.get_ticks() / 1000)
			if event.type == obstacle_timer and game_active:
				if randint(1,5) == 2:
					obstacles_rect_list.append(green_car.get_rect(midtop = (randint(230,330),-50)))
				elif randint(1,5) == 3:
					obstacles_rect_list.append(taxi.get_rect(midtop = (randint(340,450),-50)))
				else :
					obstacles_rect_list.append(truck.get_rect(midtop = (randint(460,570),-50)))


		if game_active :
			screen.blit(left_part,(0,0))
			screen.blit(right_part,(600,0))
			bush_rect.y += 3 
			if bush_rect.top >=400: bush_rect.top = 0
			screen.blit(bush,bush_rect)
			bush_rect2.y +=3
			if bush_rect2.top >=400: bush_rect2.top = 0
			screen.blit(bush,bush_rect2)
			bush_rect3.y +=3
			if bush_rect3.top >=400 : bush_rect3.top = 0
			screen.blit(bush,bush_rect3)
			bush_rect4.y += 3
			if bush_rect4.top >= 400 : bush_rect4.top = 0
			screen.blit(bush,bush_rect4)
			screen.blit(center,(200,0))
			screen.blit(red_car,rc_rect)
			obstacles_rect_list = obstacles_movement(obstacles_rect_list)
			score = display_score() 
			game_active = collisions(rc_rect,obstacles_rect_list)

		else:
			obstacles_rect_list.clear()
			q = rc_rect.x - 50
			w = rc_rect.y -50 
			crash = image.load('crash.png')
			screen.blit(crash,(q,w))
			play_again = test_font.render('Play Again',True,'black')
			play_again_rect = play_again.get_rect(center = (400,250))
			game_score = test_font.render(f'Your score : {score}',False,'black').convert_alpha()
			game_score_rect = game_score.get_rect(center = (400,100))
			if score == 0:
				screen.blit(f1,f1_rect)
				screen.blit(game_name,game_name_rect)
				screen.blit(run,run_rect)
			else : 
				screen.blit(over,over_rect)
				screen.blit(game_score,game_score_rect)
				screen.blit(play_again,play_again_rect)
		pygame.display.update()
		clock.tick(50)
		
bg = ImageTk.PhotoImage(file = r"D:\PYTHON MINI-PROJECT\bg.png")
my_canvas = Canvas(win,width=500,height=500)
my_canvas.pack(fill="both",expand=True)
my_canvas.create_image(0,0,image = bg,anchor="nw")
my_canvas.create_text(600,400,text="CIRCUIT O",font=("Georgia",50),fill="white")
my_canvas.create_text(650,500,text = "CHOOSE A GAME",font=("Georgia",50),fill="white")
btn_2 = Button(text = "Arcade game",font=("Georgia",20),padx= 10,pady = 10,bg ='VioletRed2',fg = 'black',activebackground='black',activeforeground='white',command =game_2)
btn_2_win =  my_canvas.create_window(200,400,anchor="nw",window=btn_2)
def resizer(e):
    global bg1 ,resized_image,new_bg
    bg1 = Image.open(r"D:\PYTHON MINI-PROJECT\bg.png")
    resized_image = bg1.resize((e.width,e.height))
    new_bg = ImageTk.PhotoImage(resized_image)
    my_canvas.create_image(0,0,image = new_bg,anchor="nw")
    my_canvas.create_text(800,100,text="CIRCUIT O",font=("Georgia",50),fill="black")
    my_canvas.create_text(800,250,text = "CHOOSE A GAME",font=("Georgia",50),fill="black")

win.bind('<Configure>',resizer)
win.mainloop()

