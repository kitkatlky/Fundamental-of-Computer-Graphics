import pygame
from pygame.locals import *

from OpenGL.GL import*
from OpenGL.GLU import *
from OpenGL.GLUT import*

import random
import math

class Star(object):
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size

    def draw(self):
        glBegin(GL_TRIANGLES)
        glColor3f(1, 1, 0)
        glVertex3f(self.x, self.y, 0)
        glVertex3f(self.x - self.size, self.y - self.size, 0)
        glVertex3f(self.x+self.size, self.y-self.size, 0)

        glVertex3f(self.x, self.y - (self.size*1.5), 0)
        glVertex3f(self.x-self.size, self.y-(self.size/2), 0)
        glVertex3f(self.x+self.size, self.y-(self.size/2), 0)
        glEnd()

class Ball(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.radius=2

    def make_ball(self):
        self.x = random.randrange(-37, 0)
        self.y = random.randrange(-17, 17)
        self.change_x = random.uniform(-0.2, 0.2)
        if self.change_x == 0:
            self.change_y = random.uniform(0, 0.2)
        else:
            self.change_y = random.uniform(-0.2, 0.2)

    def draw(self):
        self.move()
        glColor3f(1, 1, 1)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(self.x,self.y, 0)
        for i in range(200):
            theta = 2.0 * 3.1415926 * i / 100
            x = self.radius * math.cos(theta)
            y = self.radius * math.sin(theta)
            glVertex3f(x + self.x, y + self.y, 0)
        glEnd()

    def move(self):
        self.x+=self.change_x
        self.y+=self.change_y
        if self.y < -20.5 or self.y > 17.5:
            self.change_y *=-1
        if self.x < -37.5 or self.x > 37.5:
            self.change_x *=-1

class Player(object):
    def __init__(self):
        self.x=30
        self.y=0
        self.speed=0.2
        self.change_x=0
        self.change_y =0

    def draw(self):
        self.move()
        glColor3f(0,1,0)
        glLineWidth(2)
        glBegin(GL_LINE_LOOP)
        glVertex3f(self.x, self.y, 0)
        glVertex3f(self.x,self.y-6, 0)
        glVertex3f(self.x+6,self.y-6, 0)
        glVertex3f(self.x+6,self.y, 0)
        glEnd()

    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.y < -16 or self.y > 19:
            self.change_y *= 0
        if self.x < -39.2 or self.x > 33.5:
            self.change_x *= 0

def intro():
    bg=True
    blink = []
    for k in range(100):
        x = random.randrange(-40, 40)
        y = random.randrange(-30, 30)
        size = random.uniform(0.2, 1)
        blink.append((x, y, size))
    while bg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0,0,0,1.0)

        glBegin(GL_QUAD_STRIP)
        # bottom
        glColor3f(0, 0, 0.1)
        glVertex3f(-40.5,-30.5, 0)
        glColor3f(0, 0, 0.3)
        glVertex3f(40.5, -30.5, 0)

        glVertex3f(-40.5, -27, 0)
        glColor3f(0, 0, 0.5)
        glVertex3f(40.5, -27, 0)

        glVertex3f(-40.5, -23, 0)
        glColor3f(0, 0.0, 0.7)
        glVertex3f(40.5, -23, 0)

        glVertex3f(-40.5, -19, 0)
        glColor3f(0, 0.0, 0.9)
        glVertex3f(40.5, -19, 0)

        glVertex3f(-40.5, -14, 0)
        glColor3f(0, 0.2, 1.0)
        glVertex3f(40.5, -14, 0)

        glVertex3f(-40.5, -9, 0)
        glColor3f(0, 0.5, 1.0)
        glVertex3f(40.5, -9, 0)

        glVertex3f(-40.5, -5, 0)
        glColor3f(0.0, 0.8, 1.0)
        glVertex3f(40.5, -5, 0)

        glVertex3f(-40.5, -2, 0)
        glColor3f(0.4, 0.8, 1)
        glVertex3f(40.5, -2, 0)

        # center

        glVertex3f(-40.5, 0, 0)
        glColor3f(0.0, 0.8, 1.0)
        glVertex3f(40.5,0, 0)


        glVertex3f(-40.5,2, 0)
        glColor3f(0, 0.5, 1.0)
        glVertex3f(40.5, 2, 0)

        glVertex3f(-40.5, 5, 0)
        glColor3f(0, 0.2, 1.0)
        glVertex3f(40.5, 5, 0)

        glVertex3f(-40.5, 9, 0)
        glColor3f(0, 0, 0.9)
        glVertex3f(40.5, 9, 0)

        glVertex3f(-40.5, 14, 0)
        glColor3f(0, 0, 0.7)
        glVertex3f(40.5, 14, 0)

        glVertex3f(-40.5, 19, 0)
        glColor3f(0, 0, 0.5)
        glVertex3f(40.5, 19, 0)

        glVertex3f(-40.5, 23, 0)
        glColor3f(0, 0, 0.3)
        glVertex3f(40.5, 23, 0)

        glVertex3f(-40.5, 27, 0)
        glColor3f(0, 0, 0.1)
        glVertex3f(40.5, 27, 0)

        glVertex3f(-40.5, 30, 0)
        glColor3f(0.0,0.0,0.0)
        glVertex3f(40.5, 30, 0)
        glEnd()

        for blinks in blink:
            glBegin(GL_TRIANGLES)
            glColor3f(1, 1, 1)
            glVertex3f(blinks[0], blinks[1], 0)
            glVertex3f(blinks[0]-blinks[2],blinks[1]-blinks[2], 0)
            glVertex3f(blinks[0]+blinks[2], blinks[1]-blinks[2], 0)

            glVertex3f(blinks[0], blinks[1]-(blinks[2]*1.5), 0)
            glVertex3f(blinks[0]-blinks[2], blinks[1]-(blinks[2]/2), 0)
            glVertex3f(blinks[0]+blinks[2], blinks[1]-(blinks[2]/2), 0)
            glEnd()

        # print text
        glColor3f(1,1,0)
        x=-40
        for i in range(150):
            y=10
            for j in range(150):
                glPushMatrix()
                glTranslatef(x,y, 0.0)
                glScalef(8.2 / 152.38, 17 / 152.38, 0.1 / 152.38)
                title = "CATCH THE STAR"
                for i in range(len(title)):
                        glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title[i]))
                glPopMatrix()
                y+=0.01
            x+=0.01

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 780 > mouse[0] > 400 and 480 > mouse[1] > 400:
            glColor3f(0, 1, 0)
            if click[0] == 1:
                bg=False
        else:
            glColor3f(1,0,0)

        x_1 =-0.8
        for i in range (80):
            y_1 = -18
            for j in range(100):
                glPushMatrix()
                glTranslatef(x_1,y_1, 0.0)
                glScalef(6.3 / 152.38, 10 / 152.38, 0.1 / 152.38)
                text = "START >>>"
                for i in range(len(text)):
                    glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(text[i]))
                glPopMatrix()
                y_1+=0.01
            x_1+=0.01
        pygame.display.flip()

