from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from BaseGraphs import *
import time

HEIGHT = 480
WIDTH = 680

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, WIDTH, 0, HEIGHT)

Lines = [(0, 0), (100, 100), (200, 300), (400, 233), (600, 133)]

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    i = 0
    drawPolyv(Lines)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(100, 100)
glutCreateWindow("test")
init()

glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()

