import pygame
from pygame.locals import *

from OpenGL.GL import*
from OpenGL.GLU import *
from OpenGL.GLUT import*

import random
import math

class player(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.speed=0.2
        self.change_x=0
        self.change_y=0
        self.shot=False
        self.ans=0

    def draw(self):
        self.move()
        glColor3f(0,1,0)
        glBegin(GL_TRIANGLES)
        glVertex3f(self.x,self.y,0)
        glVertex3f(self.x-2,self.y-2,0)
        glVertex3f(self.x+2,self.y-2,0)
        glEnd()

        glLineWidth(4)
        glBegin(GL_LINES)
        glVertex3f(self.x, self.y-1, 0)
        glVertex3f(self.x,self.y-7, 0)
        glEnd()

    def move(self):
        if self.shot:
            self.y+=self.change_y
            if self.y>7:
                self.shot=False
                self.change_y=0
                self.y=-15
        self.x+=self.change_x
        if self.x>35 or self.x<-35:
            self.change_x=0

class Ball(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.num=0
        self.change_x = 0.02
        self.radius=3
        self.moving=False
        self.visible=True
        self.red=False

    def make_ball(self,x,y,num):
        self.x=x
        self.y=y
        self.num=num

    def draw(self):
        self.move()
        if self.visible and self.x>-35:
            if self.red:
                glColor3f(1, 0, 0)
            else:
                glColor3f(1, 1, 1)
            glBegin(GL_TRIANGLE_FAN)
            glVertex3f(self.x,self.y, 0)
            for i in range(200):
                theta = 2.0 * 3.1415926 * i / 100
                x = self.radius * math.cos(theta)
                y = self.radius * math.sin(theta)
                glVertex3f(x + self.x, y + self.y, 0)
            glEnd()

            glColor3f(0, 0, 1)
            glLineWidth(5)
            glPushMatrix()
            glTranslatef(self.x-2,self.y-2, 0)
            glScalef(6 / 152.38, 6 / 152.38, 0.1 / 152.38)
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(str(self.num)))
            glPopMatrix()

    def move(self):
        if self.moving:
            self.x+=self.change_x
            if self.x>35:
                self.x=-42.5

class question(object):
    def __init__(self,stage):
        self.num_1=0
        self.operation = [" + ? = "," - ? = "," x ? = "," / ? = "]
        self.num_2=0
        self.ans=0
        self.stage=stage

    def display(self):
        glColor3f(0, 0, 0)
        glLineWidth(10)
        glPushMatrix()
        glTranslatef(-28, 17, 0)
        glScalef(8 / 152.38, 8 / 152.38, 0.1 / 152.38)
        for i in range(len(self.ques)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(self.ques[i]))
        glPopMatrix()

    def set(self):
        if self.stage==1:
            self.num_1 = random.randrange(0, 9)
            self.ans = random.randrange(1, 9)
            self.num_2 = self.num_1 + self.ans
            self.ques = str(self.num_1)+self.operation[0]+str(self.num_2)
        elif self.stage==2:
            self.num_1 = random.randrange(0, 9)
            self.ans = random.randrange(1, 9)
            self.num_2 = self.num_1 + self.ans
            self.ques = str(self.num_2) + self.operation[1] + str(self.num_1)
        elif self.stage==3:
            self.num_1 = random.randrange(1, 9)
            self.ans = random.randrange(1, 9)
            self.num_2 = self.num_1 * self.ans
            self.ques = str(self.num_1) + self.operation[2] + str(self.num_2)
        elif self.stage==4:
            self.num_1 = random.randrange(1, 9)
            self.ans = random.randrange(1, 9)
            self.num_2 = self.num_1 * self.ans
            self.ques = str(self.num_2) + self.operation[3] + str(self.num_1)

def intro():
    bg=True
    blink = []
    for k in range(100):
        x = random.randrange(-40, 40)
        y = random.randrange(20, 30)
        size = random.uniform(9, 1)
        num = random.randrange(0, 9)
        blink.append((x, y, size,num))

    for l in range(100):
        x = random.randrange(-40, 40)
        y = random.randrange(-30, -20)
        size = random.uniform(9, 1)
        num = random.randrange(0, 9)
        blink.append((x, y, size,num))

    while bg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(1,1,1,1.0)

        glBegin(GL_QUAD_STRIP)
        glColor3f(1,0,1)
        glVertex3f(-40.5,-30.5, 0)
        glVertex3f(40.5, -30.5, 0)
        glColor3f(0,0,0.5)
        glVertex3f(-40.5, 30, 0)
        glVertex3f(40.5, 30, 0)
        glEnd()

        for blinks in blink:
            glColor3f(1, 1, 1)
            glPushMatrix()
            glTranslatef(blinks[0], blinks[1], 0.0)
            glScalef(blinks[2] / 152.38, blinks[2] / 152.38, 0.1 / 152.38)
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(str(blinks[3])))
            glPopMatrix()

        # print text
        glColor3f(1,1,0)
        x=-31
        for i in range(100):
            y=5
            for j in range(150):
                glPushMatrix()
                glTranslatef(x,y, 0.0)
                glScalef(9 / 152.38, 20 / 152.38, 0.1 / 152.38)
                title = "HAPPY MATH"
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
        glLineWidth(5)
        glPushMatrix()
        glTranslatef(-40, 24, 0.0)
        glScalef(7 / 152.38, 7 / 152.38, 0.1 / 152.38)
        title = "SELECT GAME MODE "
        for i in range(len(title)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title[i]))
        glPopMatrix()

        glBegin(GL_QUADS)
        glColor3f(1, 0, 1)
        glVertex3f(-34, 20, 0)
        glVertex3f(17, 20, 0)
        glVertex3f(17, 10, 0)
        glVertex3f(-34, 10, 0)

        glColor3f(1, 0, 0)
        glVertex3f(-34, 8, 0)
        glVertex3f(17, 8, 0)
        glVertex3f(17, -2, 0)
        glVertex3f(-34,-2, 0)

        glColor3f(1.0, 0.5, 0)
        glVertex3f(-34, -4, 0)
        glVertex3f(17, -4, 0)
        glVertex3f(17, -14, 0)
        glVertex3f(-34, -14, 0)

        glColor3f(0.2, 0.2, 0.8)
        glVertex3f(-34, -16, 0)
        glVertex3f(17, -16, 0)
        glVertex3f(17, -26, 0)
        glVertex3f(-34, -26, 0)
        glEnd()

        glColor3f(1, 1, 1)
        glLineWidth(3)
        glPushMatrix()
        glTranslatef(-24, 12.5, 0.0)
        glScalef(4.5/ 152.38, 8 / 152.38, 0.1 / 152.38)
        title_1 = " ADDITION "
        for i in range(len(title_1)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title_1[i]))
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-29.5, 0.5, 0.0)
        glScalef(4.5/ 152.38, 8 / 152.38, 0.1 / 152.38)
        title_2 = " SUBTRACTION "
        for i in range(len(title_2)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title_2[i]))
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-33, -11.5, 0.0)
        glScalef(4.5 / 152.38, 8 / 152.38, 0.1 / 152.38)
        title_3 = " MULTIPLICATION "
        for i in range(len(title_3)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title_3[i]))
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-24, -23.5, 0.0)
        glScalef(4.5 / 152.38, 8 / 152.38, 0.1 / 152.38)
        title_4 = " DIVISION "
        for i in range(len(title_4)):
            glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(title_4[i]))
        glPopMatrix()

        mouse_1 = pygame.mouse.get_pos()
        click_1 = pygame.mouse.get_pressed()

        glColor3f(0, 0, 0)
        if mode == 1:
            glBegin(GL_LINE_LOOP)
            glVertex3f(-35, 21, 0)
            glVertex3f(18, 21, 0)
            glVertex3f(18, 9, 0)
            glVertex3f(-35, 9, 0)
            glEnd()
        elif mode == 2:
            glBegin(GL_LINE_LOOP)
            glVertex3f(-35, 9, 0)
            glVertex3f(18, 9, 0)
            glVertex3f(18, -3, 0)
            glVertex3f(-35, -3, 0)
            glEnd()
        elif mode == 3:
            glBegin(GL_LINE_LOOP)
            glVertex3f(-35, -3, 0)
            glVertex3f(18, -3, 0)
            glVertex3f(18, -15, 0)
            glVertex3f(-35, -15, 0)
            glEnd()
        elif mode == 4 :
            glBegin(GL_LINE_LOOP)
            glVertex3f(-35, -15, 0)
            glVertex3f(18, -15, 0)
            glVertex3f(18, -27, 0)
            glVertex3f(-35, -27, 0)
            glEnd()

        if 570 > mouse_1[0] > 60 and 200 > mouse_1[1] > 100:
            if click_1[0] == 1:
                mode=1
        elif 570 > mouse_1[0] > 60 and 320 > mouse_1[1] > 220:
            if click_1[0] == 1:
                mode=2
        elif 570 > mouse_1[0] > 60 and 440 > mouse_1[1] > 340:
            if click_1[0] == 1:
                mode=3
        elif 570 > mouse_1[0] > 60 and 560 > mouse_1[1] > 460:
            if click_1[0] == 1:
                mode=4

        if 755 > mouse_1[0] > 647 and 555 > mouse_1[1] > 100:
            glColor3f(0, 1, 0)
            if click_1[0]==1:
                sel=False
        else:
            glColor3f(0.5, 0.5, 0.5)
        glBegin(GL_TRIANGLES)
        glVertex3f(25, 20, 0)
        glVertex3f(36, -3, 0)
        glVertex3f(25, -27, 0)
        glEnd()
        pygame.display.flip()
    return mode

