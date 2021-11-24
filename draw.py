from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

import math

rot = 0.0
# mouse parameter
lastx = lasty = 0.0
xrot = 0.0
yrot = 0.0
# box initialise state
num=0
# object rotate
xRot=0
yRot=0
# eye z
zEye=-25
# static mode
staticRot=0
xBefore=0
yBefore=0

class box(object):
    def __init__(self,state):
        self.state=state

    def draw(self):
        if self.state==0:
            self.bottom()
            self.top()
            glTranslatef(-3.6,0,0)
            glRotatef(50, 1, 0, 0)

        if self.state==1:
            self.bottom()
            glTranslatef(1,0,0)

        elif self.state==2:
            pass

    def bottom(self):
        glTranslatef(-1, 0, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)
        # z=-3
        glVertex3f(3, -3, -3)
        glVertex3f(-3, -3, -3)
        glVertex3f(-3, 3, -3)
        glVertex3f(3, 3, -3)
        # y=3
        glVertex3f(3, 3, -3)
        glVertex3f(-3, 3, -3)
        glVertex3f(-3, 3, 3)
        glVertex3f(3, 3, 3)
        # z=3
        glVertex3f(3, 3, 3)
        glVertex3f(-3, 3, 3)
        glVertex3f(-3, -3, 3)
        glVertex3f(3, -3, 3)
        # y=-3
        glVertex3f(3, -3, 3)
        glVertex3f(-3, -3, 3)
        glVertex3f(-3, -3, -3)
        glVertex3f(3, -3, -3)
        # x=-3
        glVertex3f(-3, -3, 3)
        glVertex3f(-3, -3, -3)
        glVertex3f(-3, 3, -3)
        glVertex3f(-3, 3, 3)

        # inner box
        glColor3f(0.0, 0.0, 0.0)
        # z=-2.9
        glVertex3f(2.9, -2.9, -2.9)
        glVertex3f(-2.9, -2.9, -2.9)
        glVertex3f(-2.9, 2.9, -2.9)
        glVertex3f(2.9, 2.9, -2.9)
        # y=2.9
        glVertex3f(2.9, 2.9, -2.9)
        glVertex3f(-2.9, 2.9, -2.9)
        glVertex3f(-2.9, 2.9, 2.9)
        glVertex3f(2.9, 2.9, 2.9)
        # z=2.9
        glVertex3f(2.9, 2.9, 2.9)
        glVertex3f(-2.9, 2.9, 2.9)
        glVertex3f(-2.9, -2.9, 2.9)
        glVertex3f(2.9, -2.9, 2.9)
        # y=-2.9
        glVertex3f(2.9, -2.9, 2.9)
        glVertex3f(-2.9, -2.9, 2.9)
        glVertex3f(-2.9, -2.9, -2.9)
        glVertex3f(2.9, -2.9, -2.9)
        # x=-2.9
        glVertex3f(-2.9, -2.9, 2.9)
        glVertex3f(-2.9, -2.9, -2.9)
        glVertex3f(-2.9, 2.9, -2.9)
        glVertex3f(-2.9, 2.9, 2.9)

        # ribbon
        glColor3f(0.8, 0.8, 0.8)
        # z=-3.1
        glVertex3f(2.5, -0.5, -3.1)
        glVertex3f(-3.1, -0.5, -3.1)
        glVertex3f(-3.1, 0.5, -3.1)
        glVertex3f(2.5, 0.5, -3.1)
        # y=3.1
        glVertex3f(2.5, 3.1, -0.5)
        glVertex3f(-3.1, 3.1, -0.5)
        glVertex3f(-3.1, 3.1, 0.5)
        glVertex3f(2.5, 3.1, 0.5)
        # z=3.1
        glVertex3f(2.5, 0.5, 3.1)
        glVertex3f(-3.1, 0.5, 3.1)
        glVertex3f(-3.1, -0.5, 3.1)
        glVertex3f(2.5, -0.5, 3.1)
        # y=-3.1
        glVertex3f(2.5, -3.1, 0.5)
        glVertex3f(-3.1, -3.1, 0.5)
        glVertex3f(-3.1, -3.1, -0.5)
        glVertex3f(2.5, -3.1, -0.5)
        # x=-3.1
        glVertex3f(-3.1, -0.5, 3.1)
        glVertex3f(-3.1, -0.5, -3.1)
        glVertex3f(-3.1, 0.5, -3.1)
        glVertex3f(-3.1, 0.5, 3.1)

        glVertex3f(-3.1, -3.1, 0.5)
        glVertex3f(-3.1, -3.1, -0.5)
        glVertex3f(-3.1, 3.1, -0.5)
        glVertex3f(-3.1, 3.1, 0.5)
        glEnd()

    def top(self):
        # upper box
        glTranslatef(3.5, 0, 0)
        glColor3f(0.9, 0, 0)
        glBegin(GL_QUADS)
        # z=-3.1
        glVertex3f(1, -3.1, -3.1)
        glVertex3f(-1, -3.1, -3.1)
        glVertex3f(-1, 3.1, -3.1)
        glVertex3f(1, 3.1, -3.1)
        # y=3.1
        glVertex3f(1, 3.1, -3.1)
        glVertex3f(-1, 3.1, -3.1)
        glVertex3f(-1, 3.1, 3.1)
        glVertex3f(1, 3.1, 3.1)
        # z=3.1
        glVertex3f(1, 3.1, 3.1)
        glVertex3f(-1, 3.1, 3.1)
        glVertex3f(-1, -3.1, 3.1)
        glVertex3f(1, -3.1, 3.1)
        # y=-3.1
        glVertex3f(1, -3.1, 3.1)
        glVertex3f(-1, -3.1, 3.1)
        glVertex3f(-1, -3.1, -3.1)
        glVertex3f(1, -3.1, -3.1)
        # x=1
        glVertex3f(1, -3.1, 3.1)
        glVertex3f(1, -3.1, -3.1)
        glVertex3f(1, 3.1, -3.1)
        glVertex3f(1, 3.1, 3.1)

        # ribbon
        glColor3f(0.8, 0.8, 0.8)
        # z=-3.2
        glVertex3f(1.1, -0.5, -3.2)
        glVertex3f(-1.1, -0.5, -3.2)
        glVertex3f(-1.1, 0.5, -3.2)
        glVertex3f(1.1, 0.5, -3.2)

        glVertex3f(-1.1, -0.5, -3.1)
        glVertex3f(-1.1, -0.5, -3.2)
        glVertex3f(-1.1, 0.5, -3.2)
        glVertex3f(-1.1, 0.5, -3.1)
        # y=3.2
        glVertex3f(1.1, 3.2, -0.5)
        glVertex3f(-1.1, 3.2, -0.5)
        glVertex3f(-1.1, 3.2, 0.5)
        glVertex3f(1.1, 3.2, 0.5)

        glVertex3f(-1.1, 3.1, -0.5)
        glVertex3f(-1.1, 3.2, -0.5)
        glVertex3f(-1.1, 3.2, 0.5)
        glVertex3f(-1.1, 3.1, 0.5)
        # z=3.2
        glVertex3f(1.1, 0.5, 3.2)
        glVertex3f(-1.1, 0.5, 3.2)
        glVertex3f(-1.1, -0.5, 3.2)
        glVertex3f(1.1, -0.5, 3.2)

        glVertex3f(-1.1, 0.5, 3.1)
        glVertex3f(-1.1, 0.5, 3.2)
        glVertex3f(-1.1, -0.5, 3.2)
        glVertex3f(-1.1, -0.5, 3.1)
        # y=-3.2
        glVertex3f(1.1, -3.2, 0.5)
        glVertex3f(-1.1, -3.2, 0.5)
        glVertex3f(-1.1, -3.2, -0.5)
        glVertex3f(1.1, -3.2, -0.5)

        glVertex3f(-1.1, -3.1, 0.5)
        glVertex3f(-1.1, -3.2, 0.5)
        glVertex3f(-1.1, -3.2, -0.5)
        glVertex3f(-1.1, -3.1, -0.5)
        # x=1.1 &z=3.2
        glVertex3f(1.1, -0.5, 3.2)
        glColor3f(0.7, 0.7, 0.7)
        glVertex3f(1.1, -0.1, 0)
        glVertex3f(1.1, 0.1, 0)
        glColor3f(0.8, 0.8, 0.8)
        glVertex3f(1.1, 0.5, 3.2)
        # x=1.1 & z=-3.2
        glVertex3f(1.1, 0.5, -3.2)
        glColor3f(0.7, 0.7, 0.7)
        glVertex3f(1.1, 0.1, 0)
        glVertex3f(1.1, -0.1, 0)
        glColor3f(0.8, 0.8, 0.8)
        glVertex3f(1.1, -0.5, -3.2)
        # x=1.1 & y=-3.2
        glVertex3f(1.1, -3.2, 0.5)
        glVertex3f(1.1, -3.2, -0.5)
        glColor3f(0.7, 0.7, 0.7)
        glVertex3f(1.1, 0, -0.2)
        glVertex3f(1.1, 0, 0.2)
        # x=1.1 & y=3.2
        glVertex3f(1.1, 0, 0.2)
        glVertex3f(1.1, 0, -0.2)
        glColor3f(0.8, 0.8, 0.8)
        glVertex3f(1.1, 3.2, -0.5)
        glVertex3f(1.1, 3.2, 0.5)
        glEnd()

        glTranslatef(1.0, 0, 0)
        glRotatef(40, 1, 0, 0)
        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_QUAD_STRIP)
        glVertex3f(0.0, 0, 0.2)
        glVertex3f(0.0, 0, 0)

        glColor3f(0.8, 0.8, 0.8)
        glVertex3f(0.8, 2.5, 0.8)
        glVertex3f(0.8, 2.5, -0.3)
        for i in range(-25, 30):
            theta = 2 * 3.142 * i / 100
            cx = 0.4 * math.sin(theta)
            cy = 0.4 * math.cos(theta)
            glVertex3f(0.4 - cx, 2.5 + cy, 0.8)
            glVertex3f(0.4 - cx, 2.5 + cy, -0.3)
        glVertex3f(0.0, 0.3, 0.1)
        glVertex3f(0.0, 0.3, 0)
        glEnd()

        glRotatef(90, 1, 0, 0)
        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_QUAD_STRIP)
        glVertex3f(0.0, 0, 0.2)
        glVertex3f(0.0, 0, 0)

        glColor3f(0.8, 0.8, 0.8)
        glVertex3f(0.8, 2.5, 0.8)
        glVertex3f(0.8, 2.5, -0.3)
        for i in range(-25, 30):
            theta = 2 * 3.142 * i / 100
            cx = 0.4 * math.sin(theta)
            cy = 0.4 * math.cos(theta)
            glVertex3f(0.4 - cx, 2.5 + cy, 0.8)
            glVertex3f(0.4 - cx, 2.5 + cy, -0.3)
        glVertex3f(0.0, 0.3, 0.1)
        glVertex3f(0.0, 0.3, 0)
        glEnd()

        glRotatef(90, 1, 0, 0)
        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_QUAD_STRIP)
        glVertex3f(0.0, 0, 0.2)
        glVertex3f(0.0, 0, 0)

        glColor3f(0.8, 0.8, 0.8)
        glVertex3f(0.8, 2.5, 0.8)
        glVertex3f(0.8, 2.5, -0.3)
        for i in range(-25, 30):
            theta = 2 * 3.142 * i / 100
            cx = 0.4 * math.sin(theta)
            cy = 0.4 * math.cos(theta)
            glVertex3f(0.4 - cx, 2.5 + cy, 0.8)
            glVertex3f(0.4 - cx, 2.5 + cy, -0.3)
        glVertex3f(0.0, 0.3, 0.1)
        glVertex3f(0.0, 0.3, 0)
        glEnd()

        glRotatef(90, 1, 0, 0)
        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_QUAD_STRIP)
        glVertex3f(0.0, 0, 0.2)
        glVertex3f(0.0, 0, 0)

        glColor3f(0.8, 0.8, 0.8)
        glVertex3f(0.8, 2.5, 0.8)
        glVertex3f(0.8, 2.5, -0.3)
        for i in range(-25, 30):
            theta = 2 * 3.142 * i / 100
            cx = 0.4 * math.sin(theta)
            cy = 0.4 * math.cos(theta)
            glVertex3f(0.4 - cx, 2.5 + cy, 0.8)
            glVertex3f(0.4 - cx, 2.5 + cy, -0.3)
        glVertex3f(0.0, 0.3, 0.1)
        glVertex3f(0.0, 0.3, 0)
        glEnd()

