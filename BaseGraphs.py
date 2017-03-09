from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawPoint(point):
    glBegin(GL_POINTS)
    glVertex2fv(point)
    glEnd()

def drawLine(vert1, vert2):
    #use Bresenham Algorithm
    x1, y1, x2, y2 = vert1[0], vert1[1], vert2[0], vert2[1]
    if x1 > x2:
        x1, x2 = x2, x1
        vert1, vert2 = vert2, vert1
    if y1 > y2:
        y1, y2 = y2, y1
    dx = x2 - x1
    dy = y2 - y1
    if dx < dy:
        x1, x2, y1, y2, dx, dy = y1, y2, x1, x2, dy ,dx
    yList = [y1]
    y = y1
    p = 2 * dy - dx
    for x in range(x1, x2):
        if p > 0:
            p += 2 * (dy - dx)
            y += 1
            yList.append(y)
        else:
            p += 2 * dy
            yList.append(y)
    
    dx = vert2[0] - vert1[0]
    dy = vert2[1] - vert1[1]
    glBegin(GL_POINTS)
    for x in range(x1, x2 + 1):
        if dy >= 0:
            if abs(dx) >= abs(dy):
                glVertex2i(x, yList[x - x1])
            else:
                glVertex2i(yList[x - x1], x)
        else:
            if abs(dx) >= abs(dy):
                glVertex2i(x, y1 + y2 - yList[x - x1])
            else:
                glVertex2i(yList[x - x1], x1 + x2 - x)
    glEnd()

def drawPolyv(args):
    for i in range(len(args) - 1):
        drawLine(args[i], args[i + 1])
    drawLine(args[-1], args[0])

def drawPoly(*args):
    drawPolyv(args)

def drawEllipse(vert1, vert2):
    x1, y1, x2, y2 = vert1[0], vert1[1], vert2[0], vert2[1]
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    a = (x2 - x1) // 2
    b = (y2 - y1) // 2
    dx = (x2 + x1 + 1) // 2
    dy = (y2 + y1 + 1) // 2
    glBegin(GL_POINTS)
    x = 0
    y = b
    p = b * b - a * a * b + (a * a) // 4
    while(True):
        glVertex2i(x + dx, y + dy)
        glVertex2i(-x + dx, y + dy)
        glVertex2i(x + dx, -y + dy)
        glVertex2i(-x + dx, -y + dy)
        if b * b * x >= a * a * y:
            break
        if p < 0:
            p += b * b * (2 * x + 3)
            x += 1
        else:
            p += b * b * (2 * x + 3) - 2 * a * a * (y - 1)
            x += 1
            y -= 1
    
    x = a
    y = 0
    p = a * a - b * b * a + (b * b) // 4
    while(True):
        glVertex2i(x + dx, y + dy)
        glVertex2i(-x + dx, y + dy)
        glVertex2i(x + dx, -y + dy)
        glVertex2i(-x + dx, -y + dy)
        if a * a * y > b * b * x:
            break
        if p < 0:
            p += a * a * (2 * y + 3)
            y += 1
        else:
            p += a * a * (2 * y + 3) - 2 * b * b * (x - 1)
            y += 1
            x -= 1
        
    glEnd()
