from BaseGraphs import *

POINTS = []
LINES = []
ELLIPSES = []
FILLEDPOLYGONS = []
POLYGONS = []
SPLINES = []

HELP = """
Commands:
    help:             Print help information
    point:            Need 2 agrues x, y. Draw a point in (x, y)
    line:             Need 4 argues x1, y1, x2, y2. Draw a line between (x1, y1) and (x2, y2)
    ellipse:          Need 4 argues x1, y1, x2, y2. Draw a ellipse in (x1, y1) and (x2, y2)
    filledpolygon:    Need 3 RGB values and more than 6 argues x1, y1, x2, y2, x3, y3... Draw a filled polygon
    polygon:          Need more than 6 argues x1, y1, x2, y2, x3, y3... Draw a polygon with lines
    spline:           Need more than 8 argues x1, y1, x2, y2, x3, y3, x4, y4... Draw a spline
    clear:            Clear the graph
"""

def draw():
    global POINTS, LINES, ELLIPSES, POLYGONS, UNFILLEDPOLYGONS, SPLLINES
    glClear(GL_COLOR_BUFFER_BIT)
    for point in POINTS:
        drawPoint((int(point[0]), int(point[1])))
    for line in LINES:
        drawLine((int(line[0]), int(line[1])), (int(line[2]), int(line[3])))
    for ellipse in ELLIPSES:
        drawEllipse((int(ellipse[0]), int(ellipse[1])), (int(ellipse[2]), int(ellipse[3])))
    for polygon in POLYGONS:
        drawUnfilledPolygon(polygon)
    for polygon in FILLEDPOLYGONS:
        drawFilledPolygon(polygon[0], polygon[1])
    for spline in SPLINES:
        BezierSpline(spline)
    
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

def add_filled_polygon(args):
    global FILLEDPOLYGONS
    if (len(args) % 2 != 1 or len(args) < 9):
        print("args error")
    else:
        FILLEDPOLYGONS.append((args[3:], args[0:3]))

@check_arg_num("mt", 8)
def add_splines(args):
    global SPLINES
    SPLINES.append(args)


def clear(args):
    global POINTS, LINES, ELLIPSES, POLYGONS, FILLEDPOLYGONS, SPLINES
    POINTS, LINES, ELLIPSES, POLYGONS, FILLEDPOLYGONS, SPLINES = [], [], [], [], [], []

def myhelp(args):
    print(HELP)
