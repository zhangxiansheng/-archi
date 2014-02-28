import math

#output a center point between two points;tuple
def cen(px,py):
    return(((px[0]+py[0])*0.5,(px[1]+py[1])*0.5))

#output a center point between two points;return int tuple
def cenint(px,py):
    return(((px[0]+py[0])/2,(px[1]+py[1])/2))

#output center point of up,down,left,right side;tuple
def sidecenter(p):
    p1,p2,p3,p4=p[0],p[1],p[2],p[3]
    return((cen(p2,p3),cen(p1,p4),cen(p1,p2),cen(p3,p4)))

#cross the y axiel
#y=a*x+b->b=y-a*x
def crossy(angle,point):
    a=math.tan(math.radians(angle))
    b=point[1]-a*point[0]
    return b

#cross the x axiel
#x=a*y+b->b=x-a*y
def crossx(angle,point):
    a=math.cos(math.radians(angle))/math.sin(math.radians(angle))
    b=point[0]-a*point[1]
    return b

#distance between two lines
def distance_y(angle,b1,b2):
    return abs((b1-b2)*math.cos(angle))

#distance between two lines
def distance_x(angle,b1,b2):
    return abs((b1-b2)*math.sin(angle))

#distance between two points[x1,y1][x2,y2]
def dis_lianbiao(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

#adjustwo
def adjustwo(angle,b,p):
    a=math.tan(math.radians(angle))
    x0,y0=p[0],p[1]
    x=(a*y0+x0-a*b)/(a*a+1)
    y=a*x+b
    return (x,y)

#adjustwo_
def adjustwo_(angle,b,p):
    a=math.cos(math.radians(angle))/math.sin(math.radians(angle))
    x0,y0=p[0],p[1]
    y=(a*x0+y0-a*b)/(a*a+1)
    x=a*y+b
    return (x,y)

#adjust two points
def adjust(angle,bb,tuple,side):
    p0,p1,p2,p3=tuple[0],tuple[1],tuple[2],tuple[3]
    if side==1:
        p1,p2=adjustwo(angle,bb,tuple[1]),adjustwo(angle,bb,tuple[2])
    elif side==2:
        p0,p3=adjustwo(angle,bb,tuple[0]),adjustwo(angle,bb,tuple[3])
    elif side==3:
        p0,p1=adjustwo_(angle,bb,tuple[0]),adjustwo_(angle,bb,tuple[1])
    else:
        p2,p3=adjustwo_(angle,bb,tuple[2]),adjustwo_(angle,bb,tuple[3])
    return (p0,p1,p2,p3)

def right_copy(p1,p2,step,angle):
    p1=(p1[0]+step*math.cos(math.radians(angle)),p1[1]+step*math.sin(math.radians(angle)))
    p2=(p2[0]+step*math.cos(math.radians(angle)),p2[1]+step*math.sin(math.radians(angle)))
    #print p1,p2,angle
    return p1,p2

def right1_copy(p1,p2,step,angle):
    p1=(p1[0]+step*math.cos(math.radians(angle+90)),p1[1]+step*math.sin(math.radians(angle+90)))
    p2=(p2[0]+step*math.cos(math.radians(angle+90)),p2[1]+step*math.sin(math.radians(angle+90)))
    #print p1,p2,angle
    return p1,p2
