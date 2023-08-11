import pygame
import funcs
import random
import time
import serial
import pandas as pd
from sys import exit
from datetime import datetime
import os
from pyfirmata import Arduino, util
from inspect import signature

pygame.init()
screen = pygame.display.set_mode((1080,720))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()

lightblue = pygame.Color('lightskyblue3')
black = pygame.Color('black')
gray = pygame.Color('gray')
white = pygame.Color('white')

background = pygame.image.load('graphics/background.png').convert()
background = pygame.transform.scale(background, (1080,720))

# Inicializacion de botones

button_start = pygame.image.load('graphics/start.png').convert_alpha()
button_start = pygame.transform.scale(button_start, (button_start.get_width()/2,button_start.get_height()/2))
button_start_hover = pygame.image.load('graphics/start_hover.png').convert_alpha()
button_start_hover = pygame.transform.scale(button_start_hover, (button_start_hover.get_width()/2,button_start_hover.get_height()/2))
button_start_mask = pygame.mask.from_surface(button_start)
button_start_rect = button_start.get_rect(topleft = (200,200))

button_quit = pygame.image.load('graphics/quit.png').convert_alpha()
button_quit = pygame.transform.scale(button_quit, (button_quit.get_width()/2,button_quit.get_height()/2))
button_quit_hover = pygame.image.load('graphics/quit_hover.png').convert_alpha()
button_quit_hover = pygame.transform.scale(button_quit_hover, (button_quit_hover.get_width()/2,button_quit_hover.get_height()/2))
button_quit_mask = pygame.mask.from_surface(button_quit)
button_quit_rect = button_start.get_rect(topright = (880,200))

button_one = pygame.image.load('graphics/button_one.png').convert_alpha()
button_one = pygame.transform.scale(button_one, (button_one.get_width()/2,button_one.get_height()/2))
button_one_hover = pygame.image.load('graphics/button_one_hover.png').convert_alpha()
button_one_hover = pygame.transform.scale(button_one_hover, (button_one_hover.get_width()/2,button_one_hover.get_height()/2))
button_one_mask = pygame.mask.from_surface(button_one)
button_one_rect = button_one.get_rect(topleft = (200,200))

button_two = pygame.image.load('graphics/button_two.png').convert_alpha()
button_two = pygame.transform.scale(button_two, (button_two.get_width()/2,button_two.get_height()/2))
button_two_hover = pygame.image.load('graphics/button_two_hover.png').convert_alpha()
button_two_hover = pygame.transform.scale(button_two_hover, (button_two_hover.get_width()/2,button_two_hover.get_height()/2))
button_two_mask = pygame.mask.from_surface(button_two)
button_two_rect = button_two.get_rect(topright = (880,200))

button_continue = pygame.image.load('graphics/continue.png').convert_alpha()
button_continue = pygame.transform.scale(button_continue, (button_continue.get_width()/2,button_continue.get_height()/2))
button_continue_hover = pygame.image.load('graphics/continue_hover.png').convert_alpha()
button_continue_hover = pygame.transform.scale(button_continue_hover, (button_continue_hover.get_width()/2,button_continue_hover.get_height()/2))
button_continue_mask = pygame.mask.from_surface(button_continue)
button_continue_rect = button_continue.get_rect(midtop = (540,530))

button_res_1 = pygame.image.load('graphics/res_1.png').convert_alpha()
button_res_1 = pygame.transform.scale(button_res_1, (button_res_1.get_width()/2.2,button_res_1.get_height()/2.2))
button_res_1_hover = pygame.image.load('graphics/res_1_selected.png').convert_alpha()
button_res_1_hover = pygame.transform.scale(button_res_1_hover, (button_res_1_hover.get_width()/2.2,button_res_1_hover.get_height()/2.2))
button_res_1_mask = pygame.mask.from_surface(button_res_1)
button_res_1_rect = button_res_1.get_rect(midtop = (240,450))

button_res_2 = pygame.image.load('graphics/res_2.png').convert_alpha()
button_res_2 = pygame.transform.scale(button_res_2, (button_res_2.get_width()/2.2,button_res_2.get_height()/2.2))
button_res_2_hover = pygame.image.load('graphics/res_2_selected.png').convert_alpha()
button_res_2_hover = pygame.transform.scale(button_res_2_hover, (button_res_2_hover.get_width()/2.2,button_res_2_hover.get_height()/2.2))
button_res_2_mask = pygame.mask.from_surface(button_res_2)
button_res_2_rect = button_res_2.get_rect(midtop = (540,450))

