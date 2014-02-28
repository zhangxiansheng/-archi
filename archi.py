import cv2,cv
import numpy as np
import coconut as co
import math


#open an image as <"numpy.ndarray">
#input address<"string">
#output image<"numpy.ndarray">
#<"numpy.ndarray">.dtype = unit8 (0-255)
#<"numpy.ndarray">.shape = (width, height, <3 is the Count of BGR>)
def open_image(address):
    return cv2.imread(address)


#copy img.shape to create a vain paper
#0 mains Black and 255 mains White
#input1 shape<"tuple"> = <"numpy.ndarray">.shape = (width, height, <3 is the Count of BGR>)
#input2 color<"int"> = 0-255
def create_paper(shape, color=0):
    return np.zeros(shape, np.uint8) + color


#input a colorful image
#input_image.shape = (width, height, <3 is the Count of BGR>)
#output a gray image
#output_image.shape = (width, height)
#input <"numpy.ndarray"> and output <"numpy.ndarray">
def get_gray_image(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#input1 img_gray <"numpy.ndarray"> which shape is just (width, height)
#input2 img_draw is for the contours to be drawt on
#output cornerlists=[cornerlist1,cornerlist2...]
#cornerlist[i]=[(x1,y1), (x2,y2), (x3,y3)...]
def get_contour_cornerlists(img_gray, img_draw=None):
    cornerlists = []
    ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh,2,1)
    for kk in range(len(contours)):
        cnt = contours[kk]
        if len(cnt)>100:
            if hierarchy[0][kk][0] == -1:
                break
            zywcorners = []
            for i in range(len(cnt)-1):
                start = cnt[i][0]
                end =  cnt[i+1][0]
                zywcorners.append((end[0],end[1]))
                if not img_draw == None:
                    cv2.line(img_draw,(start[0],start[1]),(end[0],end[1]),[0,255,0],2)
                    cv2.circle(img_draw,(start[0],start[1]),1,[0,0,255],-1)
            start = cnt[0][0]
            zywcorners.append((start[0],start[1]))
            if not img_draw == None:
                cv2.circle(img_draw,(end[0],end[1]),1,[0,0,255],-1)
                cv2.line(img_draw,(start[0],start[1]),(end[0],end[1]),[0,255,0],2)
            cornerlists.append(zywcorners)
    return cornerlists


#get a uniformal rectangle
#input a contour list [(x1,y1), (x2,y2)...]
#output rectangle<"list"> [center(x,y),size(width,height),angle]
def get_rectangle(contour):
    rect = cv.MinAreaRect2(contour)
    #get the uniform angle
    if rect[2]<-45:
        rect = [rect[0],rect[1],rect[2]+90]
    elif rect[2]>45:
        rect = [rect[0],rect[1],rect[2]-90]
    else:
        rect = [rect[0],rect[1],rect[2]]
    return rect


#input a list of rectangles
#output <"list"> = [ [rect1,rect2...], [rect8, rect9..]..]
#output's every rect is not a list but a tuple
#recti = (center(x,y), size(width,height), angle_adjusted)
def machine_classify(rectangles):
    angle_gap = 12 #
    rects = []
    angles = []
    def dishave_angle(angle_test):
        if len(angles) == 0:
            return None
        for angle_i in range(len(angles)):
            if abs(angles[angle_i]-angle_test) < angle_gap:
                return angle_i
        return None

    for rectangle in rectangles:
        i = dishave_angle( rectangle[2] )
        if i > -1 :
            angles[i] = (angles[i]*len(rects[i])+rectangle[2])/float(len(rects[i])+1)
            rects[i].append((rectangle[0],rectangle[1],angles[i]))
        else:
            angles.append( rectangle[2] )
            rects.append( [(rectangle[0], rectangle[1], rectangle[2])] )

    for i in range(len(rects)):
        for j in range(len(rects[i])):
            rects[i][j] = (rects[i][j][0], rects[i][j][1], angles[i])

    return rects


#input <"list"> = [ [rect1,rect2...], [rect8, rect9..]..]
#input recti = (center(x,y), size(width,height), angle_adjusted)
#output <"list"> = [ [rect1,rect2...], [rect8, rect9..]..]
#output recti = (point1, point2, point3, point4)
def machine_optimize(rectangles):
    #get four points of rectangles
    four_points = []
    for rectangle_list in rectangles:
        four_points.append( [] )
        for rectangle in rectangle_list:
            four_points[-1].append( cv2.cv.BoxPoints(rectangle) )

    #do with every kinds of angle
    four_points_adjusted = []
    for i in range(len(rectangles)):
        #adjust_rect_list( angle,rect_list )
        four_points_adjusted.append( adjust_rect_list(rectangles[i][0][2], four_points[i]) )

    return four_points_adjusted


