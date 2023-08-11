import pygame
import funcs
import random
import time
from sys import exit

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

button_create = pygame.image.load('graphics/button_create.png').convert_alpha()
button_create = pygame.transform.scale(button_create, (button_create.get_width()/2.2,button_create.get_height()/2.2))
button_create_hover = pygame.image.load('graphics/button_create_hover.png').convert_alpha()
button_create_hover = pygame.transform.scale(button_create_hover, (button_create_hover.get_width()/2.2,button_create_hover.get_height()/2.2))
button_create_mask = pygame.mask.from_surface(button_create)
button_create_rect = button_create.get_rect(topright = (1000,200))

button_continue = pygame.image.load('graphics/continue.png').convert_alpha()
button_continue = pygame.transform.scale(button_continue, (button_continue.get_width()/2,button_continue.get_height()/2))
button_continue_hover = pygame.image.load('graphics/continue_hover.png').convert_alpha()
button_continue_hover = pygame.transform.scale(button_continue_hover, (button_continue_hover.get_width()/2,button_continue_hover.get_height()/2))
button_continue_mask = pygame.mask.from_surface(button_continue)
button_continue_rect = button_continue.get_rect(midtop = (540,530))

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

data_text_banner = pygame.image.load('graphics/data_text_2.png').convert_alpha()
data_text_banner = pygame.transform.scale(data_text_banner, (data_text_banner.get_width()/2.8,data_text_banner.get_height()/2.8))
data_text_banner_rect = data_text_banner.get_rect(midtop = (540, 5))

name_banner = pygame.image.load('graphics/Name.png').convert_alpha()
name_banner = pygame.transform.scale(name_banner, (name_banner.get_width()/2.8,name_banner.get_height()/2.8))
name_banner_rect = name_banner.get_rect(midtop = (160, 100))

id_banner = pygame.image.load('graphics/ID.png').convert_alpha()
id_banner = pygame.transform.scale(id_banner, (id_banner.get_width()/2.8,id_banner.get_height()/2.8))
id_banner_rect = id_banner.get_rect(midtop = (160, 400))

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

name_rect = pygame.Rect(350,157,500,60)
id_rect = pygame.Rect(350,457,500,60)

main_menu = True
input_data = False
create_train_menu = False

text_box_1 = True
text_box_2 = False
text_box_3 = False
text_box_4 = False

text_name = True
text_id = False

color_text_box_1 = lightblue
color_text_box_2 = gray
color_text_box_3 = gray
color_text_box_4 = gray

color_text_box_name = lightblue
color_text_box_id = gray

saved_train = []

def close_game():
    pygame.quit
    exit()