button_res_3 = pygame.image.load('graphics/res_3.png').convert_alpha()
button_res_3 = pygame.transform.scale(button_res_3, (button_res_3.get_width()/2.2,button_res_3.get_height()/2.2))
button_res_3_hover = pygame.image.load('graphics/res_3_selected.png').convert_alpha()
button_res_3_hover = pygame.transform.scale(button_res_3_hover, (button_res_3_hover.get_width()/2.2,button_res_3_hover.get_height()/2.2))
button_res_3_mask = pygame.mask.from_surface(button_res_3)
button_res_3_rect = button_res_3.get_rect(midtop = (840,450))

button_send = pygame.image.load('graphics/send_data.png').convert_alpha()
button_send = pygame.transform.scale(button_send, (button_send.get_width()/2.2,button_send.get_height()/2.2))
button_send_hover = pygame.image.load('graphics/send_data_hover.png').convert_alpha()
button_send_hover = pygame.transform.scale(button_send_hover, (button_send_hover.get_width()/2.2,button_send_hover.get_height()/2.2))
button_send_mask = pygame.mask.from_surface(button_send)
button_send_rect = button_send.get_rect(midtop = (900,200))

# Inicializacion de imagenes y elementos graficos

clock_pic = pygame.image.load('graphics/clock.png').convert_alpha()
clock_pic = pygame.transform.scale(clock_pic, (clock_pic.get_width()/7,clock_pic.get_height()/7))
clock_pic_rect = clock_pic.get_rect(topleft = (10,10))

next_cup_red = pygame.image.load('graphics/fullcupred.png').convert_alpha()
next_cup_red = pygame.transform.scale(next_cup_red, (next_cup_red.get_width()/7,next_cup_red.get_height()/7))
next_cup_red_rect = next_cup_red.get_rect(topleft = (250,10))

next_cup_green = pygame.image.load('graphics/fullcupgreen.png').convert_alpha()
next_cup_green = pygame.transform.scale(next_cup_green, (next_cup_green.get_width()/7,next_cup_green.get_height()/7))
next_cup_green_rect = next_cup_green.get_rect(topleft = (250,10))

machine_off = pygame.image.load('graphics/maquina_0.png').convert_alpha()
machine_off = pygame.transform.scale(machine_off, (machine_off.get_width()/3,machine_off.get_height()/3))
machine_off_rect = machine_off.get_rect(midtop = (540,0))

machine_idle = pygame.image.load('graphics/maquina_1.png').convert_alpha()
machine_idle = pygame.transform.scale(machine_idle, (machine_idle.get_width()/3,machine_idle.get_height()/3))
machine_idle_rect = machine_idle.get_rect(midtop = (540,0))

machine_mid = pygame.image.load('graphics/maquina_2.png').convert_alpha()
machine_mid = pygame.transform.scale(machine_mid, (machine_mid.get_width()/3,machine_mid.get_height()/3))
machine_mid_rect = machine_mid.get_rect(midtop = (540,0))

machine_full = pygame.image.load('graphics/maquina_3.png').convert_alpha()
machine_full = pygame.transform.scale(machine_full, (machine_full.get_width()/3,machine_full.get_height()/3))
machine_full_rect = machine_full.get_rect(midtop = (540,0))

empty_cup = pygame.image.load('graphics/empty_cup.png').convert_alpha()
empty_cup = pygame.transform.scale(empty_cup, (empty_cup.get_width()/2.3,empty_cup.get_height()/2.3))
empty_cup_rect = empty_cup.get_rect(midtop = (540,250))

red_cup_30 = pygame.image.load('graphics/30cupred.png').convert_alpha()
red_cup_30 = pygame.transform.scale(red_cup_30, (red_cup_30.get_width()/2.3,red_cup_30.get_height()/2.3))
red_cup_30_rect = red_cup_30.get_rect(midtop = (540,250))

green_cup_30 = pygame.image.load('graphics/30cupgreen.png').convert_alpha()
green_cup_30 = pygame.transform.scale(green_cup_30, (green_cup_30.get_width()/2.3,green_cup_30.get_height()/2.3))
green_cup_30_rect = green_cup_30.get_rect(midtop = (540,250))

red_cup_60 = pygame.image.load('graphics/60cupred.png').convert_alpha()
red_cup_60 = pygame.transform.scale(red_cup_60, (red_cup_60.get_width()/2.3,red_cup_60.get_height()/2.3))
red_cup_60_rect = red_cup_60.get_rect(midtop = (540,250))

green_cup_60 = pygame.image.load('graphics/60cupgreen.png').convert_alpha()
green_cup_60 = pygame.transform.scale(green_cup_60, (green_cup_60.get_width()/2.3,green_cup_60.get_height()/2.3))
green_cup_60_rect = green_cup_60.get_rect(midtop = (540,250))