def game(style,music,correct,wrong,win,lose):
    help()

    stage=1
    num_stage=1
    score=0
    heart=3
    q=question(style)
    q.set()

    ball_list=[]

    for ball in range(9):
        balls = Ball()
        ball_list.append(balls)
        balls.make_ball(-34 + 8.5 *ball, 7, ball+1)

    count=0

    me=player(3,-15)

    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit=True
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    me.change_y =me.speed
                    me.shot=True
                elif event.key == pygame.K_LEFT :
                    if me.x>-35:
                        me.change_x -= me.speed
                elif event.key == pygame.K_RIGHT :
                    if me.x<35:
                        me.change_x += me.speed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    me.change_x =0
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0, 1.0)

        if stage == 1:
            name_stage = "EASY"
        elif stage == 2:
            name_stage = "NORMAL"
        elif stage == 3:
            name_stage = "HARD"

        glColor3f(1, 1, 1)
        glRasterPos2f(-38, 27)
        state = "Level : "+str(name_stage)+" _ " +str(num_stage)
        for i in range(len(state)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(state[i]))

        glRasterPos2f(20, 27)
        life = "Life :"
        for i in range(len(life)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(life[i]))

        glColor3f(1, 0, 0)
        cx = 26
        for i in range(heart * 2):
            if i % 2 == 0:
                glBegin(GL_QUADS)
                glVertex3f(cx + 0.1, 28, 0)
                glVertex3f(cx + 2, 29, 0)
                glVertex3f(cx + 3.7, 28, 0)
                glVertex3f(cx + 2, 26, 0)
                glEnd()
                cx += 1
            glBegin(GL_TRIANGLE_FAN)
            glVertex3f(cx, 28.5, 0)
            for i in range(200):
                theta = 2.0 * 3.1415926 * i / 100
                x = 1 * math.cos(theta)
                y = 1 * math.sin(theta)
                glVertex3f(x + cx, y + 28.5, 0)
            glEnd()
            cx += 1.8

        glColor3f(1, 1, 0.5)
        glBegin(GL_QUADS)
        glVertex3f(-30, 24, 0)
        glVertex3f(-30, 15, 0)
        glVertex3f(30, 15, 0)
        glVertex3f(30, 24, 0)
        glEnd()

        glLineWidth(10)
        glBegin(GL_LINE_LOOP)
        glColor3f(1,0,0)
        glVertex3f(-38, 13, 0)
        glVertex3f(-38, -23, 0)
        glVertex3f(38, -23, 0)
        glVertex3f(38, 13, 0)
        glEnd()

        q.display()

        for balls in ball_list:
            balls.draw()

        me.draw()

        if 6.8>me.y > 4.0:
            for b in range(9):
                if ball_list[b].x - 3 < me.x and ball_list[b].x + 3 > me.x:
                    ball_list[b].red=True
        elif me.y>6.8:
            for ba in range(9):
                if ball_list[ba].x - 3 < me.x and ball_list[ba].x + 3 > me.x:
                    me.ans = ball_list[ba].num
            if me.ans<1:
                me.ans=0

            if me.ans == q.ans:
                correct.play()
                score+=10
                num_stage+=1
                me.ans=0
                q.set()
            else:
                wrong.play()
                heart-=1
                num_stage+=1
                me.ans = 0
                q.set()
        else:
            for number in range(9):
                ball_list[number].red = False

        if stage>1:
            if stage==3:
                if count==200:
                    for balls in ball_list:
                        if balls.visible:
                            balls.visible=False
                        else:
                            balls.visible = True
                    count=0
                else:
                    count+=1
            if me.shot:
                for balls in ball_list:
                    balls.moving = False
                    if not balls.visible:
                        balls.visible=True
            else:
                for balls in ball_list:
                    balls.moving = True

        # end game if used all heart or answer all question
        if heart < 0 or num_stage>10:
            endGame(style,stage,score,music,correct,wrong,win,lose)
            stage+=1
            num_stage=1
            score=0
            heart=3

        mouse_2 = pygame.mouse.get_pos()
        click_2 = pygame.mouse.get_pressed()

        # pause button
        if 53 > mouse_2[0] > 12 and 590 > mouse_2[1] > 550:
            glColor3f(0.6, 0.6, 0.6)
            if click_2[0] == 1:
                music = paused(style,music,correct,wrong,win,lose)
        else:
            glColor3f(0.3, 0.3, 0.3)

        if music == 0:
            pygame.mixer.pause()
        elif music == 1:
            pygame.mixer.unpause()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(-37, -27, 0)
        for i in range(200):
            theta = 2.0 * 3.1415926 * i / 100
            x = 3 * math.cos(theta)
            y = 3 * math.sin(theta)
            glVertex3f(-37 + x, -27 + y, 0)
        glEnd()

        glColor3f(1, 1, 1)
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
            if click_2[0] == 1:
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

        longText = ['\n - Press key "LEFT" or "RIGHT" to move your arrow. ',
                    '\n - Press key "SPACEBAR" to shoot your arrow.',
                    '\n - The number on top of the ball that your arrow hit is your answer. ',
                    '\n - Be carefull, if your arrow do not hit any ball, system will take your answer as 0. ',
                    '\n - There are total 10 questions in each game mode. ',
                    '\n - Life will be deducted if you choose a wrong answer. ',
                    '\n - You lose the game autmatically if you used all 3 life. ',
                    '\n - You pass the game if you correctly answered more than 7 questions. ',
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

def endGame(stage,level,markah,lagu,betul,salah,happy,sad):
    current=True

    if level == 1:
        nama = "EASY"
    elif level == 2:
        nama = "NORMAL"
    elif level == 3:
        nama = "HARD"

    if markah<70:
        sad.play()
    else :
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
        if markah<70:
            glColor3f(0.5, 0, 1)
            glPushMatrix()
            glTranslatef(-28, 10, 0)
            glScalef(10 / 152.38, 8 / 152.38, 0.1 / 152.38)
            youLose = "YOU LOSE"
            for i in range(len(youLose)):
                glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(youLose[i]))
            glPopMatrix()

        # when pass the game
        else :
            glColor3f(0.5, 0, 1)
            glPushMatrix()
            if level < 3:
                glTranslatef(-34, 10, 0)
                glScalef(10 / 152.38, 8 / 152.38, 0.1 / 152.38)
                youWin = "PASS LEVEL"
            else :
                glTranslatef(-25, 10, 0)
                glScalef(10 / 152.38, 8 / 152.38, 0.1 / 152.38)
                youWin = "YOU WIN"
            for i in range(len(youWin)):
                glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(youWin[i]))
            glPopMatrix()

        if stage==1:
            modeGame="ADDITION "
        elif stage==2:
            modeGame="SUBTRACTION"
        elif stage==3:
            modeGame="MULTIPLICATION"
        elif stage==4:
            modeGame="DIVISION"

        glColor3f(0,0,0)
        glRasterPos2f(-17.5, 4)
        mg = "Mode Game : "+modeGame
        for i in range(len(mg)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(mg[i]))

        glRasterPos2f(-10.5, 0.5)
        stg = "Level : "+nama
        for i in range(len(stg)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(stg[i]))

        glRasterPos2f(-19, -3)
        record = "Highest Score : "+str(markah)
        for i in range(len(record)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(record[i]))

        mouse_5 = pygame.mouse.get_pos()
        click_5 = pygame.mouse.get_pressed()

        # exit button
        if 300 > mouse_5[0] > 180 and 490 > mouse_5[1] > 370:
            glColor3f(1, 1, 1)
            if click_5[0] == 1:
                current = False
                main(lagu)
        else:
            glColor3f(0.5, 0.5, 0.5)

        glBegin(GL_QUADS)
        glVertex3f(-22, -7, 0)
        glVertex3f(-10, -7, 0)
        glVertex3f(-10, -19, 0)
        glVertex3f(-22, -19, 0)
        glEnd()
        glLineWidth(5)
        glColor3f(0, 0, 0)
        glBegin(GL_LINE_STRIP)
        glVertex3f(-21, -17.5, 0)
        glVertex3f(-18.5, -17.5, 0)
        glVertex3f(-18.5, -8.5, 0)
        glVertex3f(-13.5, -8.5, 0)
        glVertex3f(-13.5, -17.5, 0)
        glVertex3f(-11, -17.5, 0)
        glEnd()
        glBegin(GL_QUADS)
        glVertex3f(-18,-17.3, 0)
        glVertex3f(-18, -9, 0)
        glVertex3f(-16, -9.5, 0)
        glVertex3f(-16, -16.8, 0)
        glEnd()

        if markah<70 or level==3:
            # restart button
            if 617 > mouse_5[0] > 500 and 490 > mouse_5[1] > 370:
                glColor3f(1, 1, 1)
                if click_5[0] == 1:
                    current = False
                    game(stage,lagu,betul,salah,happy,sad)
            else:
                glColor3f(0.5, 0.5, 0.5)

            glBegin(GL_QUADS)
            glVertex3f(22, -7, 0)
            glVertex3f(10, -7, 0)
            glVertex3f(10, -19, 0)
            glVertex3f(22, -19, 0)
            glEnd()

            glColor(0, 0, 0)
            glLineWidth(5)
            glBegin(GL_LINE_STRIP)
            for i in range(75):
                theta = 2.0 * 3.1415926 * i / 100
                x = 4 * math.cos(theta)
                y = 4 * math.sin(theta)
                glVertex3f(16 - x, -14 - y, 0)
            glEnd()
            glBegin(GL_TRIANGLES)
            glVertex3f(16.5, -8, 0)
            glVertex3f(16.5, -12, 0)
            glVertex3f(13, -10, 0)
            glEnd()

        else:
            # next level button
            if 617 > mouse_5[0] > 500 and 490 > mouse_5[1] > 370:
                glColor3f(1, 1, 1)
                if click_5[0] == 1:
                    current = False
            else:
                glColor3f(0.5, 0.5, 0.5)

            glBegin(GL_QUADS)
            glVertex3f(22, -7, 0)
            glVertex3f(10, -7, 0)
            glVertex3f(10, -19, 0)
            glVertex3f(22, -19, 0)
            glEnd()

            glColor3f(0,0,0)
            glBegin(GL_TRIANGLES)
            glVertex3f(12, -8, 0)
            glVertex3f(12, -18, 0)
            glVertex3f(21, -13, 0)
            glEnd()

        pygame.display.flip()

def main(playSound):
    glutInit(sys.argv)
    pygame.init()
    size = (800,600)
    pygame.display.set_mode(size,DOUBLEBUF | OPENGL)
    gluPerspective(45, (size[0] / size[1]), 0.1,100)
    glTranslatef(0, 0, -73)
    pygame.display.set_caption("Shooting Game")

    done = False
    clock = pygame.time.Clock()
    correct = pygame.mixer.Sound("correct.wav")
    wrong = pygame.mixer.Sound("wrong.wav")
    win = pygame.mixer.Sound("win.wav")
    lose = pygame.mixer.Sound("fail.wav")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0, 0, 1.0)

        # intro()
        # style = select()
        # game(style,playSound,correct,wrong,win,lose)
        game(1, playSound, correct, wrong, win, lose)

        clock.tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main(1)