def select():
    sel=True
    mode=1
    while sel:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(1, 1, 0.5, 1.0)

        glColor3f(0,0,0)
        x = -40
        for i in range (100):
            y = 18
            for j in range (100):
                glPushMatrix()
                glTranslatef(x, y, 0.0)
                glScalef(7.2/ 152.38, 15 / 152.38, 0.1 / 152.38)
                title = "SELECT GAME MODE"
                for i in range(len(title)):
                    glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title[i]))
                glPopMatrix()
                y += 0.01
            x += 0.01

        glBegin(GL_QUADS)
        glColor3f(1, 0, 1)
        glVertex3f(-34, 9, 0)
        glVertex3f(17, 9, 0)
        glVertex3f(17, 2, 0)
        glVertex3f(-34, 2, 0)

        glColor3f(1, 0, 0)
        glVertex3f(-34, -4, 0)
        glVertex3f(17, -4, 0)
        glVertex3f(17, -11, 0)
        glVertex3f(-34, -11, 0)

        glColor3f(0.2, 0.2, 0.8)
        glVertex3f(-34, -17, 0)
        glVertex3f(17, -17, 0)
        glVertex3f(17, -24, 0)
        glVertex3f(-34, -24, 0)
        glEnd()

        glColor3f(1, 1, 1)
        glLineWidth(3)
        glPushMatrix()
        glTranslatef(-33, 3, 0.0)
        glScalef(3/ 152.38, 8 / 152.38, 0.1 / 152.38)
        title_1 = " EASY    2 BALLS 1 STARS"
        for i in range(len(title_1)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title_1[i]))
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-33, -10, 0.0)
        glScalef(3/ 152.38, 8 / 152.38, 0.1 / 152.38)
        title_2 = "NORMAL   5 BALLS 1 STARS"
        for i in range(len(title_2)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title_2[i]))
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-33, -23, 0.0)
        glScalef(3 / 152.38, 8 / 152.38, 0.1 / 152.38)
        title_3 = " HARD   10 BALLS 2 STARS"
        for i in range(len(title_3)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title_3[i]))
        glPopMatrix()

        mouse_1 = pygame.mouse.get_pos()
        click_1 = pygame.mouse.get_pressed()

        glColor3f(0, 0, 0)
        if mode == 1:
            glBegin(GL_LINE_LOOP)
            glVertex3f(-35, 10, 0)
            glVertex3f(18, 10, 0)
            glVertex3f(18, 1, 0)
            glVertex3f(-35, 1, 0)
            glEnd()
        elif mode == 2:
            glBegin(GL_LINE_LOOP)
            glVertex3f(-35, -3, 0)
            glVertex3f(18, -3, 0)
            glVertex3f(18, -12, 0)
            glVertex3f(-35, -12, 0)
            glEnd()
        elif mode == 3:
            glBegin(GL_LINE_LOOP)
            glVertex3f(-35, -16, 0)
            glVertex3f(18, -16, 0)
            glVertex3f(18, -25, 0)
            glVertex3f(-35, -25, 0)
            glEnd()
        if 568 > mouse_1[0] > 65 and 270 > mouse_1[1] > 212:
            if click_1[0] == 1:
                mode=1
        elif 568 > mouse_1[0] > 65 and 400 > mouse_1[1] > 340:
            if click_1[0] == 1:
                mode=2
        elif 568 > mouse_1[0] > 65 and 530 > mouse_1[1] > 470:
            if click_1[0] == 1:
                mode=3

        if 745 > mouse_1[0] > 647 and 530 > mouse_1[1] > 212:
            glColor3f(0, 1, 0)
            if click_1[0]==1:
                sel=False
        else:
            glColor3f(0.5, 0.5, 0.5)
        glBegin(GL_TRIANGLES)
        glVertex3f(25, 9, 0)
        glVertex3f(35, -7, 0)
        glVertex3f(25, -23, 0)
        glEnd()
        pygame.display.flip()
    return mode

