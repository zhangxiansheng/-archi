#coding=utf-8
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
#其实不是list传入也行，这里主要以前用了这个函数名字，暂时不想改了，等以后一次性改了
def dis_between_two_points(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5


#get triangle area by Heron
def get_triangle_area(p1, p2, p3):
    a, b, c = dis_between_two_points(p1, p2), dis_between_two_points(p2, p3), dis_between_two_points(p1, p3)
    p = (a + b + c) * 0.5
    return (p*(p-a)*(p-b)*(p-c))**0.5


#get raised quad area
def get_quad_area(p1, p2, p3, p4):
    s1 = get_triangle_area( p1, p2, p3 )
    s2 = get_triangle_area( p1, p2, p4 )
    s3 = get_triangle_area( p1, p3, p4 )
    s4 = get_triangle_area( p2, p3, p4 )
    return ( s1 + s2 + s3 +s4 ) * 0.5


#input (p1,p2,p3,p4) and (p1,p2,p3,p4)
#up_left up_right down_right down_left & up right down left
#output (p1,p2,p3,p4)
#and with the order of up_left up_right down_left down right
def get_paper_points(list1,list2):
    
    #判断面积大小
    s1 = get_quad_area(list1[0],list1[1],list1[2],list1[3])
    s2 = get_quad_area(list2[0],list2[1],list2[2],list2[3])
    if s1 > s2*1.1 : return list1
    if s2 > s1*1.1 : return list2
    
    #面积相仿的情况下
    min_dist = int(s1) #99999
    for xi in range(4):
        dist = dis_between_two_points(list2[xi],list1[0])
        if dist < min_dist:
            min_dist, min_xi = dist, xi

    #进行错位取平均
    result_list = [cen(list1[xi], list2[ (xi+min_xi)%4 ]) for xi in range(4)]

    return result_list


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


if __name__ == "__main__":
    print get_quad_area((0,0),(0,1),(1,0),(1,8))
