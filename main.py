from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from DrawGraphs import *
import threading
HEIGHT = 480
WIDTH = 680

def init():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("test")
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, WIDTH, 0, HEIGHT)

def inputLoop():
    cmds = {"help" : myhelp,
            "point" : add_point,
            "line" : add_line,
            "ellipse" : add_ellipse,
            "polygon" : add_polygon,
            "filledpolygon": add_filled_polygon,
            "spline" : add_splines,
            "clear" : clear
            }
    print("You can type 'help' for some help.")
    while(True):
        cmd = input(">>")
        cmd = cmd.split()
        def error(args):
            print("No Such Command!")
        cmds.get(cmd[0], error)(cmd[1:])


t = threading.Thread(target = inputLoop)
t.start()
init()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()