class bear(object):
    def draw(self):
        self.head()
        self.body()

    def head(self):
        glTranslatef(1.5, 0.2, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.5,50,10)
        glutSolidSphere(1.5, 50, 10)
        glPopMatrix()

        glTranslatef(0, 0.5, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.5,50,10)
        glutSolidSphere(1.5, 50, 10)
        glPopMatrix()

        glTranslatef(0, -0.9, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.5, 50, 10)
        glutSolidSphere(1.5, 50, 10)
        glPopMatrix()

        glTranslatef(0, -0.5, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.5, 50, 10)
        glutSolidSphere(1.5, 50, 10)
        glPopMatrix()

        glTranslatef(0.25, 0.7, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.5,50,10)
        glutSolidSphere(1.5, 50, 10)
        glPopMatrix()

        glTranslatef(-0.05, 0.3, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.5,50,10)
        glutSolidSphere(1.5, 50, 10)
        glPopMatrix()

        glTranslatef(0, -0.6, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.5,50,10)
        glutSolidSphere(1.5, 50, 10)
        glPopMatrix()

        glTranslatef(1.2, 2.0, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(0.5, 50, 10)
        glutSolidSphere(0.5, 50, 10)
        glPopMatrix()

        glTranslatef(-0.08, 0.05, -0.15)
        glColor3f(1, 1, 0)
        glPushMatrix()
        # glutWireSphere(0.4, 50, 10)
        glutSolidSphere(0.4, 50, 10)
        glPopMatrix()

        glTranslatef(0.08, -3.45, 0.15)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(0.5, 50, 10)
        glutSolidSphere(0.5, 50, 10)
        glPopMatrix()

        glTranslatef(-0.08, -0.05, -0.15)
        glColor3f(1, 1, 0)
        glPushMatrix()
        # glutWireSphere(0.4, 50, 10)
        glutSolidSphere(0.4, 50, 10)
        glPopMatrix()

        # EYE
        glTranslatef(-1.42, 1.75, -1.35)
        glColor3f(0, 0, 0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0.7, 0)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.25 * math.sin(theta)
            cy = 0.25 * math.cos(theta)
            glVertex3f(0 + cx, 0.7 + cy, 0)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, -0.7, 0)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.25 * math.sin(theta)
            cy = 0.25 * math.cos(theta)
            glVertex3f(0 + cx, -0.7 + cy, 0)
        glEnd()

        # NOSE
        glRotate(30, 0, 1, 0)
        glTranslatef(-0.63, 0.06, -0.05)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.38,10,100)
        glutSolidTorus(0.1, 0.38, 10, 100)
        glPopMatrix()

        glTranslatef(0.0, -0.12, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1, 0.38, 10, 100)
        glutSolidTorus(0.1, 0.38, 10, 100)
        glPopMatrix()

        glColor3f(1, 1, 1)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0.14, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.4 * math.sin(theta)
            cy = 0.4 * math.cos(theta)
            glVertex3f(0 + cx, 0.14 + cy, -0.1)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(-0.0, 0.02, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.4 * math.sin(theta)
            cy = 0.4 * math.cos(theta)
            glVertex3f(-0.0 + cx, 0.02 + cy, -0.1)
        glEnd()

        glColor3f(0, 0, 0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0.1, 0.04, -0.15)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.15 * math.sin(theta)
            cy = 0.15 * math.cos(theta)
            glVertex3f(0.1 + cx, 0.04 + cy, -0.15)
        glEnd()

        glBegin(GL_LINES)
        for x in range(15):
            glVertex3f(-0.02 - x / 200, 0.04, -0.15)
            glVertex3f(-0.10 - x / 200, -0.20, -0.15)
            glVertex3f(-0.02 - x / 200, 0.04, -0.15)
            glVertex3f(-0.10 - x / 200, 0.28, -0.15)
        glEnd()

    def body(self):
        glRotate(-30, 0, 1, 0)
        glTranslatef(-1.8, 0.26, 1.35)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.4,50,10)
        glutSolidSphere(1.4, 50, 10)
        glPopMatrix()

        glTranslatef(-0.5, 0, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.4,50,10)
        glutSolidSphere(1.4, 50, 10)
        glPopMatrix()

        glTranslatef(-0.5, 0, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.4,50,10)
        glutSolidSphere(1.4, 50, 10)
        glPopMatrix()

        glTranslatef(1.0, -0.4, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.4,50,10)
        glutSolidSphere(1.4, 50, 10)
        glPopMatrix()

        glTranslatef(-0.5, 0, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.4,50,10)
        glutSolidSphere(1.4, 50, 10)
        glPopMatrix()

        glTranslatef(-0.5, 0, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(1.4,50,10)
        glutSolidSphere(1.4, 50, 10)
        glPopMatrix()

        # white abdomen
        glTranslatef(1.1, 0.2, -1.3)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(-0.3, 0, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(-0.3, 0, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(-0.3, 0, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(-0.3, 0, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(1.1, 0.2, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(-0.3, 0, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(-0.3, 0, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(-0.3, 0, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(-0.3, 0, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(1.2, -0.4, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(-0.3, 0, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(-0.3, 0, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(-0.3, 0, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        glTranslatef(-0.3, 0, 0)
        glColor3f(1, 1, 1)
        glPushMatrix()
        # glutWireTorus(0.1,0.5,10,100)
        glutSolidTorus(0.1, 0.5, 10, 100)
        glPopMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, -0.1)
        for i in range(200):
            theta = 2 * 3.142 * i / 100
            cx = 0.5 * math.sin(theta)
            cy = 0.5 * math.cos(theta)
            glVertex3f(0 + cx, 0 + cy, -0.1)
        glEnd()

        # leg
        glTranslatef(-0.5, -0.9, 1.8)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(0.5,50,10)
        glutSolidSphere(0.5, 50, 10)
        glPopMatrix()

        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireCylinder(0.5,-2.5,50,10)
        glutSolidCylinder(0.5, -2.5, 50, 10)
        glPopMatrix()

        glTranslatef(0, 0, -2.5)
        glColor3f(1, 1, 0)
        glPushMatrix()
        # glutWireSphere(0.5,50,10)
        glutSolidSphere(0.5, 50, 10)
        glPopMatrix()

        glTranslatef(0, 2, 0)
        glColor3f(1, 1, 0)
        glPushMatrix()
        # glutWireSphere(0.5,50,10)
        glutSolidSphere(0.5, 50, 10)
        glPopMatrix()

        glTranslatef(0, 0, 2.5)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(0.5,50,10)
        glutSolidSphere(0.5, 50, 10)
        glPopMatrix()

        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireCylinder(0.5,-2.5,50,10)
        glutSolidCylinder(0.5, -2.5, 50, 10)
        glPopMatrix()

        # hand
        glTranslatef(2.0, -2.3, -0.5)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(0.45,50,10)
        glutSolidSphere(0.45, 50, 10)
        glPopMatrix()

        glTranslatef(0, 2.8, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireSphere(0.45,50,10)
        glutSolidSphere(0.45, 50, 10)
        glPopMatrix()

        glRotate(90, 1, 1, 0)
        glTranslatef(0.05, 0.05, 0)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireCylinder(0.4,-1.5,50,10)
        glutSolidCylinder(0.4, -1.5, 50, 10)
        glPopMatrix()

        glTranslatef(0, 0, -1.5)
        glColor3f(1, 1, 0)
        glPushMatrix()
        # glutWireSphere(0.4,50,10)
        glutSolidSphere(0.4, 50, 10)
        glPopMatrix()

        glRotate(-90, 1, 1, 0)
        glTranslatef(1.0, -3.9, 0)
        glRotate(260, 1, 0, 1)
        glTranslatef(0.1, 0, 0.1)
        glColor3f(0.8, 0.5, 0.3)
        glPushMatrix()
        # glutWireCylinder(0.4,-1.5,50,10)
        glutSolidCylinder(0.4, -1.5, 50, 10)
        glPopMatrix()

        glTranslatef(0, 0, -1.5)
        glColor3f(1, 1, 0)
        glPushMatrix()
        # glutWireSphere(0.4,50,10)
        glutSolidSphere(0.4, 50, 10)
        glPopMatrix()

        glRotate(-260, 1, 0, 1)
        glTranslatef(-1.2, 2.42, 1.8)
        glColor3f(0.9, 0.6, 0.4)
        glPushMatrix()
        # glutWireSphere(0.3,50,10)
        glutSolidSphere(0.3, 50, 10)
        glPopMatrix()

        glColor3f(0, 0, 0)
        glBegin(GL_LINES)
        for i in range(4):
            glVertex3f(0.0, -0.02 + i / 100, 0.1)
            glVertex3f(2.0, -0.02 + i / 100, 0.1)

        for x in range(8):
            for y in range(4):
                glVertex3f(0.5 + x / 5 + y / 100, 0.08, 0.1)
                glVertex3f(0.5 + x / 5 + y / 100, -0.08, 0.1)
        glEnd()

def text():
    glColor3f(1,1,1)
    glRasterPos2f(20, 15)
    boxMotion = "Left mouse click to \"Remove Box Cover\" or \"Open Box\" or \"Close Box\" "
    for i in range(len(boxMotion)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(boxMotion[i]))

    objectMotion = ["Press key \"up\",\"down\",\"left\",\"right\" to rotate object ",
                    "Scroll mouse wheel to zoom in or zoom out"]
    for i in range(len(objectMotion)):
        glRasterPos2f(20, 520+i*40)
        for j in range(len(objectMotion[i])):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(objectMotion[i][j]))

def drawScene():
    global num,xRot,yRot
    global staticRot,xBefore,yBefore
    if xRot!=0 or yRot!=0 :
        staticRot=0
        glRotatef(rot, xRot,yRot,0)
    glRotatef(staticRot, xBefore, yBefore, 0)
    b=box(num)
    teddy=bear()
    b.draw()
    teddy.draw()


def CameraProp():
    """ method: Camera properties.. """
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)

def MouseWheel(button,dir,x,y):
    global zEye
    if dir>0:
        zEye+=1
    else:
        zEye-=1

def MouseMovement(x, y):
    """ method: Handling Mouse movements """

    global lastx
    global lasty
    global xrot, yrot

    diffx = x - lastx  # check the difference between the current x and the last x position
    diffy = y - lasty  # check the difference between the current y and the last  y position
    lastx = x  # set lastx to the current x position
    lasty = y  # set lasty to the current y position
    xrot += (float)(diffy)  # set the xrot to xrot  with the addition of the difference in the y position
    yrot += (float)(diffx)  # set the xrot to yrot with the addition of the difference in the x position

def Mouse(button,action,x,y):
    global num
    if (button == GLUT_LEFT_BUTTON and action == GLUT_DOWN) :
        num+=1
        if num>2:
            num=0

def SpecialInput(key,x,y):
    global rot,xRot,yRot
    global staticRot,xBefore,yBefore

    if xRot==0:
        if key==GLUT_KEY_RIGHT:
            if xBefore==-1:
                rot=-rot
            xRot=1
        elif key==GLUT_KEY_LEFT:
            if xBefore==1:
                rot=-rot
            xRot=-1
    elif xRot==1:
        if key==GLUT_KEY_RIGHT:
            staticRot = rot
            xBefore=xRot
            xRot=0
        elif key==GLUT_KEY_LEFT:
            rot=-rot
            xRot=-1
    elif xRot==-1:
        if key==GLUT_KEY_RIGHT:
            rot=-rot
            xRot=1
        elif key==GLUT_KEY_LEFT:
            staticRot = rot
            xBefore =xRot
            xRot = 0

    if yRot==0:
        if key==GLUT_KEY_DOWN:
            if yBefore==-1:
                rot=-rot
            yRot=1
        elif key==GLUT_KEY_UP:
            if yBefore==1:
                rot=-rot
            yRot=-1
    elif yRot==1:
        if key==GLUT_KEY_DOWN:
            staticRot = rot
            yBefore=yRot
            yRot=0
        elif key==GLUT_KEY_UP:
            rot=-rot
            yRot=-1
    elif yRot==-1:
        if key==GLUT_KEY_DOWN:
            rot=-rot
            yRot=1
        elif key==GLUT_KEY_UP:
            staticRot = rot
            yBefore =yRot
            yRot = 0

def KeyPressed(*args):
    """ method: If quit button is pressed, kill everything """
    if args[0] == b'q' or args[0] == b'Q':
        sys.exit()
    glutPostRedisplay()

# /* Initialize OpenGL Graphics */
def initGL():
   glClearColor(1.0, 0.0, 1.0, 1.0)  #  Set background color to magenta and opaque
   glClearDepth(1.0)  # Set background depth to farthest
   glEnable(GL_DEPTH_TEST)  # Enable depth testing for z-culling
   glDepthFunc(GL_LEQUAL)  # Set the type of depth-test
   glShadeModel(GL_SMOOTH)  # Enable smooth shading
   glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)  # Nice perspective corrections

def display():
    """ display """
    global rot,zEye
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear color and depth buffers
    glMatrixMode(GL_MODELVIEW)  # To operate on model-view matrix

    glLoadIdentity() # Reset the model-view matrix
    gluLookAt(0.0, 0.0,zEye, 0.0, 0.0, 0.0, 1000.0, 1.0, 1000.0)

    CameraProp()
    drawScene()

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0.0, 800, 0.0, 600)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    text()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glEnable(GL_TEXTURE_2D)

    glutSwapBuffers()
    rot = rot + 0.5

def reshape(width, height):
    if height == 0:  # Prevent A Divide By Zero If The Window Is Too Small
        height = 1
    glViewport(0, 0, (int)(width), (int)(height))
    # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)  # set it so we can play with the 'camera'
    glLoadIdentity()  # replace the current matrix with the Identity Matrix
    gluPerspective(40, (float)(width) / (float)(height), 0.1, 100.0)
    # set the angle of view, the ratio of sight, the near and far factors
    glMatrixMode(GL_MODELVIEW)  # switch back the the model editing mode.

def main():
    glutInit(sys.argv)  # initialize the program.
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)  # window size
    glutInitWindowPosition(100, 50)  # window position
    glutCreateWindow(b"Happy Birthday")  # show window
    glutDisplayFunc(display)
    glutIdleFunc(display)  # to set loop cycle for primitive
    glutReshapeFunc(reshape)
    glutKeyboardFunc(KeyPressed)  # to new function to invoke Keyboard facilities
    glutSpecialFunc(SpecialInput)
    glutMouseFunc(Mouse)
    glutPassiveMotionFunc(MouseMovement)
    glutMouseWheelFunc(MouseWheel)
    initGL()
    glutMainLoop()  # initialize the OpenGL loop cycle

if __name__ == "__main__":
    main()
