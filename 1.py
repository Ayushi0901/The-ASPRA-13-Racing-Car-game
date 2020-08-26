import pygame
import time
import random
pygame.init()       
purple=(52, 46, 87)                                             #initiate the window 
black=(0,0,0)
yellow=(224, 203, 63)                                             
red=(255,0,0)
blue=(41, 110, 150 )
green=(0, 200, 0)
bright_red=(255,0,0)
bright_blue=(0, 0,255)
bright_green=(0,255,0)
display_width=900                                       #width and height of window
display_height=600



gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The ASPRA 13 Racing Road')             #Name of the game
clock=pygame.time.Clock()                                          #for all the intervals in game
carimg=pygame.image.load("car2.png")
backgroundpic=pygame.image.load("left.png")
backgroundpic1=pygame.image.load("right.png")
white_strip=pygame.image.load("whitestrip.jpg")
strip=pygame.image.load("strip.jpg")
intro_bg=pygame.image.load("dp.jpg")
instruct_bg=pygame.image.load("back.jpg")
car_width = 50
pause=True

def  intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_bg,(0,0))
        largetext=pygame.font.Font("freesansbold.ttf",50)
        textSurf,textRect=text_objects("ASPRA 13 Racing Road",largetext)
        textRect.center=(500,100)
        gamedisplays.blit(textSurf,textRect)
        button("START",100,350,110,35,green,bright_green,"play")
        button("QUIT",400,400,120,40,red,bright_red,"quit")
        button("INSTRUCTION",700,450,150,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)    

def  button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and  y+h > mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if click[0]==1 and action !=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()    
            elif action=="unpause":
                unpaused()    

    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)                        

def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruct_bg,(0,0))
        largetext=pygame.font.Font("freesansbold.ttf",50)
        mediumtext=pygame.font.Font("freesansbold.ttf",35)
        smalltext=pygame.font.Font("freesansbold.ttf",20)
        textsurf, textrect=text_objects("this the car game in which you need to dodge the coming cars",smalltext)
        textrect.center=((300),(150))
        textsurf, textrect=text_objects("Instruction",largetext)
        textrect.center=((450),(100))
        gamedisplays.blit(textsurf,textrect)
        ftextsurf, ftextrect=text_objects("ARROW LEFT : LEFT TURN",smalltext)
        ftextrect.center=((150),(300))
        htextsurf, htextrect=text_objects("ARROW RIGHT : RIGHT TURN",smalltext)
        htextrect.center=((150),(350))
        atextsurf, atextrect=text_objects("A : ACCELERATOR",smalltext)
        atextrect.center=((150),(400))
        rtextsurf, rtextrect=text_objects("B : BRAKE",smalltext)
        rtextrect.center=((150),(450))
        ptextsurf, ptextrect=text_objects("P : PAUSE",smalltext)
        ptextrect.center=((150),(500))
        stextsurf, stextrect=text_objects("CONTROLS",mediumtext)
        stextrect.center=((450),(170))
        gamedisplays.blit(ftextsurf,ftextrect)
        gamedisplays.blit(stextsurf,stextrect)
        gamedisplays.blit(htextsurf,htextrect)
        gamedisplays.blit(atextsurf,atextrect)
        gamedisplays.blit(rtextsurf,rtextrect)
        gamedisplays.blit(ptextsurf,ptextrect)
        button("BACK",700,500,120,40,red,bright_red,"menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruct_bg,(0,0))
        largetext=pygame.font.Font("freesansbold.ttf",80)
        textSurf,textRect=text_objects("PAUSED",largetext)
        textRect.center=((display_width/2),(display_height/2))
        gamedisplays.blit(textSurf,textRect)
        button("CONTINUE",100,500,140,40,green,bright_green,"unpause")
        button("RESTART",390,500,130,40,red,bright_red,"play")
        button("MAIN MENU",650,500,150,40,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)    

def  unpaused():
    global pause
    pause=False

def countdown_bg():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic1,(770,0))
    gamedisplays.blit(backgroundpic1,(770,200))
    gamedisplays.blit(backgroundpic1,(770,400))
    gamedisplays.blit(white_strip,(410,0))
    gamedisplays.blit(white_strip,(410,100))
    gamedisplays.blit(white_strip,(410,200))
    gamedisplays.blit(white_strip,(410,300))
    gamedisplays.blit(white_strip,(410,400))
    gamedisplays.blit(white_strip,(410,500))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(760,0))
    gamedisplays.blit(strip,(760,100))
    gamedisplays.blit(strip,(760,200))
    gamedisplays.blit(carimg,(x,y))
    text=font.render("Passed: 0",True,black)
    score=font.render("SCORE: 0",True,black)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))
    button("Pause",750,0,150,50,blue,bright_blue,"pause") 

