import pygame
import math
import random
import os

pygame.init()
screen= pygame.display.set_mode((600,650))
pygame.display.set_caption("Race")
icon=pygame.image.load("./Data/logo.png")
pygame.display.set_icon(icon)
backgroundImg=pygame.image.load("./Data/Background.png")
bushImg=pygame.image.load("./Data/Bush.png")
clock=pygame.time.Clock()

running=True
clockspeed=50
loopnum=0
accelaration=0
startlineY=260
isstartgame=False

iscrash=False
iscrashleft=False
iscrashright=False

stlinex1=220
stliney1=150
stlinex2=380

carK1=0
carK2=11

b=0

bushK=0

carloopnum=0
iscarleft=False
iscarright=False

startlineImg=pygame.image.load("./Data/check.png")

#try again
##Try again
tryfont=pygame.font.Font("freesansbold.ttf",18)

def Tryagain(x,y):
    trytext=tryfont.render("Press RETURN to try again",True,(0,0,0))
    screen.blit(trytext,(x,y))
    score_value=0
#game over
gameoverImg=pygame.image.load("./Data/gameover.png")

#score
score_value=0
font=pygame.font.Font("freesansbold.ttf",22)
def showscore(x,y):
    score=font.render("SCORE : "+str(score_value),True,(0,0,0))
    screen.blit(score,(x,y))
#car2
car2img=pygame.image.load("./Data/Car2.png")
car2K=200
class car2(object):
    def __init__(self,x):
        self.x=x
        self.y=-100
    def ymotion(self,screen):
        if accelaration!=0:
            self.y+=accelaration+1
        screen.blit(car2img,(self.x,self.y))
car2list=[car2(438),car2(438),car2(438),car2(438)]

