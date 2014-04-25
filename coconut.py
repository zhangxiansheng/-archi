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
def get_quad_area(p1, p2=None, p3=None, p4=None):
    #if input a tuple or list
    if isinstance(p1, (list, tuple)):
        p2, p3, p4 = p1[1], p1[2], p1[3]
        p1 = p1[0]
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


#quadratic
def quadratic( a, b, c ):
    '''判断方程的根；若方程有根，则将其解出来'''
    delta=b**2-4*a*c #根的判别式
    print a,b,c,delta
    if delta<0:
        return None
    elif delta==0:
        return -b/(2*a)
    else:
        x1=(-b+math.sqrt(delta))/(2*a) #第一个根  
        x2=(-b-math.sqrt(delta))/(2*a) #第二个根  
        return (x1, x2)


#offset to get two points
#near is first
#!!!!!
def offset( p0, p1, R, center=(0,0) ):
    K, B = p1[0]-p0[0], p1[1]-p0[1]
    x1 = (B*B*R*R/(B*B+K*K))**0.5
    x2 = -x1
    y1 = (R*R-x1*x1)**0.5
    y2 = -y1
    if abs(K*x1+B*y1)>abs(K*x2+B*y1):
        x1, x2 = x2, x1
    result_p1, result_p2 = (p0[0]+x1, p0[1]+y1), (p0[0]+x2, p0[1]+y2)
    if dis_between_two_points(center,result_p1) > dis_between_two_points(center,result_p2):
        result_p1, result_p2 = result_p2, result_p1
    return result_p1, result_p2


#one line to transform to get a rect
def line_to_rect( c0, c1, r, off=0, center=(0,0) ):
    if off > 0 :
        x0, x1 = offset( c0, c1, off, center )
        x2, x3 = offset( c1, c0, off, center )
        c0, c1 = x1, x3
    p1, p2 = offset( c0, c1, r)
    p4, p3 = offset( c1, c0, r)
    return p1,p2,p3,p4


#scale a rect
def rect_scale( p0, p1, p2, p3, width, height ):
    p1_ = get_rect_point( p0, p1, p2, p3, width, 0 )
    p2_ = get_rect_point( p0, p1, p2, p3, width, height)
    p3_ = get_rect_point( p0, p1, p2, p3, 0, height)
    return p0, p1_, p2_, p3_


#不完全地3个顶点求取第四个顶点
def rect_progress( p0, p1, p3 ):
    p2 = ( p3[0]-p0[0]+p1[0], p3[1]-p0[1]+p1[1] )
    return p0, p1, p2, p3


#传入一个距离，和两个端点，求离第一个端点l距离的分点
def get_l_point( p0, p1, l ):
    d = dis_between_two_points(p0, p1)
    return ( p0[0]+(p1[0]-p0[0])*l/d, p0[1]+(p1[1]-p0[1])*l/d )


#传入一个顶点，一个width顶点，一个height顶点
#传入width_, height_
def get_rect_point( p0, p1, p2, p3, width_, height_):
    w1 = get_l_point( p0, p1, width_)
    w2 = get_l_point( p3, p2, width_)
    return get_l_point( w1, w2, height_)



if __name__ == "__main__":
    print get_quad_area((0,0),(0,1),(1,0),(1,8))
