from pygame.constants import *
from objloader import *

rot = 0.0
# mouse parameter
lastx = lasty = 0.0
xrot = 0.0
yrot = 0.0
# object rotate
xRot=0
yRot=0
# eye z
zEye=50
# static mode
staticRot=0
xBefore=0
yBefore=0

class MINION:
    def __init__(self):
        self.baju=OBJ("minion_baju.obj")
        self.body=OBJ("minion_body.obj")
        self.hand=OBJ("minion_hand.obj")
        self.kasut=OBJ("minion_kasut.obj")
        self.spec=OBJ("minion_spec.obj")

    def display(self):
        glTranslate(0, 7, 0)
        glCallList(self.baju.gl_list)
        glCallList(self.body.gl_list)
        glCallList(self.hand.gl_list)
        glCallList(self.kasut.gl_list)
        glCallList(self.spec.gl_list)
        glLineWidth(5)
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(4.5, 3.5, -2)
        glVertex3f(-4.5, 3.5, -2)
        glVertex3f(-4.5, -4, -2)
        glVertex3f(4.5, -4, -2)
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(4.5, 3.5, -2)
        glVertex3f(4.5, 3.5, 2)
        glVertex3f(-4.5, 3.5, -2)
        glVertex3f(-4.5, 3.5, 2)
        glVertex3f(-4.5, -4, -2)
        glVertex3f(-4.5, -4, 2)
        glVertex3f(4.5, -4, -2)
        glVertex3f(4.5, -4, 2)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glVertex3f(4.5, 3.5, 2)
        glVertex3f(-4.5, 3.5, 2)
        glVertex3f(-4.5, -4, 2)
        glVertex3f(4.5, -4, 2)
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(-4.5, -4, 0)
        glVertex3f(-8, -6, 0)

        glVertex3f(4.5, -4, 0)
        glVertex3f(8, -6, 0)
        glEnd()

        glTranslate(8, -8, 0)
        glCallList(self.baju.gl_list)
        glCallList(self.hand.gl_list)
        glCallList(self.kasut.gl_list)
        glCallList(self.spec.gl_list)
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(4.5, 2, -2)
        glVertex3f(-4.5, 2, -2)
        glVertex3f(-4.5, -5, -2)
        glVertex3f(4.5, -5, -2)
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(4.5, 2, -2)
        glVertex3f(4.5, 2, 2)
        glVertex3f(-4.5, 2, -2)
        glVertex3f(-4.5, 2, 2)
        glVertex3f(-4.5, -5, -2)
        glVertex3f(-4.5, -5, 2)
        glVertex3f(4.5, -5, -2)
        glVertex3f(4.5, -5, 2)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glVertex3f(4.5, 2, 2)
        glVertex3f(-4.5, 2, 2)
        glVertex3f(-4.5, -5, 2)
        glVertex3f(4.5, -5, 2)
        glEnd()

        glBegin(GL_LINES)
        glVertex3f(-4.5, -5, 0)
        glVertex3f(-24, -8, 0)

        glVertex3f(-4.5, -5, 0)
        glVertex3f(-16, -8, 0)

        glVertex3f(4.5, -5, 0)
        glVertex3f(-4.5, -8, 0)

        glVertex3f(4.5, -5, 0)
        glVertex3f(8, -8, 0)
        glEnd()

        glTranslate(-16, -1, 0)
        glCallList(self.body.gl_list)
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(4.5, 3, -2)
        glVertex3f(-4.5, 3, -2)
        glVertex3f(-4.5, -4, -2)
        glVertex3f(4.5, -4, -2)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(4.5, 3, -2)
        glVertex3f(4.5, 3, 2)
        glVertex3f(-4.5, 3, -2)
        glVertex3f(-4.5, 3, 2)
        glVertex3f(-4.5, -4, -2)
        glVertex3f(-4.5, -4, 2)
        glVertex3f(4.5, -4, -2)
        glVertex3f(4.5, -4, 2)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glVertex3f(4.5, 3, 2)
        glVertex3f(-4.5, 3, 2)
        glVertex3f(-4.5, -4, 2)
        glVertex3f(4.5, -4, 2)
        glEnd()

        glTranslate(24, -7, 0)
        glCallList(self.baju.gl_list)
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(3, 0, -2)
        glVertex3f(-3, 0, -2)
        glVertex3f(-3, -4, -2)
        glVertex3f(3, -4, -2)
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(3, 0, -2)
        glVertex3f(3, 0, 2)
        glVertex3f(-3, 0, -2)
        glVertex3f(-3, 0, 2)
        glVertex3f(-3, -4, -2)
        glVertex3f(-3, -4, 2)
        glVertex3f(3, -4, -2)
        glVertex3f(3, -4, 2)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glVertex3f(3, 0, 2)
        glVertex3f(-3, 0, 2)
        glVertex3f(-3, -4, 2)
        glVertex3f(3, -4, 2)
        glEnd()

        glTranslate(-12, -1, 0)
        glCallList(self.hand.gl_list)
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(4.5, 1, -2)
        glVertex3f(-4.5, 1, -2)
        glVertex3f(-4.5, -3, -2)
        glVertex3f(4.5, -3, -2)
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(4.5, 1, -2)
        glVertex3f(4.5, 1, 2)
        glVertex3f(-4.5, 1, -2)
        glVertex3f(-4.5, 1, 2)
        glVertex3f(-4.5, -3, -2)
        glVertex3f(-4.5, -3, 2)
        glVertex3f(4.5, -3, -2)
        glVertex3f(4.5, -3, 2)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glVertex3f(4.5, 1, 2)
        glVertex3f(-4.5, 1, 2)
        glVertex3f(-4.5, -3, 2)
        glVertex3f(4.5, -3, 2)
        glEnd()

        glTranslate(-12, 2, 0)
        glCallList(self.kasut.gl_list)
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(2, -1, -2)
        glVertex3f(-2, -1, -2)
        glVertex3f(-2, -5, -2)
        glVertex3f(2, -5, -2)
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(2, -1, -2)
        glVertex3f(2, -1, 2)
        glVertex3f(-2, -1, -2)
        glVertex3f(-2, -1, 2)
        glVertex3f(-2, -5, -2)
        glVertex3f(-2, -5, 2)
        glVertex3f(2, -5, -2)
        glVertex3f(2, -5, 2)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glVertex3f(2, -1, 2)
        glVertex3f(-2, -1, 2)
        glVertex3f(-2, -5, 2)
        glVertex3f(2, -5, 2)
        glEnd()

        glTranslate(-8, -3.5, 0)
        glCallList(self.spec.gl_list)
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(3, 2.5, -2)
        glVertex3f(-3, 2.5, -2)
        glVertex3f(-3, -1.5, -2)
        glVertex3f(3, -1.5, -2)
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(3, 2.5, -2)
        glVertex3f(3, 2.5, 2)
        glVertex3f(-3, 2.5, -2)
        glVertex3f(-3, 2.5, 2)
        glVertex3f(-3, -1.5, -2)
        glVertex3f(-3, -1.5, 2)
        glVertex3f(3, -1.5, -2)
        glVertex3f(3, -1.5, 2)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glVertex3f(3, 2.5, 2)
        glVertex3f(-3, 2.5, 2)
        glVertex3f(-3, -1.5, 2)
        glVertex3f(3, -1.5, 2)
        glEnd()

