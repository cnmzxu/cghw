from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from BaseGraphs import *
import time

HEIGHT = 690
WIDTH = 1390

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, WIDTH, 0, HEIGHT)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    i = 0
    drawEllipse((10, 10), (1380, 680))
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

