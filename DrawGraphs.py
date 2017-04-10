from BaseGraphs import *

POINTS = []
LINES = []
ELLIPSES = []
POLYGONS = []

HELP = """
Commands:
    help:       Print help information
    point:      Need 2 agrues x, y. Draw a point in (x, y)
    line:       Need 4 argues x1, y1, x2, y2. Draw a line between (x1, y1) and (x2, y2)
    ellipse:    Need 4 argues x1, y1, x2, y2. Draw a ellipse in (x1, y1) and (x2, y2)
    polygon:    Need more than 6 argues x1, y1, x2, y2, x3, y3. Draw a polygon
    clear:      Clear the graph
"""

def draw():
    global POINTS, LINES, ELLIPSES, POLYGONS
    glClear(GL_COLOR_BUFFER_BIT)
    for point in POINTS:
        drawPoint((int(point[0]), int(point[1])))
    for line in LINES:
        drawLine((int(line[0]), int(line[1])), (int(line[2]), int(line[3])))
    for ellipse in ELLIPSES:
        drawEllipse((int(ellipse[0]), int(ellipse[1])), (int(ellipse[2]), int(ellipse[3])))
    for polygon in POLYGONS:
        for i in range(len(polygon)//2 - 1):
            drawLine((int(polygon[2 * i]), int(polygon[2 * i + 1])), (int(polygon[2 * i + 2]), int(polygon[2 * i + 3])))
        drawLine((int(polygon[-2]), int(polygon[-1])), (int(polygon[0]), int(polygon[1])))
    glFlush()

def check_arg_num(mode, n):
    def decorator(func):
        def wrapper(args):
            def error(args):
                print("args error")
            if (mode == "lt" and (len(args) > n or len(args) % 2 != 0)):
                return error(args)
            if (mode == "mt" and (len(args) < n or len(args) % 2 != 0)):
                return error(args)
            if (mode == "eq" and len(args) != n):
                return error(args)
            return func(args)
        return wrapper
    return decorator

@check_arg_num("eq", 2)
def add_point(args):
    global POINTS
    POINTS.append(tuple(args))

@check_arg_num("eq", 4)
def add_line(args):
    global LINES
    LINES.append(tuple(args))

@check_arg_num("eq", 4)
def add_ellipse(args):
    global ELLIPSES
    ELLIPSES.append(tuple(args))

@check_arg_num("mt", 6)
def add_polygon(args):
    global POLYGONS
    POLYGONS.append(tuple(args))

def clear(args):
    global POINTS, LINES, ELLIPSES, POLYGONS
    POINTS, LINES, ELLIPSES, POLYGONS = [], [], [], []

def myhelp(args):
    print(HELP)