red_cup = pygame.image.load('graphics/fullcupred.png').convert_alpha()
red_cup = pygame.transform.scale(red_cup, (red_cup.get_width()/2.3,red_cup.get_height()/2.3))
red_cup_rect = red_cup.get_rect(midtop = (540,250))

green_cup = pygame.image.load('graphics/fullcupgreen.png').convert_alpha()
green_cup = pygame.transform.scale(green_cup, (green_cup.get_width()/2.3,green_cup.get_height()/2.3))
green_cup_rect = green_cup.get_rect(midtop = (540,250))

wrong_rep = pygame.image.load('graphics/wrong.png').convert_alpha()
wrong_rep = pygame.transform.scale(wrong_rep, (wrong_rep.get_width()/3.4,wrong_rep.get_height()/3.4))
wrong_rep_rect = wrong_rep.get_rect(midtop = (325,14))

good_rep = pygame.image.load('graphics/right.png').convert_alpha()
good_rep = pygame.transform.scale(good_rep, (good_rep.get_width()/3.4,good_rep.get_height()/3.4))
good_rep_rect = good_rep.get_rect(midtop = (325,14))

face_happy = pygame.image.load('graphics/face_happy.png').convert_alpha()
face_happy = pygame.transform.scale(face_happy, (face_happy.get_width()/4,face_happy.get_height()/4))
face_happy_rect = face_happy.get_rect(topleft = (830,15))

face_reg = pygame.image.load('graphics/face_reg.png').convert_alpha()
face_reg = pygame.transform.scale(face_reg, (face_reg.get_width()/4,face_reg.get_height()/4))
face_reg_rect = face_reg.get_rect(topleft = (830,15))

face_serious = pygame.image.load('graphics/face_serious.png').convert_alpha()
face_serious = pygame.transform.scale(face_serious, (face_serious.get_width()/4,face_serious.get_height()/4))
face_serious_reg = face_serious.get_rect(topleft = (830,15))

face_sad = pygame.image.load('graphics/face_sad.png').convert_alpha()
face_sad = pygame.transform.scale(face_sad, (face_sad.get_width()/4,face_sad.get_height()/4))
face_sad_reg = face_sad.get_rect(topleft = (830,15))

# Inicializacion de etiquetas y textos

select_train_text = pygame.image.load('graphics/select_train.png').convert_alpha()
select_train_text = pygame.transform.scale(select_train_text, (select_train_text.get_width()/2.5,select_train_text.get_height()/2.5))
select_train_rect = select_train_text.get_rect(midtop = (540, 50))

data_text_banner = pygame.image.load('graphics/data_text.png').convert_alpha()
data_text_banner = pygame.transform.scale(data_text_banner, (data_text_banner.get_width()/2.8,data_text_banner.get_height()/2.8))
data_text_banner_rect = data_text_banner.get_rect(midtop = (540, 5))

name_banner = pygame.image.load('graphics/Name.png').convert_alpha()
name_banner = pygame.transform.scale(name_banner, (name_banner.get_width()/2.8,name_banner.get_height()/2.8))
name_banner_rect = name_banner.get_rect(midtop = (160, 100))

age_banner = pygame.image.load('graphics/Age.png').convert_alpha()
age_banner = pygame.transform.scale(age_banner, (age_banner.get_width()/2.8,age_banner.get_height()/2.8))
age_banner_rect = age_banner.get_rect(midtop = (160, 250))

id_banner = pygame.image.load('graphics/ID.png').convert_alpha()
id_banner = pygame.transform.scale(id_banner, (id_banner.get_width()/2.8,id_banner.get_height()/2.8))
id_banner_rect = id_banner.get_rect(midtop = (160, 400))

train_end_banner = pygame.image.load('graphics/train_end_banner.png').convert_alpha()
train_end_banner = pygame.transform.scale(train_end_banner, (train_end_banner.get_width()/2.8,train_end_banner.get_height()/2.8))
train_end_banner_rect = train_end_banner.get_rect(midtop = (540, 5))

banner_complete_flex = pygame.image.load('graphics/banner_1.png').convert_alpha()
banner_complete_flex = pygame.transform.scale(banner_complete_flex, (banner_complete_flex.get_width()/3,banner_complete_flex.get_height()/3))
banner_complete_flex_rect = banner_complete_flex.get_rect(topleft = (130,40))

banner_partial_flex = pygame.image.load('graphics/banner_2.png').convert_alpha()
banner_partial_flex = pygame.transform.scale(banner_partial_flex, (banner_partial_flex.get_width()/3,banner_partial_flex.get_height()/3))
banner_partial_flex_rect = banner_partial_flex.get_rect(topleft = (130,190))

banner_complete_ext = pygame.image.load('graphics/banner_3.png').convert_alpha()
banner_complete_ext = pygame.transform.scale(banner_complete_ext, (banner_complete_ext.get_width()/3,banner_complete_ext.get_height()/3))
banner_complete_ext_rect = banner_complete_ext.get_rect(topleft = (130,340))