def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.fill(purple)
            countdown_bg()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            textSurf,textRect=text_objects("3",largetext)
            textRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(textSurf,textRect)
            pygame.display.update()
            clock.tick(1)
            countdown_bg()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            textSurf,textRect=text_objects("2",largetext)
            textRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(textSurf,textRect)
            pygame.display.update()
            clock.tick(1)
            countdown_bg()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            textSurf,textRect=text_objects("1",largetext)
            textRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(textSurf,textRect)
            pygame.display.update()
            clock.tick(1)
            countdown_bg()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            textSurf,textRect=text_objects("GO!!!",largetext)
            textRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(textSurf,textRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()

def obstacle(obs_startx,obs_starty,obs):
    global obs_pic
    if obs==0:
        obs_pic=pygame.image.load("car1.png")
    elif obs==1:
        obs_pic=pygame.image.load("car.png")
    elif obs==2:
        obs_pic=pygame.image.load("car2.png") 
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))

def score_Sys(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render('Passed-'+str(passed),True,yellow)   
    score=font.render('Score-'+str(score),True,red)    
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))

def text_objects(text,font):
    textsurface=font.render(text,True,yellow)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",40)                                                 #msg font
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))                                              #msg display atv center
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)                                                                                     #msg displayed for 3 sec
    game_loop()

def crash():
    message_display('You Crashed!')

def background():

    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic1,(770,0))
    gamedisplays.blit(backgroundpic1,(770,200))
    gamedisplays.blit(backgroundpic1,(770,400))
    gamedisplays.blit(white_strip,(410,0))
    gamedisplays.blit(white_strip,(410,100))
    gamedisplays.blit(white_strip,(410,200))
    gamedisplays.blit(white_strip,(410,300))
    gamedisplays.blit(white_strip,(410,400))
    gamedisplays.blit(white_strip,(410,500))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(760,0))
    gamedisplays.blit(strip,(760,100))
    gamedisplays.blit(strip,(760,200))
def car(x,y):
    gamedisplays.blit(carimg,(x,y))                                             #blitfunction is used for putting image into window of the game

def game_loop():                                                                #loop for game
    global pause
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0
    obstacle_speed=30
    obs=0
    y_changes=0
    obs_startx=random.randrange(150,(display_width-150))
    obs_starty=-700
    obs_width=50
    obs_height=100
    passed=0
    level=0
    score=0
    y2=7
    fps=120


    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit() 
            if event.type==pygame.KEYDOWN:                                                               #to move the car
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key== pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_a:
                    obstacle_speed+=2
                if event.key==pygame.K_b:
                    obstacle_speed-=2     
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        x+=x_change 
        pause=True       
        
        gamedisplays.fill(purple)

        real_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,real_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic1,(770,real_y-backgroundpic1.get_rect().width))
        if real_y<800:
            gamedisplays.blit(backgroundpic,(0,real_y))
            gamedisplays.blit(backgroundpic1,(770,real_y))
            gamedisplays.blit(white_strip,(410,real_y))
            gamedisplays.blit(white_strip,(410,real_y+200))
            gamedisplays.blit(white_strip,(410,real_y+300))
            gamedisplays.blit(white_strip,(410,real_y+400))
            gamedisplays.blit(white_strip,(410,real_y+500))
            gamedisplays.blit(white_strip,(410,real_y+600))
            gamedisplays.blit(white_strip,(410,real_y-200))
            gamedisplays.blit(strip,(100,real_y-400))
            gamedisplays.blit(strip,(100,real_y+40))
            gamedisplays.blit(strip,(100,real_y+50))
            gamedisplays.blit(strip,(760,real_y-300))
            gamedisplays.blit(strip,(760,real_y+40))
            gamedisplays.blit(strip,(760,real_y+50))

        y2+=obstacle_speed


                                                                      
        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed                                        #speed incresed with respect to y axis
        car(x,y)                                                                                   #defining car
        score_Sys(passed,score)
        
        if x> 770-car_width or x<140:                        
            crash()
        if x>display_width-(car_width+140) or x<140:
            crash()
        if obs_starty > display_height:
            obs_starty= 0-obs_height
            obs_startx=random.randrange(150,(display_width-150))  
            obs=random.randrange(0,10) 
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+2
                largetext=pygame.font.Font("freesansbold.ttf",80)                #msg font
                textsurf,textrect=text_objects("LEVEL "+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))               #msg display at center
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3)   

        if y<obs_starty+obs_height:
            if x > obs_startx and x< obs_startx+obs_width or x+car_width >obs_startx and x +car_width < obs_startx+obs_width:
                crash()   
        button("Pause",750,0,150,50,blue,bright_blue,"pause")           
        pygame.display.update()                                                                          #display the color
        clock.tick(60)  
intro_loop()        
game_loop()
pygame.quit()
quit()                    