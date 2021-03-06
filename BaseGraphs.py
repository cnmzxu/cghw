from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

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

def drawUnfilledPolygon(polygon):
    for i in range(len(polygon)//2 - 1):
        drawLine((int(polygon[2 * i]), int(polygon[2 * i + 1])), (int(polygon[2 * i + 2]), int(polygon[2 * i + 3])))
    drawLine((int(polygon[-2]), int(polygon[-1])), (int(polygon[0]), int(polygon[1])))

def drawFilledPolygon(polygon, color):
    lines = []
    polygon = [int(num) for num in polygon]
    color = [float(c) for c in color]
    for i in range(len(polygon) // 2 - 1):
        if (polygon[2 * i] < polygon[2 * i + 2]):
            lines.append((polygon[2 * i], polygon[2 * i + 1], polygon[2 * i + 2], polygon[2 * i + 3]))
        elif (polygon[2 * i] > polygon[2 * i + 2]):
            lines.append((polygon[2 * i + 2], polygon[2 * i + 3], polygon[2 * i], polygon[2 * i + 1]))

    if (polygon[0] > polygon[-2]):
        lines.append((polygon[-2], polygon[-1], polygon[0], polygon[1]))
    elif (polygon[0] < polygon[-2]):
        lines.append((polygon[0], polygon[1], polygon[-2], polygon[-1]))

    xmin = min([polygon[2 * i] for i in range(len(polygon) // 2)])
    xmax = max([polygon[2 * i] for i in range(len(polygon) // 2)])
    
    intersections = [0] * len(lines)
    counter = [0] * len(lines)

    lines = sorted(lines)
    nowx = xmin
    
    intersectedlines = []
    ttemp = 0

    glBegin(GL_POINTS)
    if (len(color) == 3):
        glColor3f(color[0], color[1], color[2])
    else:
        glColor4f(color[0], color[1], color[2], color[3])

    while nowx != xmax:
        intersectedlines = [x for x in filter(lambda x:lines[x][2] >= nowx, intersectedlines)]
        
        for i in intersectedlines:
            dy = lines[i][3] - lines[i][1]
            dx = lines[i][2] - lines[i][0]
            counter[i] = counter[i] + dy
            nowdy = counter[i]
            if nowdy == 0:
                flag = 1
            else:
                flag = nowdy // abs(nowdy)
            nowdy = abs(nowdy)
            if nowdy >= dx:
                intersections[i] += flag * (nowdy // dx)
                counter[i] = flag * (nowdy % dx)

        while True:
            if ttemp >= len(lines) or lines[ttemp][0] > nowx:
                break
            intersectedlines.append(ttemp)
            intersections[ttemp] = lines[ttemp][1]
            ttemp += 1
  
        intersectedlines = sorted(intersectedlines, key = lambda i:intersections[i])

        nowy = intersections[intersectedlines[0]]
        ymax = intersections[intersectedlines[-1]]
        
        t = 0
        temp = 0
        while nowy <= ymax:
            while True:
                if temp >= len(intersectedlines):
                    break
                linenum = intersectedlines[temp]
                if intersections[linenum] != nowy:
                    break
                if lines[linenum][0] < nowx:
                    t += 1
                if lines[linenum][2] < nowx:
                    t += 1
                temp += 1
            if t % 2 == 1:
                glVertex2i(nowx, nowy)            
            nowy += 1

        nowx += 1
    glEnd()

def BezierSpline(nodes):
    nodes = [int(node) for node in nodes]
    x = [nodes[2 * i] for i in range(len(nodes) // 2)]
    y = [nodes[2 * i + 1] for i in range(len(nodes) // 2)]
    
    n = len(x)
    
    def drawspline(x1, y1, x2, y2, x3, y3, x4, y4):
        glColor3f(1, 0, 0)
        if (x1 >=0 and y1 >= 0):
            glVertex2f(x1, y1)
        if (x2 >=0 and y2 >= 0):
            glVertex2f(x2, y2)
        if (x3 >=0 and y3 >= 0):
            glVertex2f(x3, y3)
        if (x4 >=0 and y4 >= 0):
            glVertex2f(x4, y4)
        glColor3f(1, 1, 1)
        if (abs(x1 - x2) <= 1 and abs(x1 - x3) <= 1 and abs(x1 - x4) <= 1 and abs(y1 - y2) <= 1 and abs(y1 - y3) <= 1 and abs(y1 - y4) <= 1):
            if (x1 >=0 and y1 >= 0):
                glVertex2f(x1, y1)
            if (x2 >=0 and y2 >= 0):
                glVertex2f(x2, y2)
            if (x3 >=0 and y3 >= 0):
                glVertex2f(x3, y3)
            if (x4 >=0 and y4 >= 0):
                glVertex2f(x4, y4)
            return
        else:
            x11 = (x1 + x2) / 2
            x12 = (x2 + x3) / 2
            x13 = (x3 + x4) / 2
            x21 = (x11 + x12) / 2
            x22 = (x12 + x13) / 2
            x31 = (x21 + x22) / 2
            
            y11 = (y1 + y2) / 2
            y12 = (y2 + y3) / 2
            y13 = (y3 + y4) / 2
            y21 = (y11 + y12) / 2
            y22 = (y12 + y13) / 2
            y31 = (y21 + y22) / 2
            
            if (x31 >= 0 and y31 >= 0):
                glVertex2f(x31, y31)
            drawspline(x1, y1, x11, y11, x21, y21, x31, y31)
            drawspline(x31, y31, x22, y22, x13, y13, x4, y4)
    
    y1 = y[0]
    y2 = y[1]
    y3 = y[2]
    y4 = y[3]
    
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    nown = 3
    glBegin(GL_POINTS)
    while nown < n:
        x4 = x[nown]
        y4 = y[nown]
        nown += 1
        drawspline(x1, y1, x2, y2, x3, y3, x4, y4)
        x1, y1 = x4, y4
        x2, y2 = x4 + x4 - x3, y4 + y4 -y3
        x3, y3 = x2 + 4 * (x4 - x3), y2 + 4 * (y4 - y3)
    glEnd()
