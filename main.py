from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from BaseGraphs import *
import threading
HEIGHT = 480
WIDTH = 680
POINTS = []
LINES = []
ELLIPSES = []

def init():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("test")
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, WIDTH, 0, HEIGHT)

def draw():
    global POINTS, LINES, ELLIPSES
    glClear(GL_COLOR_BUFFER_BIT)
    for point in POINTS:
        drawPoint(point)
    for line in LINES:
        drawLine(line[0], line[1])
    for ellipse in ELLIPSES:
        drawEllipse(ellipse[0], ellipse[1])
    glFlush()

def inputLoop():
    global POINTS, LINES, ELLIPSES
    cmds = {"point" : lambda arg: POINTS.append((int(arg[0]), int(arg[1]))), 
            "line" : lambda arg: LINES.append(((int(arg[0]), int(arg[1])), (int(arg[2]), int(arg[3])))),
            "ellipse" : lambda arg: ELLIPSES.append(((int(arg[0]), int(arg[1])),(int(arg[2]), int(arg[3])))),
            "quit" : lambda arg: exit(0)}
    while(True):
        cmd = input(">>")
        cmd = cmd.split()
        cmds.get(cmd[0], lambda arg: print("no such command"))(cmd[1:])


t = threading.Thread(target = inputLoop)
t.start()

init()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()

