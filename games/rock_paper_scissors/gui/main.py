import os
import random

import pygame

pygame.init()
pygame.font.init()

r = "rock"
p = "paper"
s = "scissor"
    
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rock Paper Scissors")


# Background image
source_dir = os.path.dirname(os.path.abspath(__file__))
bg_path = os.path.join(source_dir, 'assets/bg1.jpg')
bg = pygame.image.load(bg_path).convert()

# Rock button image
r_path = os.path.join(source_dir, 'assets/br.png')
r_i = pygame.image.load(r_path)
r_i = pygame.transform.scale(r_i, (r_i.get_rect().width*0.25, r_i.get_rect().height*0.25))

# Paper button image
p_path = os.path.join(source_dir, 'assets/bp.png')
p_i = pygame.image.load(p_path)
p_i = pygame.transform.scale(p_i, (p_i.get_rect().width*0.25, p_i.get_rect().height*0.25))

# Scissor button image
s_path = os.path.join(source_dir, 'assets/bs.png')
s_i = pygame.image.load(s_path)
s_i = pygame.transform.scale(s_i, (s_i.get_rect().width*0.25, s_i.get_rect().height*0.25))

font_path = os.path.join(source_dir, 'assets/ComicSans.ttf')
score_font = pygame.font.Font(font_path,25)
user_score_label = score_font.render("Your Score 0", True, (255, 235, 193))
computer_score_label = score_font.render("Comp Score 0", True, (255, 235, 193))

# Welcome message
font = pygame.font.Font(font_path, 25)
play_message = font.render("Welcome to Rock Paper Scissor Game", True, (255, 235, 193))
play_message2 = font.render("Pick you Weapon to start playing", True, (255, 235, 193))

# Result message
result_tie = font.render("It's a Tie", True, (255, 235, 193))
result_win = font.render("You Won..!!", True, (124, 252, 0))
result_loss = font.render("You Lost..", True, (255, 0, 0))

rock_rect = r_i.get_rect(topleft=(25, 280))
paper_rect = r_i.get_rect(topleft=(225, 280))
scissor_rect = r_i.get_rect(topleft=(425, 280))

rock_path = os.path.join(source_dir, 'assets/rock.png')
rock = pygame.image.load(rock_path)
paper_path = os.path.join(source_dir, 'assets/paper.png')
paper = pygame.image.load(paper_path)
scissor_path = os.path.join(source_dir, 'assets/scissor.png')
scissor = pygame.image.load(scissor_path)

all_choices = [rock, paper, scissor]
all_choices_text = ["R","P", "S"]


user_choice = None
computer_choice = None
user_has_weapon = False

is_show_weapon = False

user_text = None
computer_text = None
result_msg = None

user_score_cnt = 0
computer_score_cnt = 0

def weapon_choice(user_idx:int):
    global is_running, user_choice, computer_choice,user_has_weapon, is_show_weapon, user_text, computer_text
    is_running =True
    user_choice = all_choices[user_idx]
    user_text = all_choices_text[user_idx]
    user_has_weapon = True
    is_show_weapon = False
    idx =random.randint(0,2)
    computer_choice = all_choices[idx]
    computer_text = all_choices_text[idx]




is_running = False
dead=False
while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rock_rect.collidepoint(event.pos):
                # print("rock")
                weapon_choice(0)
            if paper_rect.collidepoint(event.pos):
                # print("paper")
                weapon_choice(1)
            if scissor_rect.collidepoint(event.pos):
                # print("scissor")
                weapon_choice(2)

    screen.blit(bg, [0, 0])
    screen.blit(user_score_label, (50,20))
    screen.blit(computer_score_label, (320,20))

    if is_running is False:
        screen.blit(play_message, (100, 170))
        screen.blit(play_message2, (120, 200))
    
    if is_show_weapon:
        screen.blit(user_choice,(60, 70))
        screen.blit(computer_choice,(400, 70))
        screen.blit(result_msg,(250, 50))
        user_has_weapon = False 

    
    if user_has_weapon:
        is_show_weapon = True
        if computer_text == user_text:
            result_msg = result_tie
        elif (user_text == "R" and computer_text == "S") or (user_text == "P" and computer_text == "R") or (user_text == "S" and computer_text == "P"):
            result_msg = result_win
            user_score_cnt += 1
        else:
            result_msg = result_loss
            computer_score_cnt += 1
        
        user_score_label = font.render("Your score " + str(user_score_cnt), True,(255, 235, 193))
        computer_score_label = font.render("Computer score " + str(computer_score_cnt), True,(255, 235, 193))
        

    screen.blit(r_i,rock_rect)
    screen.blit(p_i,paper_rect)
    screen.blit(s_i,scissor_rect)

    pygame.display.update()
    clock.tick(60)

