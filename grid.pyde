'''Grid for graphing'''

def setup():
    size(600,600)
    
rangex = 21
rangey = 21
    
def draw():
    global xscl, yscl
    background(255)
    xscl = width/rangex
    yscl = -height/rangey
    translate(width/2,height/2)
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(-10,11):
        line(i*xscl,-10*yscl,i*xscl,10*yscl)
        line(-10*xscl,i*yscl, 10*xscl,i*yscl)
        
    stroke(0) #black axes
    line(0,-10*yscl,0,10*yscl)
    line(-10*xscl,0, 10*xscl,0)
    fill(0)
    graphFunction()
    
def f(x):
    return 0.03*x**3 - 0.02*x + 2

def graphFunction():
    global xscl, yscl
    x = -10
    while x <= 10:
        stroke(255,0,0) #red function
        line(x*xscl,f(x)*yscl,(x+0.1)*xscl,f(x+0.1)*yscl)
        x += 0.1
    
def graphPoints(pointList):
    '''Graphs the points in a list'''
    for p in pointList:
        point(p[0]*xscl,p[1]*yscl)


def graphFunction():
    global xscl, yscl
    x = -10
    while x <= 10:
        stroke(255,0,0) #red function
        line(x*xscl,f(x)*yscl,(x+0.1)*xscl,f(x+0.1)*yscl)
        x += 0.1

a = list() #or a = []

for i in range(-10,11):
    a.append([i,2*i+5])
    
def graphPoints(pointList):
    '''Graphs the points in a list'''
    for p in pointList:
        point(p[0]*xscl,p[1]*yscl)
    
def graphPoints2(pointList):
    '''Graphs the points in a list using segments'''
    for i,p in enumerate(pointList):
        if i<len(pointList)-1:
            line(p[0]*xscl,p[1]*yscl,pointList[i+1][0]*xscl,pointList[i+1][1]*yscl)


def arange(start,stop,step):
    output = []
    x = start
    while x < stop:
        output.append(x)
        x += step
    return output


def graphx(x):
    '''converting point to canvas form'''
    return x * width/rangex

def graphy(y):
    '''convert y-coord to canvas form'''
    return y * height/rangey


    