banner_partial_ext = pygame.image.load('graphics/banner_4.png').convert_alpha()
banner_partial_ext = pygame.transform.scale(banner_partial_ext, (banner_partial_ext.get_width()/3,banner_partial_ext.get_height()/3))
banner_partial_ext_rect = banner_partial_ext.get_rect(topleft = (130,490))

base_font = pygame.font.Font(None,50)
complete_flex = ''
#partial_flex = ''
complete_ext = ''
#partial_ext = ''
complete_flex_rect = pygame.Rect(420,100,350,50)
#partial_flex_rect = pygame.Rect(420,250,350,50)
complete_ext_rect = pygame.Rect(420,400,350,50)
#partial_ext_rect = pygame.Rect(420,550,350,50)

full_name = ''
identification = ''
age = ''

name_rect = pygame.Rect(350,157,500,60)
age_rect = pygame.Rect(350,307,500,60)
id_rect = pygame.Rect(350,457,500,60)

timer_banner = ''
timer_banner_rect = pygame.Rect(10,20,200,50)

main_menu = True
input_data = False
select_train_menu = False
play_game = False
touching_one = False
touching_two = False
touching_create = False
touching_continue = False

text_box_1 = True
text_box_2 = False
text_box_3 = False
text_box_4 = False

text_name = True
text_age = False
text_id = False

color_text_box_1 = lightblue
color_text_box_2 = gray
color_text_box_3 = gray
color_text_box_4 = gray

color_text_box_name = lightblue
color_text_box_id = gray
color_text_box_age = gray

saved_train = []
input_var = 0
t_start = 0
t_current = 0

idle = False
midway = False
active = False
done = False
rep_fail = False
rep_complete = False
rep_incomplete = False
highest_stage = "start"
train_end = False

happiness_weight = 0
good_flex_reps = 0
good_ext_reps = 0
incomplete_flex_reps = 0
incomplete_ext_reps = 0
failed_flex_reps = 0
failed_ext_reps = 0

good_flex_reps_banner = ""
good_ext_reps_banner = ""
incomplete_flex_reps_banner = ""
incomplete_ext_reps_banner = ""
failed_flex_reps_banner = ""
failed_ext_reps_banner = ""

collecting_data = []
counter = 0
counter_seconds = 0

res_1_const = 0.0171
res_1_offset = 0.0732
res_2_const = 0.0299
res_2_offset = 0.0704
res_3_const = 0.0306
res_3_offset = 0.1464

selected_res_const = 0
selected_res_offset = 0
selected_res_1 = False
selected_res_2 = False
selected_res_3 = False

data_sent = False
now = datetime.now()
now = str(now)[:-6]
data_to_send_array = {'created_at':[now],'field3':[0],'field4':[0]}
data_to_send = pd.DataFrame(data_to_send_array)
data_collected = False
window_ready = False

counter_for_past_angle = 0
#Calibración del sistema, con un punto ángulo, voltaje para utilizar la ecuación punto pendiente.
calibVolt = 1547
calibAng = 0

direction_changed = False
old_angle = 0

start = True