def text():
    glColor3f(0,0,0)
    objectMotion = ["Press key \"up\",\"down\",\"left\",\"right\" to rotate object ",
                    "Scroll mouse wheel to zoom in or zoom out"]
    for i in range(len(objectMotion)):
        glRasterPos2f(20, 540+i*30)
        for j in range(len(objectMotion[i])):
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(objectMotion[i][j]))

def InitLighting():
    mat_specular = [1.0, 1.0, 1.0, 1.0]
    mat_shininess = [50.0]
    light_position = [1.0, 1.5, 1.0, 0.0]
    light_diffuse = [0.8, 1.0, 0.8, 1.0]  # green tinged
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_SMOOTH)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

def CameraProp():
    """ method: Camera properties.. """
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)

def main():
    pygame.init()
    glutInit(sys.argv)  # initialize the program.
    viewport = (800, 600)
    pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
    pygame.display.set_caption("minion")

    glLightfv(GL_LIGHT0, GL_POSITION, (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)  # most obj files expect to be smooth-shaded

    # LOAD OBJECT AFTER PYGAME INIT
    object = MINION()

    clock = pygame.time.Clock()

    width, height = viewport
    glViewport(0, 0, (int)(width), (int)(height))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40.0, width / float(height), 1, 100.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)

    while 1:
        global rot,zEye
        global xRot, yRot
        global staticRot, xBefore, yBefore
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    if xRot==0:
                        if xBefore == 1:
                            rot = -rot
                        xRot=-1
                    elif xRot==1:
                        rot = -rot
                        xRot = -1
                    elif xRot==-1:
                        staticRot = rot
                        xBefore = xRot
                        xRot = 0
                elif e.key == pygame.K_DOWN:
                    if xRot == 0:
                        if xBefore == -1:
                            rot = -rot
                        xRot = 1
                    elif xRot == 1:
                        staticRot = rot
                        xBefore = xRot
                        xRot = 0
                    elif xRot == -1:
                        rot = -rot
                        xRot = 1
                elif e.key == pygame.K_LEFT:
                    if yRot==0:
                        if yBefore == 1:
                            rot = -rot
                        yRot = -1
                    elif yRot==1:
                        rot = -rot
                        yRot = -1
                    elif yRot == -1:
                        staticRot = rot
                        yBefore = yRot
                        yRot = 0
                elif e.key == pygame.K_RIGHT:
                    if yRot==0:
                        if yBefore == -1:
                            rot = -rot
                        yRot = 1
                    elif yRot == 1:
                        staticRot = rot
                        yBefore = yRot
                        yRot = 0
                    elif yRot == -1:
                        rot = -rot
                        yRot = 1
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 4:
                    zEye-=1
                elif e.button == 5:
                    zEye+=1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0.0, 0.0, zEye, 0.0, 0.0, 0.0, 1000.0, 1.0, 1000.0)

        CameraProp()
        InitLighting()
        # RENDER OBJECT
        glRotate(90,0,0,-1)
        if xRot != 0 or yRot != 0:
            staticRot = 0
            glRotate(rot, xRot, yRot, 0)
        glRotate(staticRot, xBefore, yBefore, 0)
        object.display()

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

        rot +=1

        glClearColor(0.5, 0.5, 0.5, 1.0)  # Set background color to grey and opaque
        glClearDepth(1.0)  # Set background depth to farthest
        glEnable(GL_DEPTH_TEST)  # Enable depth testing for z-culling
        glDepthFunc(GL_LEQUAL)  # Set the type of depth-test
        glShadeModel(GL_SMOOTH)  # Enable smooth shading
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)  # Nice perspective corrections
        clock.tick(30)
        pygame.display.flip()


if __name__ == "__main__":
    main()