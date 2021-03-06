from tkinter import *
from tkinter import messagebox
import pygame, sys, linecache, time
from pygame.locals import*

Tk().wm_withdraw() #to hide the main window

def printf(string):
    with open("Responses.txt", "a") as file:
        file.write(string)
    print(string)
    messagebox.showinfo('', string)

pygame.init()

start_time = time.time()

black = (0, 0, 0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
pink = (255,200,200)

screen = pygame.display.set_mode((1400, 600))
pygame.display.set_caption("Getting-To-Know-You Study")
screen.fill(black)
start = time.time()


while True:
    pygame.draw.line(screen, green, [0, 0], [1400, 0], 5)
    pygame.draw.line(screen, green, [0, 200], [1400, 200], 5)
    pygame.draw.line(screen, green, [0, 400], [1400, 400], 5)
    pygame.draw.line(screen, green, [0, 600], [1400, 600], 5)
    pygame.draw.line(screen, green, [0, 0], [1200, 0], 5)
    pygame.draw.line(screen, green, [200, 0], [200, 600], 5)
    pygame.draw.line(screen, green, [400, 0], [400, 600], 5)
    pygame.draw.line(screen, green, [600, 0], [600, 600], 5)
    pygame.draw.line(screen, green, [800, 0], [800, 600], 5)
    pygame.draw.line(screen, green, [1200, 0], [1200, 600], 5)
    pygame.draw.line(screen, green, [0, 0], [0, 600], 5)
    pygame.draw.line(screen, green, [1000, 0], [1000, 600], 5)
    pygame.draw.line(screen, green, [1400, 0], [1400, 600], 5)

    Rect1 = pygame.draw.rect(screen, (40, 10, 10), (10, 10, 180, 180))
    Rect2 = pygame.draw.rect(screen, (40, 10, 10), (10, 210, 180, 180))
    Rect3 = pygame.draw.rect(screen, (40, 10, 10), (10, 410, 180, 180))
    Rect4 = pygame.draw.rect(screen, (40, 10, 10), (210, 10, 180, 180))
    Rect5 = pygame.draw.rect(screen, (40, 10, 10), (210, 210, 180, 180))
    Rect6 = pygame.draw.rect(screen, (40, 10, 10), (210, 410, 180, 180))
    Rect7 = pygame.draw.rect(screen, (40, 10, 10), (410, 10, 180, 180))
    Rect8 = pygame.draw.rect(screen, (40, 10, 10), (410, 210, 180, 180))
    Rect9 = pygame.draw.rect(screen, (40, 10, 10), (410, 410, 180, 180))
    Rect10 = pygame.draw.rect(screen, (40, 10, 10), (610, 10, 180, 180))
    Rect11 = pygame.draw.rect(screen, (40, 10, 10), (610, 210, 180, 180))
    Rect12 = pygame.draw.rect(screen, (40, 10, 10), (610, 410, 180, 180))
    Rect13 = pygame.draw.rect(screen, (40, 10, 10), (810, 10, 180, 180))
    Rect14 = pygame.draw.rect(screen, (40, 10, 10), (810, 210, 180, 180))
    Rect15 = pygame.draw.rect(screen, (40, 10, 10), (810, 410, 180, 180))
    Rect16 = pygame.draw.rect(screen, (40, 10, 10), (1010, 10, 180, 180))
    Rect17 = pygame.draw.rect(screen, (40, 10, 10), (1010, 210, 180, 180))
    Rect18 = pygame.draw.rect(screen, (40, 10, 10), (1010, 410, 180, 180))
    Rect19 = pygame.draw.rect(screen, (40, 10, 10), (1210, 10, 180, 180))
    Rect20 = pygame.draw.rect(screen, (40, 10, 10), (1210, 210, 180, 180))
    Rect21 = pygame.draw.rect(screen, (40, 10, 10), (1210, 410, 180, 180))
    
    sys_font = pygame.font.SysFont("None", 30)
    rendered = sys_font.render('Wants Marriage', 0, (80, 200, 80))
    screen.blit(rendered, (20, 40))
    rendered2 = sys_font.render('Religiosity', 0, (80, 200, 80))
    screen.blit(rendered2, (40, 240))
    rendered3 = sys_font.render('Political', 0, (80, 200, 80))
    screen.blit(rendered3, (55, 440))
    rendered4 = sys_font.render('Wants Children', 0, (80, 200, 80))
    screen.blit(rendered4, (230, 40))
    rendered5 = sys_font.render('Likely to Move', 0, (80, 200, 80))
    screen.blit(rendered5, (230, 240))
    rendered6 = sys_font.render('Away', 0, (80, 200, 80))
    screen.blit(rendered6, (265, 260))
    rendered7 = sys_font.render('Urban/Rural', 0, (80, 200, 80))
    screen.blit(rendered7, (240, 440))
    rendered8 = sys_font.render('Preferences', 0, (80, 200, 80))
    screen.blit(rendered8, (240, 460))
    rendered9 = sys_font.render('Importance of Sex', 0, (80, 200, 80))
    screen.blit(rendered9, (420, 40))
    rendered10 = sys_font.render('Ideal Sex', 0, (80, 200, 80))
    screen.blit(rendered10, (450, 240))
    rendered11 = sys_font.render('Frequency', 0, (80, 200, 80))
    screen.blit(rendered11, (440, 260))
    rendered12 = sys_font.render('Importance of', 0, (80, 200, 80))
    screen.blit(rendered12, (435, 440))
    rendered13 = sys_font.render('Physical Attraction', 0, (80, 200, 80))
    screen.blit(rendered13, (410, 460))
    rendered14 = sys_font.render('Orientation', 0, (80, 200, 80))
    screen.blit(rendered14, (30, 460))
    rendered15 = sys_font.render('Alcohol', 0, (80, 200, 80))
    screen.blit(rendered15, (665, 40))
    rendered16 = sys_font.render('Frequency', 0, (80, 200, 80))
    screen.blit(rendered16, (650, 60))
    rendered17 = sys_font.render('Hobbies', 0, (80, 200, 80))
    screen.blit(rendered17, (660, 240))
    rendered18 = sys_font.render('Marijuana', 0, (80, 200, 80))
    screen.blit(rendered18, (650, 440))
    rendered19 = sys_font.render('Frequency', 0, (80, 200, 80))
    screen.blit(rendered19, (645, 460))
    rendered20 = sys_font.render('Novelty', 0, (80, 200, 80))
    screen.blit(rendered20, (860, 40))
    rendered21 = sys_font.render('Seeking', 0, (80, 200, 80))
    screen.blit(rendered21, (860, 60))
    rendered22 = sys_font.render('Activity Level', 0, (80, 200, 80))
    screen.blit(rendered22, (835, 240))
    rendered23 = sys_font.render('Jealousy', 0, (80, 200, 80))
    screen.blit(rendered23, (850, 440))
    rendered24 = sys_font.render('Communication', 0, (80, 200, 80))
    screen.blit(rendered24, (1030, 40))
    rendered25 = sys_font.render('Financial Style', 0, (80, 200, 80))
    screen.blit(rendered25, (1030, 240))
    rendered26 = sys_font.render('Division of', 0, (80, 200, 80))
    screen.blit(rendered26, (1040, 440))
    rendered27 = sys_font.render('Household Labor', 0, (80, 200, 80))
    screen.blit(rendered27, (1020, 460))
    rendered28 = sys_font.render('Home Tidiness', 0, (80, 200, 80))
    screen.blit(rendered28, (1230, 40))
    rendered29 = sys_font.render('Cat Attitudes', 0, (80, 200, 80))
    screen.blit(rendered29, (1230, 240))
    rendered30 = sys_font.render('Dog Attitudes', 0, (80, 200, 80))
    screen.blit(rendered30, (1230, 440))
    
    pygame.draw.rect(screen, (255, 0, 0), (60, 100, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (60, 300, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (60, 500, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (280, 100, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (280, 300, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (280, 500, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (480, 100, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (480, 300, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (480, 500, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (680, 100, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (680, 300, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (680, 500, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (880, 100, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (880, 300, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (880, 500, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (1080, 100, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (1080, 300, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (1080, 500, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (1280, 100, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (1280, 300, 60, 60))
    pygame.draw.rect(screen, (255, 0, 0), (1280, 500, 60, 60))

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type != pygame.MOUSEBUTTONUP:
            continue
        
        pos = pygame.mouse.get_pos()
        
        if Rect1.collidepoint(pos):
            marriage = linecache.getline("Responses.txt", 5)
            printf("To the question, \"Do you plan on getting married someday?\"\n 1 = Definitely not \n 2 = Probably not \n 3 = Maybe/Unsure \n 4 = Probably \n 5 = Definitely\"\n your partner responded:\n" + marriage)
        if Rect2.collidepoint(pos):
            religion = linecache.getline("Responses.txt", 12)
            printf("To the question, \"How religious are you? \n 1 = Not at all religious \n 2 = A little bit religious \n 3 = Somewhat religious \n 4 = Quite religious\" \n 5 = Deeply religious ,\n your partner responde:\n " + religion)
        if Rect4.collidepoint(pos):
            printf("To the question, \"Do you plan to have children someday? \n 1 = Definitely not \n 2 = Probably not \n 3 = Maybe/Unsure \n 4 = Probably \n 5 = Definitely\" \n your partner responded: \n ")
            children = linecache.getline("Responses.txt", 6)
            printf(children)
        if Rect7.collidepoint(pos):
            importancesex = linecache.getline("Responses.txt", 7)
            printf("To the question, \"How important is sex to you in a relationship? \n 1 = Not at all important \n 2 = A little important \n 3 = Somewhat important \n 4 = Very Important \n 5 = Extremely Important\" \n your partner responded: \n" + importancesex)
        if Rect10.collidepoint(pos):
            alcohol = linecache.getline("Responses.txt", 8)
            printf("To the question, \"How often do you prefer to drink alcohol? \n 1 = Never \n 2 = A few times a year \n 3 = A few times a month \n 4 = Once a week \n 5 = Daily \"\n your partner responded: \n" + alcohol)
        if Rect13.collidepoint(pos):
            novelty = linecache.getline("Responses.txt", 9)
            printf("To the question, \"How much do you typically enjoy trying new things? \n 1 = Nearly always dislike \n 2 = Usually dislike \n 3 = It depends \n 4 = Usually enjoy \n 5 = Nearly always enjoy\" \n your partner responded: \n" + novelty)
        if Rect16.collidepoint(pos):
            communication = linecache.getline("Responses.txt", 10)
            printf("To the quesstion, \"When you have a disagreement with someone, how soon do you prefer to discuss it with them? \n 1 = Never discuss \n 2 = Discuss eventually, if problem does not resolve on its own \n 3 = Discuss soon, after brief cooling off \n 4 = Discuss immediately\" \n your partner responded: \n" + communication)
        if Rect19.collidepoint(pos):
            tidy = linecache.getline("Responses.txt", 11)
            printf("To the question, \"How tidy do you typically keep your home? \n 1 = Very messy \n 2 = Somewhat Messy \n 3 = Neither messy nor tidy \n 4 = Somewhat tidy \n 5 = Very tidy\" your partner responded: \n" + tidy)
        if Rect5.collidepoint(pos):
            move = linecache.getline("Responses.txt", 13)
            printf("To the question, \"Do you plan to move out of Ontario someday?\n 1 = Definitely not \n 2 = Probably not \n 3 = Maybe/Unsure \n 4 = Probably \n 5 = Definitely\" your partner responded: \n" + move)
        if Rect8.collidepoint(pos):
            freq = linecache.getline("Responses.txt", 14)
            printf("To the question, \"What is your ideal sexual frequency in a relationship? \n 1 = Never or almost never \n 2 = Once a month \n 3 = A few times a month \n 4 = Once a week \n 5 =  Twice a week \n 6 = A few times a week \n 7 = Daily \n\" your partner responded: \n" + freq)
        if Rect9.collidepoint(pos):
            attraction = linecache.getline("Responses.txt", 21)
            printf("To the question, \"In a relationship, how important is physical attraction to you? \n 1 = Not at all important \n 2 = Slightly important \n 3 = Moderately important \n 4 = Very important \n 5 = Extremely important \"\n your partner responded: \n" + attraction)
        if Rect11.collidepoint(pos):
            hobbies = linecache.getline("Responses.txt", 15)
            printf("To the question, \"What are your favorite hobbies? Please list up to three\"\n your partner responded: \n" + hobbies)
        if Rect14.collidepoint(pos):
            activity = linecache.getline("Responses.txt", 16)
            printf("To the question, \"How much free time do you spend being active (i.e., out doing things) versus passive (e.g., TV, videogames)? \n 1 = Almost all passive \n 2 = More passive than active \n 3 = 50/50 \n 4 = More active than passive \n 5 = Almost all active\"\n your partner responded: \n" + activity)
        if Rect17.collidepoint(pos):
            finance = linecache.getline("Responses.txt", 17)
            printf("To the question, \"When you have extra cash, what do you prefer to do with it? \n 1 = Save it all \n 2 = Save most of it \n 3 = Save some, spend some \n 4 = Spend most of it \n 5 = Spend it all\"\n your partner responded: \n" + finance)
        if Rect20.collidepoint(pos):
            cat = linecache.getline("Responses.txt", 18)
            printf("To the question, \"How do you feel about having a pet cat? \n 1 = Extremely negative \n 2 = Somewhat negative \n 3 = Neither positive nor negative \n 4 = Somewhat positive \n 5 = Extremely positive\"\n your partner responded: \n" + cat)
        if Rect3.collidepoint(pos):
            politics = linecache.getline("Responses.txt", 19)
            printf("To the question, \"What is your political orientation? \n 1 = Extremely Conservative \n 2 = very conservative \n 3 = somewhat conservsative \n 4 = Not conservative nor libeal \n 5 = Somewhat liberal \n 6 = Very liberal \n 7 = Extremely liberal\"\n your partner responded: \n" + politics)
        if Rect6.collidepoint(pos):
            urban = linecache.getline("Responses.txt", 20)
            printf("To the question, \"How urban versus rural is your ideal neighbourhood?\n 1 = Very rural (in the boonies) \n 2 = Somewhat rural (small town) \n 3 = Both (suburbs) \n 4 = Somewhat urban (small city) \n 5 = Very urban (big city)\"\n your partner responded: \n" + urban)
        if Rect12.collidepoint(pos):
            weed = linecache.getline("Responses.txt", 22)
            printf("To the question, \"How often do you prefer to use cannabis recreationally? \n 1 = Never \n 2 = A few times a year \n 3 = Once a month \n 4 = A few times a month \n 5 = Once a week \n 6 = A few times a week \n 7 = Daily \"\n your partner responded: \n" + weed)
        if Rect18.collidepoint(pos):
            labor = linecache.getline("Responses.txt", 24)
            printf("To the question, \"How important is it to you tht household tasks are equally shared in a relationship? \n 1 = Not at all important \n 2 = Slightly important \n 3 = Moderately important \n 4 = Very important \n 5 = Extremely important\"\n your partner responded: \n" + labor)
        if Rect21.collidepoint(pos):
            dog = linecache.getline("Responses.txt", 25)
            printf("To the question, \"How do you feel about having a pet dog? \n 1 = Extremely negative \n 2 = Somewhat negative \n 3 = Neither positive nor negative \n 4 = Somewhat positive \n 5 = Extremely positive\"\n your partner responded: \n" + dog)
        if Rect15.collidepoint(pos):
            jealousy = linecache.getline("Responses.txt", 23)
            printf("To the question, \"Do you consider yourself to be a jealous person, romantically? \n 1 = Never jealous \n 2 = Rarely jealous \n 3 = Sometimes jealous \n 4 = Often jealous \n 5 = Always jealous\"\n your partner responded: \n" + jealousy)

        end = time.time() - start
        timing = "Selection took you " + str(end) + "seconds. \n"
        with open("Responses.txt", "a") as file:
            file.write(timing)
        print(timing)
        