def close_game():
    pygame.quit
    exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_menu:
                if pygame.mouse.get_pressed()[0] and touching_quit:
                    close_game()
                elif pygame.mouse.get_pressed()[0] and touching_start:
                    main_menu = False
                    input_data = True
            elif input_data:
                if pygame.mouse.get_pressed()[0] and touching_continue and len(identification) == 9 and not(full_name == '' or age == '' or identification == ''):
                    channel_id = funcs.chanelID(identification)
                    if channel_id != "failed":
                        channel_apikey = funcs.chanelAPIKEY(channel_id)
                        input_data = False
                        select_train_menu = True
                
                if name_rect.collidepoint(event.pos):
                    text_name = True
                    text_age = False
                    text_id = False

                    color_text_box_name = lightblue
                    color_text_box_id = gray
                    color_text_box_age = gray

                elif age_rect.collidepoint(event.pos):
                    text_name = False
                    text_age = True
                    text_id = False
                
                    color_text_box_name = gray
                    color_text_box_id = gray
                    color_text_box_age = lightblue

                elif id_rect.collidepoint(event.pos):
                    text_name = False
                    text_age = False
                    text_id = True

                    color_text_box_name = gray
                    color_text_box_id = lightblue
                    color_text_box_age = gray

            elif select_train_menu:
                if pygame.mouse.get_pressed()[0] and touching_one:
                    complete_ext = funcs.dataread(str(channel_apikey), str(channel_id), str(7))
                    complete_flex = funcs.dataread(str(channel_apikey), str(channel_id), str(6))
                    saved_train = funcs.design_train(int(complete_flex), int(complete_ext))

                if pygame.mouse.get_pressed()[0] and touching_two and not selected_res_const == 0:
                    if len(saved_train) == 0:
                        saved_train = funcs.design_train(random.randint(1,10), int(random.randint(1,10)))
                    happiness_weight = funcs.set_weights(saved_train) 
                    t_start = time.time()
                    select_train_menu = False
                    play_game = True
                if pygame.mouse.get_pressed()[0] and touching_res_1:
                    selected_res_const = res_1_const
                    selected_res_offset = res_1_offset
                    selected_res_1 = True
                    selected_res_2 = False
                    selected_res_3 = False

                if pygame.mouse.get_pressed()[0] and touching_res_2:
                    selected_res_const = res_2_const
                    selected_res_offset = res_2_offset
                    selected_res_1 = False
                    selected_res_2 = True
                    selected_res_3 = False
                
                if pygame.mouse.get_pressed()[0] and touching_res_3:
                    selected_res_const = res_3_const
                    selected_res_offset = res_3_offset
                    selected_res_1 = False
                    selected_res_2 = False
                    selected_res_3 = True

            elif train_end:
                if pygame.mouse.get_pressed()[0] and touching_send and not data_sent:
                    funcs.UploadDataU(channel_apikey,current_happiness,good_flex_reps,good_ext_reps)
                    csv_to_send = data_to_send.to_csv("report.csv",index=False)
                    full_path = str(os.getcwd())+"\\report.csv"
                    funcs.UploadCSV(channel_apikey,full_path)
                    data_sent = True
                    close_game()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
                #input_var += 5 
            if event.key == pygame.K_BACKSPACE:
                pass
                #input_var -= 5
            if event.key == pygame.K_ESCAPE:
                close_game()
            if event.key == pygame.K_BACKSPACE and input_data:
                if text_name:
                    full_name = full_name[:-1]
                elif text_age:
                    age = age [:-1]
                elif text_id:
                    identification = identification[:-1]
            if (event.unicode.isalpha() or event.key == pygame.K_SPACE) and input_data:
                if text_name and len(full_name) <= 20:
                    full_name += event.unicode
            if event.unicode.isnumeric() and input_data:
                if text_age and len(age) <= 2:
                    age += event.unicode
                if text_id and len(identification) <= 8:
                    identification += event.unicode

    screen.blit(background,(0,0))
    
    pos = pygame.mouse.get_pos()

    if main_menu:
        current_happiness = 100

        pos_in_button_start_mask = pos[0] - button_start_rect.x, pos[1] - button_start_rect.y
        touching_start = button_start_rect.collidepoint(*pos) and button_start_mask.get_at(pos_in_button_start_mask)

        pos_in_button_quit_mask = pos[0] - button_quit_rect.x, pos[1] - button_quit_rect.y
        touching_quit = button_quit_rect.collidepoint(*pos) and button_quit_mask.get_at(pos_in_button_quit_mask)
    
    if input_data:
        pos_in_button_continue_mask = pos[0] - button_continue_rect.x, pos[1] - button_continue_rect.y
        touching_continue = button_continue_rect.collidepoint(*pos) and button_continue_mask.get_at(pos_in_button_continue_mask)

    if select_train_menu:
        pos_in_button_one_mask = pos[0] - button_one_rect.x, pos[1] - button_one_rect.y
        touching_one = button_one_rect.collidepoint(*pos) and button_one_mask.get_at(pos_in_button_one_mask)

        pos_in_button_two_mask = pos[0] - button_two_rect.x, pos[1] - button_two_rect.y
        touching_two = button_two_rect.collidepoint(*pos) and button_two_mask.get_at(pos_in_button_two_mask)

        pos_in_res_1_mask = pos[0] - button_res_1_rect.x, pos[1] - button_res_1_rect.y
        touching_res_1 = button_res_1_rect.collidepoint(*pos) and button_res_1_mask.get_at(pos_in_res_1_mask)

        pos_in_res_2_mask = pos[0] - button_res_2_rect.x, pos[1] - button_res_2_rect.y
        touching_res_2 = button_res_2_rect.collidepoint(*pos) and button_res_2_mask.get_at(pos_in_res_2_mask)

        pos_in_res_3_mask = pos[0] - button_res_3_rect.x, pos[1] - button_res_3_rect.y
        touching_res_3 = button_res_3_rect.collidepoint(*pos) and button_res_3_mask.get_at(pos_in_res_3_mask)

    if train_end:
        pos_in_button_send_create_mask = pos[0] - button_send_rect.x, pos[1] - button_send_rect.y
        touching_send = button_send_rect.collidepoint(*pos) and button_send_mask.get_at(pos_in_button_send_create_mask)

    if main_menu:
        if touching_start:
            screen.blit(button_start_hover,button_start_rect)
        else:
            screen.blit(button_start,button_start_rect)
        if touching_quit:
            screen.blit(button_quit_hover,button_quit_rect)
        else:
            screen.blit(button_quit,button_quit_rect)
    
    elif input_data:
        if touching_continue:
            screen.blit(button_continue_hover,button_continue_rect)
        else:
            screen.blit(button_continue,button_continue_rect)
        screen.blit(data_text_banner,data_text_banner_rect)
        screen.blit(name_banner,name_banner_rect)
        screen.blit(age_banner,age_banner_rect)
        screen.blit(id_banner,id_banner_rect)
        
        name_surface = base_font.render(full_name,True,(255,255,255))
        age_surface = base_font.render(age,True,(255,255,255))
        id_surface = base_font.render(identification,True,(255,255,255))
        pygame.draw.rect(screen,color_text_box_name,name_rect,200)
        pygame.draw.rect(screen,black,name_rect,2)
        screen.blit(name_surface,(name_rect.x + 10, name_rect.y + 10))

        pygame.draw.rect(screen,color_text_box_age,age_rect,200)
        pygame.draw.rect(screen,black,age_rect,2)
        screen.blit(age_surface,(age_rect.x + 10, age_rect.y + 10))

        pygame.draw.rect(screen,color_text_box_id,id_rect,200)
        pygame.draw.rect(screen,black,id_rect,2)
        screen.blit(id_surface, (id_rect.x + 10, id_rect.y + 10))
        

    elif select_train_menu:
        screen.blit(select_train_text,select_train_rect)
        if touching_one:
            screen.blit(button_one_hover,button_one_rect)
        else:
            screen.blit(button_one,button_one_rect)
        if touching_two:
            screen.blit(button_two_hover,button_two_rect)
        else:
            screen.blit(button_two,button_two_rect)

        if touching_res_1 or selected_res_1:
            screen.blit(button_res_1_hover,button_res_1_rect)
        else:
            screen.blit(button_res_1,button_res_1_rect)

        if touching_res_2 or selected_res_2:
            screen.blit(button_res_2_hover,button_res_2_rect)
        else:
            screen.blit(button_res_2,button_res_2_rect)
        
        if touching_res_3 or selected_res_3:
            screen.blit(button_res_3_hover,button_res_3_rect)
        else:
            screen.blit(button_res_3,button_res_3_rect)

    elif train_end:
        if touching_send:
            screen.blit(button_send_hover,button_send_rect)
        else:
            screen.blit(button_send,button_send_rect)

        good_flex_reps_banner = "Flexiones exitosas: "+str(good_flex_reps)
        good_ext_reps_banner = "Extensiones exitosas: "+str(good_ext_reps)
        incomplete_flex_reps_banner = "Flexiones incompletas: "+str(incomplete_flex_reps)
        incomplete_ext_reps_banner = "Extensiones incompletas: "+str(incomplete_ext_reps)
        failed_flex_reps_banner = "Flexiones fallidas: "+str(failed_flex_reps)
        failed_ext_reps_banner = "Extensiones fallidas: "+str(failed_ext_reps)
        final_timer_banner = "Tempo total: "+timer_banner+" segundos"

        screen.blit(train_end_banner,train_end_banner_rect)    
        pygame.draw.rect(screen,gray,pygame.Rect(100, 150, 500, 55),200)
        pygame.draw.rect(screen,black,pygame.Rect(100, 150, 500, 55),5)

        pygame.draw.rect(screen,gray,pygame.Rect(100, 210, 500, 55),200)
        pygame.draw.rect(screen,black,pygame.Rect(100, 210, 500, 55),5)

        pygame.draw.rect(screen,gray,pygame.Rect(100, 270, 500, 55),200)
        pygame.draw.rect(screen,black,pygame.Rect(100, 270, 500, 55),5)

        pygame.draw.rect(screen,gray,pygame.Rect(100, 330, 500, 55),200)
        pygame.draw.rect(screen,black,pygame.Rect(100, 330, 500, 55),5)

        pygame.draw.rect(screen,gray,pygame.Rect(100, 390, 500, 55),200)
        pygame.draw.rect(screen,black,pygame.Rect(100, 390, 500, 55),5)

        pygame.draw.rect(screen,gray,pygame.Rect(100, 450, 500, 55),200)
        pygame.draw.rect(screen,black,pygame.Rect(100, 450, 500, 55),5)

        pygame.draw.rect(screen,gray,pygame.Rect(100, 510, 500, 55),200)
        pygame.draw.rect(screen,black,pygame.Rect(100, 510, 500, 55),5)
        
        good_flex_surface = base_font.render(good_flex_reps_banner,True,(0,0,0))
        good_ext_surface = base_font.render(good_ext_reps_banner,True,(0,0,0))
        incomplete_flex_surface = base_font.render(incomplete_flex_reps_banner,True,(0,0,0))
        incomplete_ext_surface = base_font.render(incomplete_ext_reps_banner,True,(0,0,0))
        failed_flex_surface = base_font.render(failed_flex_reps_banner,True,(0,0,0))
        failed_ext_surface = base_font.render(failed_ext_reps_banner,True,(0,0,0))
        final_timer_surface = base_font.render(final_timer_banner,True,(0,0,0))

        screen.blit(good_flex_surface,pygame.Rect(120,160, 500, 32))
        screen.blit(good_ext_surface,pygame.Rect(120, 220, 500, 32))
        screen.blit(incomplete_flex_surface,pygame.Rect(120, 280, 500, 32))
        screen.blit(incomplete_ext_surface,pygame.Rect(120, 340, 500, 32))
        screen.blit(failed_flex_surface,pygame.Rect(120, 400, 500, 32))
        screen.blit(failed_ext_surface,pygame.Rect(120, 460, 500, 32))
        screen.blit(final_timer_surface,pygame.Rect(120, 520, 500, 32))
        
        window_ready = True

    elif play_game:
        
        input_var = funcs.data("COM3",calibVolt,calibAng)
        #print("reached 2")

        if counter_for_past_angle == 0:
            old_angle = input_var
            counter_for_past_angle += 1
        else:
            difference = abs(input_var) - abs(old_angle) 
            if difference >= 30:
                if current_movement == 'f' and input_var < old_angle:
                    direction_changed = True
                if current_movement == 'e' and input_var > old_angle:
                    direction_changed = True
            else:
                direction_changed = False

        #print("reached 2")

        t_current = time.time()
        timer = round(t_current - t_start)
        timer_banner = str(timer)
        timer_surface = base_font.render(timer_banner,True,(255,255,255))

        #print(f"counter: {counter} ")
        if counter ==3:
            collecting_data.append(input_var)
            counter_seconds += 1
            counter = 0
        else:
            counter += 1

        #print(f"counter_seconds: {counter_seconds} ")
        if counter_seconds == 29 and not data_collected:
            now = datetime.now()
            now = str(now)[:-6]
            if min(collecting_data) < 0:
                real_angle = min(collecting_data)* 34/100
            else:
                real_angle = min(collecting_data) * 159/500
            data_to_send.loc[len(data_to_send.index)] = [now,real_angle, selected_res_const * real_angle - selected_res_offset]
            data_collected = True

        if counter_seconds == 30:
            now = datetime.now()
            now = str(now)[:-6]
            if min(collecting_data) < 0:
                real_angle = max(collecting_data)* 34/100
            else:
                real_angle = max(collecting_data) * 159/500
            data_to_send.loc[len(data_to_send.index)] = [now,real_angle, selected_res_const * real_angle - selected_res_offset]
            print(data_to_send)
            data_collected = False
            collecting_data = []
            counter_seconds = 0


        pygame.draw.rect(screen,gray,timer_banner_rect,200)
        pygame.draw.rect(screen,black,timer_banner_rect,2)

        pygame.draw.rect(screen,gray,next_cup_green_rect,200)
        pygame.draw.rect(screen,black,next_cup_green_rect,15)
        pygame.draw.rect(screen,black,pygame.Rect(next_cup_green_rect.x + 40,0,6,10),15)
        pygame.draw.rect(screen,black,pygame.Rect(next_cup_green_rect.x + 100,0,6,10),15)

        pygame.draw.rect(screen,gray,pygame.Rect(face_happy_rect.x-10, face_happy_rect.y-10, face_happy_rect.width + 20, face_happy_rect.height + 20),200)
        pygame.draw.rect(screen,black,pygame.Rect(face_happy_rect.x-10, face_happy_rect.y-10, face_happy_rect.width + 20, face_happy_rect.height + 20),15)
        pygame.draw.rect(screen,black,pygame.Rect(face_happy_rect.x + 30,0,6,10),15)
        pygame.draw.rect(screen,black,pygame.Rect(face_happy_rect.x + 90,0,6,10),15)

        screen.blit(timer_surface,(timer_banner_rect.x + 75, timer_banner_rect.y + 10))
        screen.blit(clock_pic,clock_pic_rect)
        

        try:
            current_movement = saved_train[0]
        except:
            train_end = True
            play_game = False
            
        if current_happiness >= 75:
            screen.blit(face_happy,face_happy_rect)
        elif current_happiness >= 50:
            screen.blit(face_reg,face_reg_rect)
        elif current_happiness >= 25:
            screen.blit(face_serious,face_serious_reg)
        else:
            screen.blit(face_sad,face_sad_reg)

        if rep_fail:
            highest_stage = 'start'
            screen.blit(wrong_rep,wrong_rep_rect)
            screen.blit(machine_off,machine_off_rect)
            if abs(input_var) < 10:
                if current_movement == "f": failed_flex_reps += 1
                elif current_movement == "e": failed_ext_reps += 1
                current_happiness -= happiness_weight
                try:
                    saved_train.pop(0)
                except:
                    train_end = True
                rep_incomplete = False
                idle = False
                active = False
                midway = False
                done = False
                rep_fail = False
                rep_complete = False
                start = True
            
        elif rep_complete:
            highest_stage = 'start'
            screen.blit(good_rep,good_rep_rect)
            screen.blit(machine_off,machine_off_rect)
            if abs(input_var) < 10:
                if current_movement == "f": good_flex_reps += 1
                elif current_movement == "e": good_ext_reps += 1
                if current_happiness < 100-happiness_weight: current_happiness += happiness_weight/2
                try:
                    saved_train.pop(0)
                except:
                    train_end = True
                    play_game = False
                rep_incomplete = False
                idle = False
                active = False
                midway = False
                done = False
                rep_fail = False
                rep_complete = False
                start = True

        elif rep_incomplete:
            highest_stage = 'start'
            screen.blit(wrong_rep,wrong_rep_rect)
            screen.blit(machine_off,machine_off_rect)
            if abs(input_var) < 10:
                if current_movement == "f": incomplete_flex_reps += 1
                elif current_movement == "e": incomplete_ext_reps += 1
                current_happiness -= happiness_weight/2
                try:
                    saved_train.pop(0)
                except:
                    train_end = True
                    time.sleep(0.5)
                rep_incomplete = False
                idle = False
                active = False
                midway = False
                done = False
                rep_fail = False
                rep_complete = False
                start = True

        else:
            if current_movement == "f" and not (rep_complete or rep_fail or rep_incomplete):
                screen.blit(next_cup_red,(next_cup_red_rect.x, next_cup_red_rect.y - 5))
            elif current_movement == "e" and not (rep_complete or rep_fail or rep_incomplete):
                screen.blit(next_cup_green,(next_cup_green_rect.x, next_cup_green_rect.y - 5))
            
            if current_movement == 'f':
                if input_var <= -30:
                    rep_fail = True
                    print("Fallo por flexion")
            if current_movement == 'e':
                if input_var >= 30:
                    rep_fail = True
                    print("Fallo por extension")

            if abs(input_var) <= 20 and not (rep_complete or rep_fail) and not midway and start:
                idle = True
                active = False
                midway = False
                done = False
                rep_complete = False
                if abs(input_var) == 25:
                    highest_stage = 'first'
            elif 25 <= abs(input_var) <= 45 and not (rep_complete or rep_fail or direction_changed) and not active:
                start = False
                idle = False
                midway = True
                active = False
                done = False
                rep_complete = False
                if abs(input_var) == 45:
                    highest_stage = 'mid'
            elif 45 <= abs(input_var) <= 70 and not (rep_complete or rep_fail or direction_changed) and not done:
                active = True
                midway = False
                idle = False
                done = False
                rep_complete = False
                if abs(input_var) == 70:
                    highest_stage = 'top'

            elif 70 <=  abs(input_var) <= 90 and not (rep_complete or rep_fail or direction_changed):
                active = False
                midway = False
                idle = False
                done = True
                rep_complete = False

                 
            elif 90 < abs(input_var) and not direction_changed and done:
                active = False
                midway = False
                idle = False
                done = False
                rep_complete = True
            
            elif not rep_complete and not rep_fail and not start:
                active = False
                midway = False
                idle = False
                done = False
                rep_incomplete = True
    
            if idle:
                screen.blit(machine_idle,machine_idle_rect)
                screen.blit(empty_cup,empty_cup_rect)
            if midway:
                screen.blit(machine_mid,machine_mid_rect)
                if input_var > 0: screen.blit(red_cup_30,red_cup_30_rect)
                if input_var < 0: screen.blit(green_cup_30,green_cup_30_rect)
            if active:
                if 0 < input_var: screen.blit(red_cup_60,red_cup_60_rect)
                if input_var < 0: screen.blit(green_cup_60,green_cup_60_rect)
                screen.blit(machine_full,machine_full_rect)
            if done:
                if 0 < input_var: screen.blit(red_cup,red_cup_rect)
                if input_var < 0: screen.blit(green_cup,green_cup_rect)
                screen.blit(machine_full,machine_full_rect) 

    pygame.display.update()
    clock.tick(60)