def game(lvl,music,getStar,hit,happy,sad):
    help()
    if lvl==1:
        num_ball=2
        num_star=1
        stage="EASY"
    elif lvl==2:
        num_ball=5
        num_star=1
        stage="NORMAL"
    elif lvl==3:
        num_ball=10
        num_star=2
        stage="HARD"

    score = 0
    heart=5
    ball_list = []
    star_list=[]
    current_ball=num_ball
    num_stage=1

    for ball in range(num_ball):
        ball = Ball()
        ball_list.append(ball)
        ball.make_ball()

    for star in range(num_star):
        x = random.randrange(-35, 35)
        y = random.randrange(-17, 17)
        star=Star(x,y,2)
        star_list.append(star)

    me=Player()

    exit = False
    timer = pygame.time.Clock()
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit=True
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    me.change_x = me.speed
                    me.change_y = 0
                elif event.key == pygame.K_LEFT:
                    me.change_x = -me.speed
                    me.change_y = 0
                elif event.key == pygame.K_UP:
                    me.change_y = + me.speed
                    me.change_x = 0
                elif event.key == pygame.K_DOWN:
                    me.change_y = -me.speed
                    me.change_x = 0
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0, 1.0)

        glColor3f(1, 1, 1)
        glRasterPos2f(-40, 28)
        state = "Game Mode : "+str(stage)+" _ " +str(num_stage)
        for i in range(len(state)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(state[i]))

        glLineWidth(3)
        glPushMatrix()
        glTranslatef(-20,22,0)
        glScalef(4/ 152.38, 4/ 152.38, 0.1 / 152.38)
        mark = "Score : "+str(score)
        for i in range(len(mark)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(mark[i]))
        glPopMatrix()

        glRasterPos2f(12, 28)
        life="Life :"
        for i in range(len(life)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(life[i]))

        glColor3f(1, 0, 0)
        cx=18
        for i in range (heart*2):
            if i%2==0:
                glBegin(GL_QUADS)
                glVertex3f(cx + 0.1, 28, 0)
                glVertex3f(cx + 2, 29, 0)
                glVertex3f(cx + 3.7, 28, 0)
                glVertex3f(cx + 2, 26, 0)
                glEnd()
                cx+=1
            glBegin(GL_TRIANGLE_FAN)
            glVertex3f(cx, 28.5, 0)
            for i in range(200):
                theta = 2.0 * 3.1415926 * i / 100
                x = 1 * math.cos(theta)
                y = 1 * math.sin(theta)
                glVertex3f(x+cx, y +28.5, 0)
            glEnd()
            cx+=1.8

        glLineWidth(10)
        glBegin(GL_LINE_LOOP)
        glColor3f(1, 0, 0)
        glVertex3f(-40, 20, 0)
        glVertex3f(-40, -23, 0)
        glVertex3f(40, -23, 0)
        glVertex3f(40, 20, 0)
        glEnd()

        for balls in ball_list:
            balls.draw()

            # when hit player cube
            if -(2+6)<balls.y-me.y<2 and -2<balls.x-me.x<6+2:
                hit.play()
                score -= 5
                heart -= 1
                balls.x = random.randrange(-37, 37)
                balls.y = random.randrange(-17, 17)

        for stars in star_list:
            stars.draw()

        #     when player found star
            if stars.x-2>me.x and me.x+6>stars.x+2:
                if stars.y<me.y and me.y-6<stars.y-3:
                    getStar.play()
                    score += 10
                    stars.x = random.randrange(-35, 35)
                    stars.y = random.randrange(-17, 17)

        me.draw()
        # end game if used all heart
        if heart < 0:
            endGame(0, score, num_stage, lvl, music, getStar, hit, happy, sad)

        # enter new level if hit score 100
        if score>=100:
            # end game if pass the stage
            if current_ball >= num_ball + 2:
                endGame(1, score, num_stage, lvl, music, getStar, hit, happy, sad)
            else:
                score = 0
                me.speed+=0.05
                current_ball += 1
                num_stage+=1
                new_ball = Ball()
                ball_list.append(new_ball)
                new_ball.make_ball()
                if heart<5:
                    heart+=1

        mouse_2 = pygame.mouse.get_pos()
        click_2 = pygame.mouse.get_pressed()

        # pause button
        if 53 > mouse_2[0] > 12 and 590 > mouse_2[1] > 550:
            glColor3f(0.6,0.6,0.6)
            if click_2[0] == 1:
                music=paused(lvl,music,getStar,hit,happy,sad)
        else:
            glColor3f(0.3,0.3,0.3)

        if music==0:
            pygame.mixer.pause()
        elif music==1:
            pygame.mixer.unpause()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(-37, -27, 0)
        for i in range(200):
            theta = 2.0 * 3.1415926 * i / 100
            x = 3 * math.cos(theta)
            y = 3 * math.sin(theta)
            glVertex3f(-37+x, -27+y, 0)
        glEnd()

        glColor3f(1,1,1)
        glBegin(GL_QUADS)
        glVertex3f(-36.5, -29, 0)
        glVertex3f(-36.5, -25, 0)
        glVertex3f(-35.5, -25, 0)
        glVertex3f(-35.5, -29, 0)

        glVertex3f(-37.5, -29, 0)
        glVertex3f(-37.5, -25, 0)
        glVertex3f(-38.5, -25, 0)
        glVertex3f(-38.5, -29, 0)
        glEnd()

        # help button
        if 780 > mouse_2[0] > 590 and 590 > mouse_2[1] > 560:
            glColor3f(0, 0.5, 1)
            if click_2[0]==1:
                help()
        else:
            glColor3f(0, 1, 1)

        glLineWidth(3)
        glPushMatrix()
        glTranslatef(19, -29, 0)
        glScalef(3 / 152.38, 4 / 152.38, 0.1 / 152.38)
        hlp = "HOW TO PLAY"
        for i in range(len(hlp)):
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(hlp[i]))
        glPopMatrix()

        timer.tick(60)
        pygame.display.flip()