while True:
    screen.blit(background,(0,0))
    pos = pygame.mouse.get_pos()
    
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
                if pygame.mouse.get_pressed()[0] and touching_continue and not(full_name == '' or identification == '' or len(identification) != 9):
                    input_data = False
                    create_train_menu = True
                    funcs.NChanel(identification,full_name)
                    channel_id = funcs.chanelID(identification)
                    channel_apikey = funcs.chanelAPIKEY(channel_id)

                
                if name_rect.collidepoint(event.pos):
                    text_name = True
                    text_id = False

                    color_text_box_name = lightblue
                    color_text_box_id = gray

                elif id_rect.collidepoint(event.pos):
                    text_name = False
                    text_id = True

                    color_text_box_name = gray
                    color_text_box_id = lightblue
                
            elif create_train_menu:
                if pygame.mouse.get_pressed()[0] and touching_create:
                    if complete_flex == '':
                        complete_flex = '0'
                    if complete_ext == '':
                        complete_ext = '0'
                    '''
                    if partial_flex == '':
                        partial_flex = '0'
                    if partial_ext == '':
                        partial_ext = '0'
                    '''
                    saved_train.append(int(complete_flex))
                    saved_train.append(int(complete_ext))
                    
                    funcs.UploadDataF(channel_apikey,int(complete_flex),int(complete_ext))

                    create_train_menu = False
                    main_menu = True


                    try:
                        happiness_weight = funcs.set_weights(saved_train)
                    except:
                        pass
                    create_train_menu = False
                    select_train_menu = True
                
                if complete_flex_rect.collidepoint(event.pos):
                    text_box_1 = True
                    text_box_2 = False
                    text_box_3 = False
                    text_box_4 = False

                    color_text_box_1 = lightblue
                    color_text_box_2 = gray
                    color_text_box_3 = gray
                    color_text_box_4 = gray

                elif complete_ext_rect.collidepoint(event.pos):
                    text_box_1 = False
                    text_box_2 = False
                    text_box_3 = True
                    text_box_4 = False

                    color_text_box_1 = gray
                    color_text_box_2 = gray
                    color_text_box_3 = lightblue
                    color_text_box_4 = gray
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                close_game()
            if event.key == pygame.K_BACKSPACE and input_data:
                if text_name:
                    full_name = full_name[:-1]
                elif text_id:
                    identification = identification[:-1]
            if (event.unicode.isalpha() or event.key == pygame.K_SPACE) and input_data:
                if text_name and len(full_name) <= 20:
                    full_name += event.unicode
            if event.unicode.isnumeric() and input_data:
                if text_id and len(identification) <= 8:
                    identification += event.unicode
            if event.key == pygame.K_BACKSPACE and create_train_menu:
                if text_box_1:
                    complete_flex = complete_flex[:-1]
                elif text_box_3:
                    complete_ext = complete_ext[:-1]
            elif event.unicode.isnumeric() and create_train_menu:
                if text_box_1 and len(complete_flex) <= 1:
                    complete_flex += event.unicode
                elif text_box_3 and len(complete_ext) <= 1:
                    complete_ext += event.unicode

    if main_menu:
        pos_in_button_start_mask = pos[0] - button_start_rect.x, pos[1] - button_start_rect.y
        touching_start = button_start_rect.collidepoint(*pos) and button_start_mask.get_at(pos_in_button_start_mask)

        pos_in_button_quit_mask = pos[0] - button_quit_rect.x, pos[1] - button_quit_rect.y
        touching_quit = button_quit_rect.collidepoint(*pos) and button_quit_mask.get_at(pos_in_button_quit_mask)

        if touching_start:
            screen.blit(button_start_hover,button_start_rect)
        else:
            screen.blit(button_start,button_start_rect)
        if touching_quit:
            screen.blit(button_quit_hover,button_quit_rect)
        else:
            screen.blit(button_quit,button_quit_rect)

    if input_data:
        pos_in_button_continue_mask = pos[0] - button_continue_rect.x, pos[1] - button_continue_rect.y
        touching_continue = button_continue_rect.collidepoint(*pos) and button_continue_mask.get_at(pos_in_button_continue_mask)

        if touching_continue:
            screen.blit(button_continue_hover,button_continue_rect)
        else:
            screen.blit(button_continue,button_continue_rect)
        screen.blit(data_text_banner,data_text_banner_rect)
        screen.blit(name_banner,name_banner_rect)
        screen.blit(id_banner,id_banner_rect)
        
        name_surface = base_font.render(full_name,True,(255,255,255))
        id_surface = base_font.render(identification,True,(255,255,255))
        pygame.draw.rect(screen,color_text_box_name,name_rect,200)
        pygame.draw.rect(screen,black,name_rect,2)
        screen.blit(name_surface,(name_rect.x + 10, name_rect.y + 10))


        pygame.draw.rect(screen,color_text_box_id,id_rect,200)
        pygame.draw.rect(screen,black,id_rect,2)
        screen.blit(id_surface, (id_rect.x + 10, id_rect.y + 10))

    if create_train_menu:
        pos_in_button_create_mask = pos[0] - button_create_rect.x, pos[1] - button_create_rect.y
        touching_create = button_create_rect.collidepoint(*pos) and button_create_mask.get_at(pos_in_button_create_mask)

        if touching_create:
            screen.blit(button_create_hover,button_create_rect)
        else:
            screen.blit(button_create,button_create_rect)

        screen.blit(banner_complete_flex,banner_complete_flex_rect)
        #screen.blit(banner_partial_flex,banner_partial_flex_rect)
        screen.blit(banner_complete_ext,banner_complete_ext_rect)
        #screen.blit(banner_partial_ext,banner_partial_ext_rect)

        text_surface_comp_flex = base_font.render(complete_flex,True,(255,255,255))
        pygame.draw.rect(screen,color_text_box_1,complete_flex_rect,200)
        pygame.draw.rect(screen,black,complete_flex_rect,2)
        screen.blit(text_surface_comp_flex,(complete_flex_rect.x + 10, complete_flex_rect.y + 10))

        text_surface_comp_ext = base_font.render(complete_ext,True,(255,255,255))
        pygame.draw.rect(screen,color_text_box_3,complete_ext_rect,200)
        pygame.draw.rect(screen,black,complete_ext_rect,2)
        screen.blit(text_surface_comp_ext,(complete_ext_rect.x + 10, complete_ext_rect.y + 10))

    pygame.display.update()
    clock.tick(60)