#input one rectangle list
#input  <"list"> = [rect1,rect2...]
#input recti = (point1, point2, point3, point4)
#output <"list"> = [rect1_adjusted,rect2_adjusted...]
def adjust_rect_list(angle, rectangle_list):
    #input gap_on_y
    #hide_input <"list"> = [ a1, a2 ,a3 ...]
    #output <"list"> = [ <[a1,a2...]>, <[a11, a12..]> ..]
    #output <"list"> = [ a1_, a2_ ..]
    def machine_classify_crossing_y(gap_on_y):
        rails = []
        for y in crossing_y:
            true = 1
            for rail in rails:
                if co.distance_y(angle, y[0], rail[0]) < gap_on_y:
                    rail[0] = ((len(rail)-1)*rail[0]+y[0])/float(len(rail))
                    rail.append(y[1])
                    true = None
            if true:rails.append(y)
        return rails

    #get the crossing point of y-axis
    sum = 0
    crossing_y = []
    for rect in rectangle_list:
        sum = sum+1
        #mean which rect and which side
        crossing_y.append( [co.crossy(angle, rect[0]), sum] ) #up
        crossing_y.append( [co.crossy(angle, rect[1]),-sum] ) #down
    
    #classify the crossing_y########################
    rails_on_y = machine_classify_crossing_y( 3 )
    #adjust the crossing_y
    for rail in rails_on_y:
        if len(rail)>2:
            #print rail#
            bb=rail[0]
            for i in range(len(rail)-1):
                kk=abs(rail[i+1])-1 #zhiqianweil zhengfu guer jia1
                if rail[i+1]>0: #up and down
                    rectangle_list[kk]=co.adjust(angle,bb,rectangle_list[kk],2)#up 0 3
                else:
                    rectangle_list[kk]=co.adjust(angle,bb,rectangle_list[kk],1)#down 1 2

    ###from crossing_y to crossing_x

    #input gap_on_x
    #hide_input <"list"> = [ a1, a2 ,a3 ...]
    #output <"list"> = [ <[a1,a2...]>, <[a11, a12..]> ..]
    #output <"list"> = [ a1_, a2_ ..]
    def machine_classify_crossing_x(gap_on_x):
        rails = []
        for x in crossing_x:
            true = 1
            for rail in rails:
                if co.distance_x(angle+90, x[0], rail[0]) < gap_on_x:
                    rail[0] = ((len(rail)-1)*rail[0]+x[0])/float(len(rail))
                    rail.append(x[1])
                    true = None
            if true:rails.append(x)
        return rails

    #get the crossing point of y-axis
    sum = 0
    crossing_x = []
    for rect in rectangle_list:
        sum = sum+1
        #mean which rect and which side
        crossing_x.append( [co.crossx(angle+90, rect[1]), sum] ) #left
        crossing_x.append( [co.crossx(angle+90, rect[2]),-sum] ) #right

    #classify the crossing_x########################
    rails_on_x = machine_classify_crossing_x( 3 )
    #adjust the crossing_x
    for rail in rails_on_x:
        if len(rail)>2:
            #print rail#
            bb=rail[0]
            for i in range(len(rail)-1):
                kk=abs(rail[i+1])-1 #zhiqianweil zhengfu guer jia1
                if rail[i+1]>0: #up and down
                    rectangle_list[kk]=co.adjust(angle+90,bb,rectangle_list[kk],3)#left 0 1
                else:
                    rectangle_list[kk]=co.adjust(angle+90,bb,rectangle_list[kk],4)#right 2 3

    return rectangle_list


#black and white
def black_and_white(img, step=200):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j]<step:
                img[i][j] = 0
            else:
                img[i][j] = 255
    return img

#expand
def expand(img, color, step=3):
    if color == "black":c1,c2 = 255, 0
    else:c1,c2 =0, 255
    img_paper = create_paper(img.shape, c1)
    for i in range(len(img))[step:-step]:
        for j in range(len(img[i]))[step:-step]:
            if img[i][j] == c2:
                for ii in range(i+1+step)[i-step:]:
                    for jj in range(j+1+step)[j-step:]:
                        img_paper[ii][jj] = c2
    return img_paper




def draw_test(angle, rectangle_list, img1):
    def tutu(p):
        return (p[0],p[1])

    def intu(p):
        return((int(round(p[0])),int(round(p[1]))))

    stepW=10 #xianju chuizhipingyi
    #fourth time round all the rects to draw
    
    for kk in range(len(rectangle_list)):
        points = np.int0(np.around(rectangle_list[kk])) #int(four points of rect)
        cv2.polylines(img1,[points],True,(255,255,255),2) #draw rects
        if co.dis_lianbiao(points[0],points[1])<co.dis_lianbiao(points[2],points[1]):
            #heng
            cv2.line(img1,co.cenint(points[0],points[1]),co.cenint(points[2],points[3]),(255,255,255),1)
            pp1=co.cen(points[0],points[1])
            pp2=tutu(points[1])
            while pp2[0]+stepW*math.cos(math.radians(angle))<points[2][0]:
                pp1,pp2=co.right_copy(pp1,pp2,stepW,angle)
                cv2.line(img1,intu(pp1),intu(pp2),(255,255,255),1)
        else:
            #zong
            cv2.line(img1,co.cenint(points[2],points[1]),co.cenint(points[0],points[3]),(255,255,255),1)
            pp1=co.cen(points[2],points[1])
            pp2=tutu(points[1])
            while pp2[1]+stepW*math.sin(math.radians(angle)+90)<points[0][1]:
                pp1,pp2=co.right1_copy(pp1,pp2,stepW,angle)
                cv2.line(img1,intu(pp1),intu(pp2),(255,255,255),1)


###Begin the main project###

img = open_image('/Users/zyw/t2.png')
img_black_paper = create_paper(img.shape)
img_gray = get_gray_image(img)

img_gray = expand(expand(black_and_white( img_gray ), "black" ), "white")

contours = get_contour_cornerlists(img_gray,img)

rectangles = []
for contour in contours:
    rectangles.append( get_rectangle(contour) )

#angle adjust
rectangles = machine_classify( rectangles )

#get the side_point_adjusted four_point_rect
rectangles_four_points = machine_optimize( rectangles )


draw_test(rectangles[0][0][2], rectangles_four_points[0], img_black_paper)#






cv2.namedWindow('img')
cv2.imshow('img',img_gray)
cv2.namedWindow('img2')
cv2.imshow('img2',img)
cv2.namedWindow('img1')
cv2.imshow('img1',img_black_paper)
cv2.waitKey(0)
cv2.destroyAllWindows()