def help():
    play = False
    while not play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1,1,1)
        glBegin(GL_QUADS)
        glVertex3f(-35, -25, 0)
        glVertex3f(-35, 25, 0)
        glVertex3f(35, 25, 0)
        glVertex3f(35 , -25, 0)
        glEnd()

        glColor3f(0.5, 0, 1)
        glLineWidth(10)
        glPushMatrix()
        glTranslatef(-30, 19, 0)
        glScalef(8 / 152.38, 5 / 152.38, 0.1 / 152.38)
        hlp = "HOW TO PLAY"
        for i in range(len(hlp)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(hlp[i]))
        glPopMatrix()

        longText = ['\n - Press key "UP","DOWN","LEFT", and "RIGHT" to move your cube. ',
                    '\n - Successfully collect one STAR will earn 10 score.',
                    '\n - 5 score will be DEDUCTED if accidentally hit the moving ball.',
                    '\n - Life will be deducted also if hit the moving ball. ',
                    '\n - There are total 3 level in this game. You are required to collect 100 score to',
                    '\n     pass each level.',
                    '\n - After passing one level, your movement will become faster. The number',
                    '\n     of moving balls and life will be increase by one. ',
                    '',
                    '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*** GOOD LUCK TO ALL PLAYER '
                    '***\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n']
        ypos=13
        for i in range(len(longText)):
            glRasterPos2f(-32, ypos)
            for j in range(len(longText[i])):
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(longText[i][j]))
            ypos-=4

        mouse_3 = pygame.mouse.get_pos()
        click_3 = pygame.mouse.get_pressed()

        if 727 > mouse_3[0] > 608 and 537 > mouse_3[1] > 470:
            glColor3f(0, 1, 0)
            if click_3[0]==1:
                play=True
        else:
            glColor3f(1,0,0)
        glBegin(GL_QUADS)
        glVertex3f(21, -24, 0)
        glVertex3f(33, -24, 0)
        glVertex3f(33, -17, 0)
        glVertex3f(21, -17, 0)
        glEnd()
        glColor3f(0, 0, 0)
        glPushMatrix()
        glTranslatef(22, -22, 0)
        glScalef(8 / 152.38, 5 / 152.38, 0.1 / 152.38)
        resume = "OK"
        for i in range(len(resume)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(resume[i]))
        glPopMatrix()

        pygame.display.flip()

