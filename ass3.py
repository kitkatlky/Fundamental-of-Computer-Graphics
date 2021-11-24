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
zEye=10
# static mode
staticRot=0
xBefore=0
yBefore=0

class bear:
    def __init__(self):
        self.dango=OBJ("dango.OBJ")
        self.left_1=OBJ("dango1.obj")
        self.left_2=OBJ("dango2.obj")
        self.empty=OBJ("empty.obj")
        self.hand=OBJ("hand.obj")
        self.ready=OBJ("ready.obj")
        self.state=0
        self.up=-1
        self.down=0
        self.left=0
        self.right=0

    def display(self):
        glTranslate(3, -1, 0)
        glCallList(self.ready.gl_list)
        glRotate(10,0,0,-1)
        self.eat()
        glRotate(10, 0, 0, 1)
        glTranslate(-3, 2, 0)
        glCallList(self.ready.gl_list)
        glTranslate(0, -2, 0)
        glLineWidth(10)
        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(3, 0, 0)
        glVertex3f(0, 0, 0.2)

        glVertex3f(0, 1, 0.2)
        glVertex3f(0, 0, 0.2)
        glVertex3f(0, 0, 0.2)
        glVertex3f(-0.35, -1, 0.3)

        glVertex3f(-0.5, -1.5, 0.4)
        glVertex3f(-1.0, -1.5, 0.4)

        glVertex3f(-1.0, -1.5, 0.4)
        glVertex3f(-2.5, 0, 0.3)

        glVertex3f(-1.0, -1.5, 0.4)
        glVertex3f(-2.5, -1.8, 0.7)
        glEnd()
        glTranslate(0, -1, 0)
        self.eat()
        glTranslate(-2, 1, 0)
        glCallList(self.hand.gl_list)
        glTranslate(0, -1, 0)
        glCallList(self.dango.gl_list)

    def eat(self):
        if self.state==0:
            glCallList(self.hand.gl_list)
            glCallList(self.dango.gl_list)
        elif self.state==1:
            if self.up>-1 and self.up<30:
                glRotate(self.up, -1, 0, 0)
                glCallList(self.hand.gl_list)
                glCallList(self.dango.gl_list)
                self.up+=1
                self.down=self.up
            else:
                if self.down>0:
                    glRotate(self.down, -1, 0, 0)
                    glCallList(self.hand.gl_list)
                    glCallList(self.left_2.gl_list)
                    self.down -= 1
                else:
                    self.degree = -1
                    glCallList(self.hand.gl_list)
                    glCallList(self.left_2.gl_list)
        elif self.state==2:
            if self.up > -1 and self.up < 35:
                glRotate(self.up, -1, 0, 0)
                glCallList(self.hand.gl_list)
                glCallList(self.left_2.gl_list)
                self.up += 1
                self.down = self.up
            else:
                if self.down > 0:
                    glRotate(self.down, -1, 0, 0)
                    glCallList(self.hand.gl_list)
                    glCallList(self.left_1.gl_list)
                    self.down -= 1
                else:
                    self.up = -1
                    glCallList(self.hand.gl_list)
                    glCallList(self.left_1.gl_list)
        elif self.state==3:
            if self.up > -1 and self.up < 45:
                glRotate(self.up, -1, 0, 0)
                glCallList(self.hand.gl_list)
                glCallList(self.left_1.gl_list)
                self.up += 1
                self.down = self.up
            else:
                if self.down > 0:
                    glRotate(self.down, -1, 0, 0)
                    glCallList(self.hand.gl_list)
                    glCallList(self.empty.gl_list)
                    self.down -= 1
                else:
                    self.up = -1
                    glCallList(self.hand.gl_list)
                    glCallList(self.empty.gl_list)

def text():
    glColor3f(0,0,0)
    glRasterPos2f(20, 15)
    bearMotion = "Press spacebar to make the motion of food "
    for i in range(len(bearMotion)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(bearMotion[i]))

    objectMotion = ["Press key \"up\",\"down\",\"left\",\"right\" to rotate object ",
                    "Scroll mouse wheel to zoom in or zoom out"]
    for i in range(len(objectMotion)):
        glRasterPos2f(20, 520+i*40)
        for j in range(len(objectMotion[i])):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(objectMotion[i][j]))

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

def main():
    pygame.init()
    glutInit(sys.argv)  # initialize the program.
    viewport = (800, 600)
    pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
    pygame.display.set_caption("Load 3D")

    glLightfv(GL_LIGHT0, GL_POSITION, (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)  # most obj files expect to be smooth-shaded

    # LOAD OBJECT AFTER PYGAME INIT
    object = bear()

    clock = pygame.time.Clock()
    sound=pygame.mixer.Sound("slip.wav")

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
                if e.key == pygame.K_SPACE:
                    sound.play()
                    object.up = 0
                    object.state+=1
                    if object.state>3:
                        object.state=0
                elif e.key == pygame.K_UP:
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

        x,y=pygame.mouse.get_pos()
        MouseMovement(x,y)

        glClearColor(1.0, 0.0, 1.0, 1.0)  # Set background color to magenta and opaque
        glClearDepth(1.0)  # Set background depth to farthest
        glEnable(GL_DEPTH_TEST)  # Enable depth testing for z-culling
        glDepthFunc(GL_LEQUAL)  # Set the type of depth-test
        glShadeModel(GL_SMOOTH)  # Enable smooth shading
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)  # Nice perspective corrections
        clock.tick(30)
        pygame.display.flip()


if __name__ == "__main__":
    main()