#lines
line1=[]
line2=[]
lineImg=pygame.image.load("./Data/lines12.png")
class line(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def ymotion(self,screen,accelaration):
        self.accelaration=accelaration
        self.y+=self.accelaration
        screen.blit(lineImg,(self.x,self.y))

#bush

class bush(object):
    def __init__(self,x):
        self.x=x
        self.y=random.choice([-100,-170,-220])
    def ymotion(self,screen,accelaration):
        self.accelaration=accelaration
        self.y+=self.accelaration
        screen.blit(bushImg,(self.x,self.y))
bushlist=[bush(-10),bush(540),bush(-10),bush(540),bush(540),bush(540),bush(540),bush(540),bush(-10),bush(540),bush(-10),bush(540)]
#car
carImg=pygame.image.load("E:\Studies\Python\Projects\Games\Race\Data\car0.png")
carLImg=[pygame.image.load("./Data/CarL/CarL2.png"),pygame.image.load("./Data/CarL/CarL8.png"),pygame.image.load("./Data/CarL/CarL11.png"),pygame.image.load("./Data/CarL/CarL14.png"),pygame.image.load("./Data/CarL/CarL17.png"),pygame.image.load("./Data/CarL/CarL20.png"),pygame.image.load("./Data/CarL/CarL23.png"),pygame.image.load("./Data/CarL/CarL25.png"),pygame.image.load("./Data/CarL/CarL27.png"),pygame.image.load("./Data/CarL/CarL29.png")]
carRImg=[pygame.image.load("./Data/CarR/CarR2.png"),pygame.image.load("./Data/CarR/CarR8.png"),pygame.image.load("./Data/CarR/CarR11.png"),pygame.image.load("./Data/CarR/CarR14.png"),pygame.image.load("./Data/CarR/CarR17.png"),pygame.image.load("./Data/CarR/CarR20.png"),pygame.image.load("./Data/CarR/CarR23.png"),pygame.image.load("./Data/CarR/CarR25.png"),pygame.image.load("./Data/CarR/CarR27.png"),pygame.image.load("./Data/CarR/CarR29.png")]
class car(object):
    def __init__(self,x):
        self.x=x
        self.y=400

#line
for i in range(20):
    line1.append(line(220,-70))
    line2.append(line(380,-70))

i=0
car1=car(270)
############################ while loop ##########################################################################
while running:
    clock.tick(clockspeed)
    loopnum+=1
    carloopnum+=1

    screen.blit(backgroundImg,(0,-20))
    if startlineY<800:
        startlineY+=accelaration
        screen.blit(startlineImg,(0,startlineY))
    if loopnum%50==0 and accelaration!=0:
        if i<20:
            line1[i]=line(220,-70)
            line2[i]=line(380,-70)
            i+=1 
        else:
            line1[12]=line(220,-70)
            line2[12]=line(380,-70)
            i=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if not(iscarleft) and not(iscarright):
                if event.key==pygame.K_LEFT:
                    if  car1.x!=102:
                        carloopnum=0
                        carK1=0
                        carK2=-20
                        iscarleft=True
                        iscarright=False
                if event.key==pygame.K_RIGHT:
                    if car1.x!=438:
                        carloopnum=0
                        carK1=0
                        carK2=-20
                        iscarleft=False
                        iscarright=True
                if event.key==pygame.K_SPACE:
                    accelaration=4
                    isstartgame=True
                    clockspeed=50
                    iscrash=False
                    iscrashleft=False
                    iscrashright=False
                if event.key==pygame.K_RETURN:
                    accelaration=0
                    iscrash=False
                    iscrashleft=False
                    iscrashright=False
                    for i in range(20):
                        line1[i]=line(220,-70)
                        line2[i]=line(380,-70)
                    line1[14]=line(220,130)
                    line2[14]=line(380,130)
                    i=0
                    car2list=[car2(438),car2(438),car2(438),car2(438)]
                    loopnum=0
                    score_value=0
                    startlineY=260
    #before startng the game:
    if stliney1<700:
        stliney1+=accelaration
        screen.blit(lineImg,(stlinex1,stliney1))    
        screen.blit(lineImg,(stlinex2,stliney1))    
    #display lines
    for j in range(20):
        line1[j].ymotion(screen,accelaration)
        line2[j].ymotion(screen,accelaration)

    #car2
    if loopnum%car2K==0 and (loopnum>50 and accelaration!=0):
        car2K=random.choice([50])
        if b<4:
            car2list[b]=car2(random.choice([102,438,270]))
            b+=1
        else: 
            b=0
    if isstartgame:
        for z in range(4):
            car2list[z].ymotion(screen)
    #moving straight
    if not(iscarright) and not(iscarleft):
        screen.blit(carImg,(car1.x,car1.y))
    #moving left
    elif iscarleft and not(iscrashleft):
        carloopnum+=1
        if carloopnum<170:
            car1.x-=6
        if carloopnum<33:
            if carK1%3==0:
                car1.x+=3
            screen.blit(carLImg[carK1//3],(car1.x,car1.y))
            carK1+=1
        elif carloopnum<60:
            if carK1%3==0:
                car1.x-=3
            try:
                screen.blit(carLImg[carK2//3],(car1.x,car1.y))
            except:
                print("Error")
            carK2-=1
        else:
            iscarright=False
            iscarleft=False

    #moving right
    elif iscarright and not(iscrashright):
        carloopnum+=1
        if carloopnum<200:
            car1.x+=6
        if carloopnum<33:
            if carK1%3==0:
                car1.x-=3
            screen.blit(carRImg[carK1//3],(car1.x,car1.y))
            carK1+=1
        elif carloopnum<60:
            if carK1%3==0:
                car1.x+=3
            try:
                screen.blit(carRImg[carK2//3],(car1.x,car1.y))
            except:
                print("e2")
            carK2-=1
        else:
            iscarright=False
            iscarleft=False

    #crash 
    for m in range(4):
        if not(iscarleft) and not(iscarright):
            if car1.y-(car2list[m].y)<110 and car1.y-(car2list[m].y)>0 :
                if car1.x==car2list[m].x:
                    accelaration=0
                    iscrash=True
                    iscrashleft=False
                    iscrashright=False
        elif iscarleft:
            if car1.y-(car2list[m].y)<90 and car1.y-(car2list[m].y)>-90 :
                if (car1.x-car2list[m].x<70 and car1.x-car2list[m].x>0):
                    accelaration=0
                    iscrash=True
                    iscrashleft=True
                    iscrashright=False
        elif iscarright:
            if car1.y-(car2list[m].y)<90 and car1.y-(car2list[m].y)>-90 :
                if (car2list[m].x-car1.x<70 and car2list[m].x-car1.x>0):
                    accelaration=0
                    iscrash=True
                    iscrashleft=False
                    iscrashright=True

    if iscrashleft:
        screen.blit(carLImg[10],(car1.x-5,car1.y))
    if iscrashright:
        screen.blit(carRImg[7],(car1.x-35,car1.y))
    
    #bush
    if loopnum>300 and (loopnum%80==0 and accelaration!=0):
        if bushK<12:
            bushlist[bushK]=random.choice([bush(540),bush(-10)])
            bushlist[bushK+1]=random.choice([bush(540),bush(-10)])
            bushK+=2
        else:
            bushK=0
    for m in range(12):
        bushlist[m].ymotion(screen,accelaration)

    if clockspeed<160:
        if loopnum%10==0:
            clockspeed+=5
    #score
    if clockspeed%(clockspeed/10)==0 and accelaration!=0:
        score_value+=1
    if not(iscrash):
        showscore((251-5*len(str(score_value))),0)

    if iscrash:
        screen.blit(gameoverImg,(172,107))
        showscore((251-5*len(str(score_value))),80)
        Tryagain(175,350)
    pygame.display.update()