def paused(hardness,sound,gS,H,smile,cry):
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1, 1, 0.5)
        glBegin(GL_QUADS)
        glVertex3f(-35, -25, 0)
        glVertex3f(-35, 25, 0)
        glVertex3f(35, 25, 0)
        glVertex3f(35, -25, 0)
        glEnd()

        glColor3f(0.5, 0, 1)
        glLineWidth(5)
        glPushMatrix()
        glTranslatef(-30, 19, 0)
        glScalef(8 / 152.38, 5 / 152.38, 0.1 / 152.38)
        p = "GAME PAUSED"
        for i in range(len(p)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(p[i]))
        glPopMatrix()

        mouse_4 = pygame.mouse.get_pos()
        click_4 = pygame.mouse.get_pressed()

        # resume button
        if 490 > mouse_4[0] > 310 and 360 > mouse_4[1] > 180:
            glColor3f(0,1,0)
            if click_4[0]==1:
                pause=False
                return sound
        else:
            glColor3f(0.5, 0.5, 0.5)

        glBegin(GL_TRIANGLES)
        glVertex3f(10, 3, 0)
        glVertex3f(-10, 13, 0)
        glVertex3f(-10, -7, 0)
        glEnd()

        # exit button
        if 242 > mouse_4[0] > 160 and 520 > mouse_4[1] > 440:
            glColor3f(1, 1, 1)
            if click_4[0] == 1:
                pause=False
                main(sound)
        else:
            glColor3f(0.5, 0.5, 0.5)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(-20, -18, 0)
        for i in range(200):
            theta = 2.0 * 3.1415926 * i / 100
            x = 5 * math.cos(theta)
            y = 5 * math.sin(theta)
            glVertex3f(-20 + x, -18 + y, 0)
        glEnd()

        glLineWidth(1)
        glColor3f(0,0,0)
        glBegin(GL_LINE_STRIP)
        glVertex3f(-23,-21,0)
        glVertex3f(-21.5, -21, 0)
        glVertex3f(-21.5, -15, 0)
        glVertex3f(-18.5, -15, 0)
        glVertex3f(-18.5, -21, 0)
        glVertex3f(-17, -21, 0)
        glEnd()
        glBegin(GL_QUADS)
        glVertex3f(-21.3,-15.1,0)
        glVertex3f(-21.3, -20.9, 0)
        glVertex3f(-20, -20, 0)
        glVertex3f(-20, -15.5, 0)
        glEnd()

        # sound button
        if 440 > mouse_4[0] > 360 and 520 > mouse_4[1] > 440:
            glColor3f(1, 1, 1)
            if click_4[0] == 1:
                if sound==0:
                    sound=1
                else:
                    sound=0
        else:
            glColor3f(0.5, 0.5, 0.5)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, -18, 0)
        for i in range(200):
            theta = 2.0 * 3.1415926 * i / 100
            x = 5 * math.cos(theta)
            y = 5 * math.sin(theta)
            glVertex3f(0 + x, -18 + y, 0)
        glEnd()

        glColor(0, 0, 0)
        glBegin(GL_POLYGON)
        glVertex3f(-2, -16, 0)
        glVertex3f(-3.5, -16, 0)
        glVertex3f(-3.5, -20, 0)
        glVertex3f(-2, -20, 0)
        glVertex3f(0, -22, 0)
        glVertex3f(0, -14, 0)
        glEnd()

        if sound==1:
            glLineWidth(2)
            for radius in range(2,5):
                glBegin(GL_LINE_STRIP)
                for i in range(-15,15):
                    theta = 2.0 * 3.1415926 * i / 100
                    x = radius * math.cos(theta)
                    y = radius * math.sin(theta)
                    glVertex3f(0 + x, -18 + y, 0)
                glEnd()
        elif sound==0:
            glLineWidth(5)
            glBegin(GL_LINES)
            glVertex3f(2.5, -16, 0)
            glVertex3f(1.5, -20 , 0)

            glVertex3f(2.5 , -20 ,0)
            glVertex3f(1.5, -16 , 0)
            glEnd()

        # restart button
        if 640 > mouse_4[0] > 560 and 520 > mouse_4[1] > 440:
            glColor3f(1, 1, 1)
            if click_4[0] == 1:
                pause = False
                game(hardness,sound,gS,H,smile,cry)
        else:
            glColor3f(0.5, 0.5, 0.5)

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(20, -18, 0)
        for i in range(200):
            theta = 2.0 * 3.1415926 * i / 100
            x = 5 * math.cos(theta)
            y = 5 * math.sin(theta)
            glVertex3f(20 + x, -18 + y, 0)
        glEnd()

        glColor(0,0,0)
        glLineWidth(5)
        glBegin(GL_LINE_STRIP)
        for i in range(75):
            theta = 2.0 * 3.1415926 * i / 100
            x = 2.5 * math.cos(theta)
            y = 2.5 * math.sin(theta)
            glVertex3f(20-x, -18 - y, 0)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex3f(20.5, -14, 0)
        glVertex3f(20.5, -17, 0)
        glVertex3f(18.5 , -15.5 , 0)
        glEnd()

        pygame.display.flip()

def endGame(winGame,markah,stagePass,lvl,music,getStar,hit,happy,sad):
    current=True
    if winGame==0:
        sad.play()
    elif winGame==1:
        happy.play()
    while current:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(0.2, 1, 0.7)
        glBegin(GL_QUADS)
        glVertex3f(-35, -23, 0)
        glVertex3f(-35, 20, 0)
        glVertex3f(35, 20, 0)
        glVertex3f(35, -23, 0)
        glEnd()

        glLineWidth(10)
        # when lose the game
        if winGame==0:
            glColor3f(0.5, 0, 1)
            glPushMatrix()
            glTranslatef(-28, 11, 0)
            glScalef(10 / 152.38, 8 / 152.38, 0.1 / 152.38)
            youLose = "YOU LOSE"
            for i in range(len(youLose)):
                glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(youLose[i]))
            glPopMatrix()

        # when pass the game
        elif winGame==1:
            glColor3f(0.5, 0, 1)
            glPushMatrix()
            glTranslatef(-25, 11, 0)
            glScalef(10 / 152.38, 8 / 152.38, 0.1 / 152.38)
            youWin = "YOU WIN"
            for i in range(len(youWin)):
                glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(youWin[i]))
            glPopMatrix()

        if lvl==1:
            modeGame="EASY"
        elif lvl==2:
            modeGame="NORMAL"
        elif lvl==3:
            modeGame="HARD"

        glColor3f(0,0,0)
        glRasterPos2f(-13.5, 3.5)
        mg = "Mode Game : "+modeGame+" _ "+str(stagePass)
        for i in range(len(mg)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(mg[i]))

        glRasterPos2f(-15, 0)
        record = "Highest Score : "+str(markah)
        for i in range(len(record)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(record[i]))

        mouse_5 = pygame.mouse.get_pos()
        click_5 = pygame.mouse.get_pressed()

        # exit button
        if 300 > mouse_5[0] > 180 and 460 > mouse_5[1] > 340:
            glColor3f(1, 1, 1)
            if click_5[0] == 1:
                current = False
                main(music)
        else:
            glColor3f(0.5, 0.5, 0.5)

        glBegin(GL_QUADS)
        glVertex3f(-22, -4, 0)
        glVertex3f(-10, -4, 0)
        glVertex3f(-10, -16, 0)
        glVertex3f(-22, -16, 0)
        glEnd()
        glLineWidth(5)
        glColor3f(0, 0, 0)
        glBegin(GL_LINE_STRIP)
        glVertex3f(-21, -14.5, 0)
        glVertex3f(-18.5, -14.5, 0)
        glVertex3f(-18.5, -5.5, 0)
        glVertex3f(-13.5, -5.5, 0)
        glVertex3f(-13.5, -14.5, 0)
        glVertex3f(-11, -14.5, 0)
        glEnd()
        glBegin(GL_QUADS)
        glVertex3f(-18,-14.3, 0)
        glVertex3f(-18, -6, 0)
        glVertex3f(-16, -6.5, 0)
        glVertex3f(-16, -13.8, 0)
        glEnd()

        # restart button
        if 617 > mouse_5[0] > 500 and 460 > mouse_5[1] > 340:
            glColor3f(1, 1, 1)
            if click_5[0] == 1:
                current = False
                game(lvl,music,getStar,hit,happy,sad)
        else:
            glColor3f(0.5, 0.5, 0.5)

        glBegin(GL_QUADS)
        glVertex3f(22, -4, 0)
        glVertex3f(10, -4, 0)
        glVertex3f(10, -16, 0)
        glVertex3f(22, -16, 0)
        glEnd()

        glColor(0, 0, 0)
        glLineWidth(5)
        glBegin(GL_LINE_STRIP)
        for i in range(75):
            theta = 2.0 * 3.1415926 * i / 100
            x = 4 * math.cos(theta)
            y = 4 * math.sin(theta)
            glVertex3f(16 - x, -11 - y, 0)
        glEnd()
        glBegin(GL_TRIANGLES)
        glVertex3f(16.5, -5, 0)
        glVertex3f(16.5, -9, 0)
        glVertex3f(13, -7, 0)
        glEnd()
        pygame.display.flip()

def main(playSound):
    glutInit(sys.argv)
    pygame.init()
    size = (800,600)
    pygame.display.set_mode(size,DOUBLEBUF | OPENGL)
    gluPerspective(45, (size[0] / size[1]), 0.1,100)
    glTranslatef(0, 0, -73)
    pygame.display.set_caption("Bouncing Balls Game")

    done = False
    clock = pygame.time.Clock()
    slip=pygame.mixer.Sound("slip.wav")
    buzzer=pygame.mixer.Sound("buzzer.wav")
    win=pygame.mixer.Sound("win.wav")
    lose=pygame.mixer.Sound("fail.wav")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0, 1.0)

        intro()
        style=select()
        game(style,playSound,slip,buzzer,win,lose)
        clock.tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main(1)
