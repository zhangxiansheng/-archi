#coding=utf-8

import cv2,cv
import numpy as np
import coconut as co
import math
import draw.sdxf as sdxf
import json


DEVIATION_BETWEEN_X = 3
DEVIATION_BETWEEN_Y = 3
ANGLE_GAP = 12
PAPER_MODE_DIC = {'A4-h':(1684,1191), 'A4-v':(1191,1684), \
                  'A3-h':(2382,1684), 'A3-v':(1684,2382), \
                  'A2-h':(3368,2382), 'A2-v':(2382,3368), \
                  'A1-h':(4764,3368), 'A1-v':(3368,4764) }


#input <"float"> or <"int">
def set_deviation_x(new_deviation_x):
    '''重新指定识别横线与横线之间的误差距离'''
    global DEVIATION_BETWEEN_X
    DEVIATION_BETWEEN_X = new_deviation_x


#input <"float"> or <"int">
def set_deviation_y(new_deviation_y):
    '''重新指定识别纵线与纵线之间的误差距离'''
    global DEVIATION_BETWEEN_Y
    DEVIATION_BETWEEN_Y = new_deviation_y


#input <"float"> or <"int">
def set_deviation(new_deviation_x, new_deviation_y):
    '''一次性重新指定识别横纵误差距离'''
    global DEVIATION_BETWEEN_X, DEVIATION_BETWEEN_Y
    DEVIATION_BETWEEN_X = new_deviation_x
    DEVIATION_BETWEEN_Y = new_deviation_y


#input <"float"> or <"int">
#best between 0-20 degree
def set_angle_gap(new_angle_gap):
    '''重新指定角度分类的角度度数误差值'''
    global ANGLE_GAP
    ANGLE_GAP = new_angle_gap


#open an image as <"numpy.ndarray">
#input address<"string">
#output image<"numpy.ndarray">
#<"numpy.ndarray">.dtype = unit8 (0-255)
#<"numpy.ndarray">.shape = (width, height, <3 is the Count of BGR>)
def open_image(address):
    '''打开图像为numpy.ndarray类型矩阵'''
    return cv2.imread(address)


#save <"numpy.ndarray"> as an image
#input output_address<"string">
#input image<"numpy.ndarray">
def save_image(address,img):
    '''将numpy.ndarray类型的图像保存成硬图像文件'''
    cv2.imwrite(address,img)


#copy img.shape to create a vain paper
#0 mains Black and 255 mains White
#input1 shape<"tuple"> = <"numpy.ndarray">.shape = (width, height, <3 is the Count of BGR>)
#input2 color<"int"> = 0-255 or <"tuple"> = (255, 0, 255)
def create_paper(shape, color=0):
    '''根据长宽与颜色来预设生成一张画布'''
    return np.zeros(shape, np.uint8) + color


#input image <"numpy.ndarray">
#image.shape = (width, height) or (width, height, 3)
#input threshold_value <"int"> 0-255 or <"unit8">
#output black_and_white_image <"numpy.ndarray">
#black_and_white_image.shape = (width, height, 3) (RGB)
def get_black_and_white_image(image, threshold_value):
    '''根据阈值将图像二值化处理，即将输入图像处理成黑白图像'''
    ret,thresh = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return thresh


#input a colorful image
#input_image.shape = (width, height, <3 is the Count of BGR>)
#output a gray image
#output_image.shape = (width, height)
#input <"numpy.ndarray"> and output <"numpy.ndarray">
def get_gray_image(image):
    '''将RGB格式图像转换成灰度图像'''
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#input image <"numpy.ndarray">
#output image <"numpy.ndarray">
def get_thick(img, a):
    '''腐蚀图像 = 加粗图像线条'''
    #OpenCV定义的结构元素
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (a, a))
    #腐蚀图像=加粗
    eroded = cv2.erode(img, kernel)
    return eroded


#input image <"numpy.ndarray">
#output image <"numpy.ndarray">
def get_thin(img, a):
    '''膨胀图像 = 变细图像线条'''
    #OpenCV定义的结构元素
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (a, a))
    #膨胀图像 = 变细
    dilated = cv2.dilate(img, kernel)
    return dilated


#input image <"numpy.ndarray">
#output image <"numpy.ndarray">
def close_gap(img, a):
    '''缝合缺口 = 先加粗a个单位，再变细a个单位'''
    img_thick = get_thick(img, a)
    img_thin = get_thin(img_thick, a)
    return img_thin


#input a multiple-color image <"numpy.ndarray">
#input N = K - 1 (K is K-means machine learning)
#input N means how many meaningful colors except white
#output a List of image <"numpy.ndarray">
def separate_color( img, n ):
    '''K-means方法进行色彩分离'''
    k = n + 1
    Z = img.reshape( (-1, 3) )
    Z = np.float32( Z )
    criteria = ( cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0 )
    ret,label,center=cv2.kmeans( Z, k, criteria, 10, cv2.KMEANS_RANDOM_CENTERS )
    
    #find which is white
    near_white = 500
    near_self = 120
    near_i = None
    
    def volatility(c):
        return abs(c[0]-c[1]) + abs(c[1]-c[2]) + abs(c[0]-c[2])
    
    for i in xrange(k):
        if 255*3 - sum(center[i]) < near_white and volatility(center[i]) < near_self:
            near_white = 255*3 - sum(center[i])
            near_i = i
    result_images_list = []
    label_flatten = label.flatten()

    #i means which color will be show
    #j means which color is i
    for i in xrange(k):
        if i != near_i:
            center_copy = center
            for j in xrange(k):
                if j == i: center_copy[j] = [0, 0, 0]
                else: center_copy[j] = [255, 255, 255]
            res = center_copy[ label_flatten ]
            result_images_list.append( np.uint8(res.reshape(img.shape)) )

    return result_images_list



#input1 img_gray <"numpy.ndarray"> which shape is just (width, height)
#input2 img_draw is for the contours to be drawt on
#output cornerlists=[cornerlist1,cornerlist2...]
#cornerlist[i]=[(x1,y1), (x2,y2), (x3,y3)...]
def get_contour_cornerlists(img_gray, img_draw=None, thresh_mode=cv2.THRESH_BINARY, limit_caught=70 ):
    '''根据灰度图片识别出所有的内轮廓的点集'''
    cornerlists = []
    ret, thresh = cv2.threshold(img_gray, 127, 255, thresh_mode)
    contours, hierarchy = cv2.findContours(thresh,2,1)
    for kk in range(len(contours)):
        cnt = contours[kk]
        #set_limit_caught() can change the value of limit_caught
        if len(cnt) > limit_caught:
            #-1是为了排除外轮廓，8或者写成不等于-1是为了排除内岛
            if hierarchy[0][kk][0] == -1 or hierarchy[0][kk][3] != -1:
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
    '''根据一个矩形内轮廓角点集识别出此矩形'''
    rect = cv.MinAreaRect2(contour)
    #get the uniform angle
    if rect[2]<-45:
        rect = [rect[0],(rect[1][1],rect[1][0]),rect[2]+90]
    elif rect[2]>45:
        rect = [rect[0],(rect[1][1],rect[1][0]),rect[2]-90]
    else:
        rect = [rect[0],rect[1],rect[2]]
    return rect


#input a list of rectangles
#output <"list"> = [ [rect1,rect2...], [rect8, rect9..]..]
#output's every rect is not a list but a tuple
#recti = (center(x,y), size(width,height), angle_adjusted)
def machine_classify(rectangles):
    '''根据矩形的角度对矩形进行角度优化与分类'''
    #set_angle_gap() can change the value of ANGLE_GAP
    global ANGLE_GAP
    angle_gap = ANGLE_GAP #
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
    '''对列表中的矩形进行边角重合并线优化'''
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
    '''边角重合并线优化的核心处理函数（重要）'''
    
    global DEVIATION_BETWEEN_X, DEVIATION_BETWEEN_Y
    
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
    
    #classify the crossing_y 横线与横线间的误差
    #set_deviation_x() can change the value of DEVIATION_BETWEEN_X
    rails_on_y = machine_classify_crossing_y( DEVIATION_BETWEEN_X )
    #adjust the crossing_y
    for rail in rails_on_y:
        if len(rail)>2:
            bb=rail[0]
            for i in range(len(rail)-1):
                kk=abs(rail[i+1])-1 #give back for before
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

    #classify the crossing_x 竖线与竖线间的误差
    #set_deviation_y() can change the value of DEVIATION_BETWEEN_Y
    rails_on_x = machine_classify_crossing_x( DEVIATION_BETWEEN_Y )
    #adjust the crossing_x
    for rail in rails_on_x:
        if len(rail)>2:
            bb=rail[0]
            for i in range(len(rail)-1):
                kk=abs(rail[i+1])-1 #give back for before
                if rail[i+1]>0: #up and down
                    rectangle_list[kk]=co.adjust(angle+90,bb,rectangle_list[kk],3)#left 0 1
                else:
                    rectangle_list[kk]=co.adjust(angle+90,bb,rectangle_list[kk],4)#right 2 3

    return rectangle_list



########## archi-ex ############################
'''自定义模块'''
########## archi-ex ############################



#input a gray img <"numpy.ndarray">
#input close_value is used to forbid some small crossing
#recommended close_value = 20
#if close_gap the img out of this def then set close_value 0
#output a set of tuples like ( center, radius )
def get_circle_tree( img, close_value = 20, img_show = None, limit_caught=70 ):
    '''识别点状树木图标'''
    
    #当直接没传入close_value而传入img_show的情况下
    if isinstance(close_value, np.ndarray):
        img_show = close_value
        close_value = 20
    
    #当在函数外已经进行缺口闭合处理的情况下close_value为0
    if close_value > 0:
        img = close_gap( img, close_value )
    
    #如果传入了img_show则需要表现识别的过程线条到img_show上
    if img_show:
        contours = get_contour_cornerlists( img, limit_caught=limit_caught )
    else:
        contours = get_contour_cornerlists( img, img_draw=img_show, limit_caught=limit_caught )

    rectangles = [ get_rectangle(contour) for contour in contours ]
    circles = set( [ ( rect[0], max(rect[1])/2.0 ) for rect in rectangles ] )
    return circles


#input a gray img <"numpy.ndarray">
#input close_value is used to forbid some small crossing
#recommended close_value = 4
#if close_gap the img out of this def then set close_value 0
#output a list of contour points
def get_lake_strandline( img, close_value = 4, img_show = None ):
    '''识别湖岸线'''
    
    #当直接没传入close_value而传入img_show的情况下
    if isinstance(close_value, np.ndarray):
        img_show = close_value
        close_value = 4
    
    #当在函数外已经进行缺口闭合处理的情况下close_value为0
    if close_value > 0:
        img = close_gap( img, close_value )
    
    #如果传入了img_show则需要表现识别的过程线条到img_show上
    if img_show == None:
        contours = get_contour_cornerlists( img )
    else:
        contours = get_contour_cornerlists( img, img_show )

    #内岛的外轮廓已经被用
    #hierarchy元素的第四个数字的值不等于-1或者等于8这个条件进行否定了
    #目前返回的contours中并未标出是湖岸线还是内岛的岸线
    return contours


#input a gray img <"numpy.ndarray">
#input close_value is used to forbid some small crossing
#recommended close_value = 10
#if close_gap the img out of this def then set close_value 0
#output a list of contour points
def get_tree_revclound( img, close_value = 10, img_show = None ):
    '''识别树丛云线'''
    
    #当直接没传入close_value而传入img_show的情况下
    if isinstance(close_value, np.ndarray):
        img_show = close_value
        close_value = 10
    
    #当在函数外已经进行缺口闭合处理的情况下close_value为0
    if close_value > 0:
        img = close_gap( img, close_value )
    
    #如果传入了img_show则需要表现识别的过程线条到img_show上
    if img_show == None:
        contours = get_contour_cornerlists( img )
    else:
        contours = get_contour_cornerlists( img, img_show )
    
    #目前返回的云线是最原始的识别数据，尚未进行云线优化
    #将来可以进行的优化有：最近点的距离、云线数据格式等
    return contours



########## archi-draw ##########################
'''绘图模块'''
'''绘图模块分三个绘图平台：
    dxf格式绘图-->cad平台
    用openCV绘图而保存成jpg或png等格式的位图
    使用json进行数据传递然后由客户端利用canvas进行绘图'''
'''bug:need mirror'''
########## archi-draw ##########################



#archi-draw with SDXF
''' 绘制dxf格式的矢量图 '''
#archi-draw with SDXF


#output a dxf_drawing <type 'instance'>
def open_dxf():
    '''生成dxf绘图域,并对图层进行初始化'''
    drawing = sdxf.Drawing()
    drawing.layers.append( sdxf.Layer(name='lake' , color=140) )
    drawing.layers.append( sdxf.Layer(name='tree' , color=4) )
    drawing.layers.append( sdxf.Layer(name='revclound' , color=3) )
    drawing.layers.append( sdxf.Layer(name='roof_deck' , color=7) )
    drawing.layers.append( sdxf.Layer(name='roof_tile' , color=254) )
    drawing.layers.append( sdxf.Layer(name='roof_outline' , color=6) )
    return drawing


#input a dxf_drawing <type 'instance'>
#input save_address_name <'string'>
def save_dxf( drawing, save_address_name ):
    '''将指定的drawing域保存成dxf格式文件'''
    drawing.saveas( save_address_name )


#input a dxf_drawing <type 'instance'>
#input list_of_roof <'set'> or <'list'>
def dxf_draw_roof( drawing, list_of_roof ):
    '''在指定drawing域中绘制屋顶'''
    
    #画屋顶檩条的闭包
    def draw_roof_tile(p0, p1, p2, p3, min_dist = 6, opp=1):
        
        if opp == 1:
            draw_roof_tile(p0, p1, p2, p3, 3*min_dist, opp=-1)
        #initialization
        if p0[1]*opp < p1[1]*opp:
            p1, p2 = co.cen( p0, p1 ), co.cen( p2, p3 )
        else:
            p0, p3 = co.cen( p0, p1 ), co.cen( p2, p3 )

        tile_dist = min_dist
        tile_dist_max = co.dis_between_two_points( p0, p3 )
        while 1:
            if tile_dist >= tile_dist_max: break
            point1 = ( tile_dist*(p3[0]-p0[0])/tile_dist_max+p0[0], tile_dist*(p3[1]-p0[1])/tile_dist_max+p0[1] )
            point2 = ( tile_dist*(p2[0]-p1[0])/tile_dist_max+p1[0], tile_dist*(p2[1]-p1[1])/tile_dist_max+p1[1] )
            drawing.append( sdxf.Line(points=[point1, point2], layer='roof_tile') )
            tile_dist = tile_dist + min_dist
    
    #画屋顶主楞骨的闭包
    def draw_roof_deck():
        #比较长短
        if co.dis_between_two_points(roof[1],roof[2]) > co.dis_between_two_points(roof[2],roof[3]):
            drawing.append( sdxf.Line(points=[co.cen(roof[2],roof[3]),co.cen(roof[1],roof[0])], layer='roof_deck') )
            draw_roof_tile( roof[2], roof[3], roof[0], roof[1] )
        else:
            drawing.append( sdxf.Line(points=[co.cen(roof[1],roof[2]),co.cen(roof[3],roof[0])], layer='roof_deck') )
            draw_roof_tile( roof[3], roof[0], roof[1], roof[2] )

    for roof in list_of_roof:
        drawing.append( sdxf.PolyLine(points=roof, flag=1, layer='roof_outline') )
        draw_roof_deck()


#input a dxf_drawing <type 'instance'>
#input list_of_tree means circles <'list'> or <'set'>
def dxf_draw_tree( drawing, list_of_tree ):
    '''在指定drawing域中绘制点树'''
    for circle in list_of_tree:
        drawing.append( sdxf.Circle(circle[0], circle[1], layer='tree') )


#input a dxf_drawing <type 'instance'>
#input list_of_lake mean lake_strandlines <'list'> or <'set'>
def dxf_draw_lake( drawing, list_of_lake):
    '''在指定drawing域中绘制湖岸线'''
    for contour in list_of_lake:
        drawing.append( sdxf.PolyLine(points=contour, flag=1, layer='lake') )


#input a dxf_drawing <type 'instance'>
#input list_of_revclound <'list'> or <'set'>
def dxf_draw_revclound( drawing, list_of_revcloud ):
    '''在指定drawing域中绘制修行云线'''
    for contour in list_of_revcloud:
        drawing.append( sdxf.PolyLine(points=contour, flag=1, layer='revclound') )



#archi-draw with Canvas
''' 使用Canvas进行绘图 '''
#使用Js调用H5的canvas元素进行绘图
#所以一般情况是服务器识别数据然后客户端绘图
#有两种方法：
#①是服务器解析好识别的数据，
#直接传递简单的绘图命令给客户端；
#②服务器直接传递未深入解析的识别数据，
#由客户端通过js脚本来完成如何绘图的解析工作。
#为了减轻服务器的负担与减少传递信息的量，
#上述②方法更优。
#信息传递的方式：Json格式的数据传递
#在archi.py中的canvas绘图功能中，
#archi.py提供函数-->generate JSON
#用来产生标准绘图格式的json数据的函数
#为了更容易地调用canvas绘图
#笔者在processing和processingJS的基础上
#开发的prcessingX.js是直接利用js调用canvas元素
#语法上与processing一致，局部进行了改进
#processingX.js的绘图函数部分已经基本完善
#processingX的项目托管在github的仓库地址是：
#https://github.com/zhangxiansheng/processingjs
#引用processingX.js可直接在html文件中外链js脚本如下：
#<script src="http://zhangxiansheng.github.io/processingX.js"></script>
#archi-draw with Canvas


#input list_of_roof
#output a json string
#{ "kind" : "roof",
#  "four_points": [
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4] ],
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4] ],
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4] ],
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4] ],
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4] ],
#                    ...
#                 ]
def get_roof_json(list_of_roof, need_dic=None ):
    '''返回roof类型的JSON数据'''
    
    #initialize "kind"
    dic_result = { 'kind' : 'roof', 'four_points' : [] }
    
    #make points all be list not tuple
    #need int not float
    for roof in list_of_roof:
        tmp = [ [int(round(point[0])), int(round(point[1])) ] for point in roof ]
        dic_result['four_points'].append(tmp)
    
    #if user need a dic not a json
    if need_dic == 'dic':return dic_result

    return json.dumps(dic_result)


#input list_of_tree
#output a json string
#{ "kind" : "tree",
#  "circle": [
#                [ x1, y1, r1 ],
#                [ x2, y2, r2 ],
#                [ x3, y3, r3 ],
#                [ x4, y4, r4 ],
#                [ x5, y5, r5 ],
#                ...
#            ]
def get_tree_json(list_of_tree, need_dic=None ):
    '''返回tree类型的JSON数据'''
    
    #initialize "kind"
    dic_result = { 'kind' : 'tree' }
    
    #make points all be list not tuple
    #need int not float
    dic_result['circle'] = [ [int(round(circle[0][0])), int(round(circle[0][1])), int(round(circle[1]))]  for circle in list_of_tree ]
    
    #if user need a dic not a json
    if need_dic == 'dic':return dic_result
    
    return json.dumps(dic_result)


#input list_of_lake
#output a json string
#{ "kind" : "lake",
#  "lake_points": [
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4]... ],
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4]... ],
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4]... ],
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4]... ],
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4]... ],
#                    ...
#                 ]
def get_lake_json(list_of_lake, need_dic=None ):
    '''返回lake类型的JSON数据'''
    
    #initialize "kind"
    dic_result = { 'kind' : 'lake', 'lake_points' : [] }
    
    #make points all be list not tuple
    #need int not float
    for lake in list_of_lake:
        tmp = [ [int(round(point[0])), int(round(point[1])) ] for point in lake ]
        dic_result['lake_points'].append(tmp)
    
    #if user need a dic not a json
    if need_dic == 'dic':return dic_result
    
    return json.dumps(dic_result)


#input list_of_revclound
#output a json string
#{ "kind" : "revclound",
#  "revclound_points": [
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4]... ],
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4]... ],
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4]... ],
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4]... ],
#                    [ [x1,y1], [x2,y2], [x3,y3], [x4,y4]... ],
#                    ...
#                 ]
def get_revclound_json(list_of_revclound, need_dic=None ):
    '''返回lake类型的JSON数据'''
    
    #initialize "kind"
    dic_result = { 'kind' : 'revclound', 'revclound_points' : [] }
    
    #make points all be list not tuple
    #need int not float
    for revclound in list_of_revclound:
        tmp = [ [int(round(point[0])), int(round(point[1])) ] for point in revclound ]
        dic_result['revclound_points'].append(tmp)
    
    #if user need a dic not a json
    if need_dic == 'dic':return dic_result
    
    return json.dumps(dic_result)



#archi-draw with OpenCV
''' 使用OpenCV进行绘图 '''
#archi-draw with OpenCV



#input img <'numpy.ndarray'>
#input list_of_roof <'set'> or <'list'>
def cv_draw_roof( img, list_of_roof ):
    '''通过OpenCV在指定img中绘制屋顶'''
    
    #画屋顶檩条的闭包
    def draw_roof_tile(p0, p1, p2, p3, min_dist = 6, opp=1):
        
        if opp == 1:
            draw_roof_tile(p0, p1, p2, p3, 3*min_dist, opp=-1)
        #initialization
        if p0[1]*opp < p1[1]*opp:
            p1, p2 = co.cen( p0, p1 ), co.cen( p2, p3 )
        else:
            p0, p3 = co.cen( p0, p1 ), co.cen( p2, p3 )
        
        tile_dist = min_dist
        tile_dist_max = co.dis_between_two_points( p0, p3 )
        while 1:
            if tile_dist >= tile_dist_max: break
            point1 = ( tile_dist*(p3[0]-p0[0])/tile_dist_max+p0[0], tile_dist*(p3[1]-p0[1])/tile_dist_max+p0[1] )
            point2 = ( tile_dist*(p2[0]-p1[0])/tile_dist_max+p1[0], tile_dist*(p2[1]-p1[1])/tile_dist_max+p1[1] )
            cv2.polylines(img,[np.int32(np.around([point1, point2]))],True,(255,255,255),1)
            tile_dist = tile_dist + min_dist
    
    #画屋顶主楞骨的闭包
    def draw_roof_deck():
        #比较长短
        if co.dis_between_two_points(roof[1],roof[2]) > co.dis_between_two_points(roof[2],roof[3]):
            cv2.polylines(img,[np.int32(np.around([co.cen(roof[2],roof[3]),co.cen(roof[1],roof[0])]))],True,(255,255,255),1)
            draw_roof_tile( roof[2], roof[3], roof[0], roof[1] )
        else:
            cv2.polylines(img,[np.int32(np.around([co.cen(roof[1],roof[2]),co.cen(roof[3],roof[0])]))],True,(255,255,255),1)
            draw_roof_tile( roof[3], roof[0], roof[1], roof[2] )
    
    for roof in list_of_roof:
        cv2.polylines(img,[np.int32(np.around(roof))],True,(255,255,255),2)
        draw_roof_deck()


#input img <'numpy.ndarray'>
#input list_of_tree means circles <'list'> or <'set'>
def cv_draw_tree( img, list_of_tree ):
    '''通过OpenCV在指定img中绘制点树'''
    for circle in list_of_tree:
        cv2.circle( img, ( int(round(circle[0][0])), int(round(circle[0][1])) ), int(round(circle[1])), (255,255,255), 1 )


#input img <'numpy.ndarray'>
#input list_of_lake mean lake_strandlines <'list'> or <'set'>
def cv_draw_lake( img, list_of_lake ):
    '''通过OpenCV在指定img中绘制湖岸线'''
    for contour in list_of_lake:
        cv2.polylines(img,[np.int32(np.around(contour))],True,(255,255,255),2)


#input img <'numpy.ndarray'>
#input list_of_revcloud <'list'> or <'set'>
def cv_draw_revclound( img, list_of_revcloud ):
    '''通过OpenCV在指定img中绘制修行云线'''
    for contour in list_of_revcloud:
        cv2.polylines(img,[np.int32(np.around(contour))],True,(255,255,255),2)



#archi-camera Mend Perspective
'''识别、裁剪、拉伸还原具有透视效果的纸张'''
#archi-camera Mend Perspective


#input a img
#output a gray img
def detect_white_paper( img, value=127 ):
    '''用颜色来感应出白纸'''
    img = np.int32(img)
    b, g, r = cv2.split(img)
    return np.where( (b>value) & (g>value) & (r>value) & (abs(b-g)+abs(b-r)+abs(g-r)<110), np.uint8(0), np.uint8(255))


#input a gray img
#output a gray img
def zyw_denoising( img, fade_value=13, rise_value=66 ):
    '''苇式去噪法'''
    img = get_thin(img, fade_value )
    img = get_thick(img, fade_value + rise_value )
    img = get_thin(img, rise_value )
    return img


#input a gray img
#output the longest one of contours
#the longest one means paper
def find_paper_contour( img, thresh_mode=1 ):
    '''识别纸张的轮廓线'''
    ret, thresh = cv2.threshold(img, 127, 255, thresh_mode) #二值化处理
    contours, hierarchy = cv2.findContours(thresh,2,1) #轮廓线识别
    
    #get the longest contour and reshape it
    longest = 0

    for i in xrange(len(contours)):
        if len(contours[i]) > longest:
            longest, which = len(contours[i]), i

    return contours[which].reshape((longest,2))


#input a contour
#output four points
#[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
#x,y numpy.float64
def find_contour_points( contour ):
    '''识别轮廓线4个角点'''
    most_up, most_left = 999999, 999999
    most_down, most_right = 0, 0
    
    most_left_up, most_right_up = 999999, 999999
    most_left_down, most_right_down = 0, 0
    
    for p in contour:
        #kind2
        if sum(p) > most_right_down: most_right_down, right_down = sum(p), p
        if sum(p) < most_left_up: most_left_up, left_up = sum(p), p
        if p[1]+10000-p[0] < most_right_up: most_right_up, right_up = p[1]+10000-p[0], p
        if p[1]+10000-p[0] > most_left_down: most_left_down, left_down = p[1]+10000-p[0], p
        
        #kind1
        if p[0] < most_left: most_left, left_point = p[0], p
        if p[0] > most_right: most_right, right_point = p[0], p
        if p[1] < most_up: most_up, up_point = p[1], p
        if p[1] > most_down: most_down, down_point = p[1], p
    
    #up_left up_right down_right down_left & up right down left
    list1 = [ left_up, right_up, right_down, left_down ]
    list2 = [ up_point, right_point, down_point, left_point ]
    
    return co.get_paper_points(list1, list2)


#input points [ up_left_point, up_right_point, down_right_point, down_left_point ]
#output image
def perspective_transform( img, points, paper_width=1684, paper_height=1191, paper_mode='A4-h'):
    '''透视转换成正视'''
    global PAPER_MODE_DIC
    
    if paper_mode != 'A4-h':
        paper_width, paper_height = PAPER_MODE_DIC[ paper_mode ]

    points[2], points[3] = points[3], points[2]
    if (float(paper_width)/paper_height - 1 )*(co.dis_between_two_points(points[0],points[1])/co.dis_between_two_points(points[0],points[2]) -1 ) < 0 :
        points[0], points[1], points[2], points[3] = points[2], points[0], points[3], points[1]

    pts1 = np.float32( points )
    pts2 = np.float32( [[0,0],[paper_width,0],[0,paper_height],[paper_width,paper_height]] )
    M = cv2.getPerspectiveTransform( pts1, pts2 )
    dst = cv2.warpPerspective( img, M, (1684,1191) )
    return dst


#archi-pro
'''建筑布局的深入|迭代递归|测试版|此api不纳入正统'''
#archi-pro

import random

#input four points = (point1, point2, point3, point4)
#output a set of tuple = {(p1,p2,p3,p4)...}
#So sorry for it is complex
def roof_cut( four_points, bound_A=100, bound_B=230, gap=25, corner=38 ):
    '''智能分割布局'''
    global img_black_paper
    
    rect_width = co.dis_between_two_points( four_points[0], four_points[1] ) #width
    rect_height = co.dis_between_two_points( four_points[1], four_points[2] ) #height
    rect_max_side = max( rect_width, rect_height )

    # Kind1:One building
    if rect_max_side < bound_A:
        if min( rect_width, rect_height ) <10: return set()
        return set([four_points])
    
    result_set = set()
    
    # Kind2:One side to be a yard or block
    # Kind3:A yard or a street block
    if rect_max_side < bound_B:
        if rect_width < bound_A:
            # Kind2
            c_right, c_left, c_up, c_down = co.sidecenter( four_points )
            center_rect = co.cen(c_up,c_down)
            tmp_point = co.cen( co.cen(c_down, center_rect), c_up )
            result_set = result_set.union( roof_cut( co.line_to_rect(c_up, tmp_point, rect_width*0.5*0.8, 0.2*0.5*rect_width ) ) )
            result_set = result_set.union( roof_cut( co.line_to_rect(tmp_point, c_down, rect_width*0.5 ) ) )
            return result_set
            
        elif rect_height < bound_A:
            # Kind2
            c_right, c_left, c_up, c_down = co.sidecenter( four_points )
            center_rect = co.cen(c_up,c_down)
            tmp_point = co.cen( co.cen(c_right, center_rect), c_left )
            result_set = result_set.union( roof_cut( co.line_to_rect(c_left, tmp_point, rect_height*0.5*0.8, 0.2*0.5*rect_height ) ) )
            result_set = result_set.union( roof_cut( co.line_to_rect(tmp_point, c_right, rect_height*0.5 ) ) )
            return result_set
            
        else:
            # Kind3
            if rect_width>2*bound_A or rect_height>2*bound_A:
                width_cut, height_cut = int(rect_width / bound_A), int(rect_height / bound_A)
                if width_cut == 0: width_cut = 1
                if height_cut == 0: height_cut = 1
                width_side, height_side = rect_width / width_cut, rect_height / height_cut
                print width_side, height_side,width_cut,height_cut, '&&&&'
                for i in xrange(width_cut):
                    for j in xrange(height_cut):
                        #wrong
                        p0 = co.get_rect_point( four_points[0], four_points[1], four_points[2], four_points[3], \
                                   i*width_side, j*height_side )
                                   
                        p1 = co.get_rect_point( four_points[0], four_points[1], four_points[2], four_points[3], \
                                               (i+1)*width_side, j*height_side )
                                               
                        p2 = co.get_rect_point( four_points[0], four_points[1], four_points[2], four_points[3], \
                                               (i+1)*width_side, (j+1)*height_side )
                        
                        p3 = co.get_rect_point( four_points[0], four_points[1], four_points[2], four_points[3], \
                                               i*width_side, (j+1)*height_side )
                        
                        result_set = result_set.union( roof_cut( (p0,p1,p2,p3) ) )
            
            else:
                #先加入四个角，再把四边剩下来的递归处理（目前再处理角的问题上不引入折角，未来可以在此处引入）
                rect_tmp1 = co.rect_scale( four_points[0], four_points[1], four_points[2], four_points[3], corner*random.uniform(1.3,1.8), corner )
                result_set.add(  rect_tmp1 )
                rect_tmp2 = co.rect_scale( four_points[1], four_points[2], four_points[3], four_points[0], corner*random.uniform(1.3,1.8), corner )
                result_set.add(  rect_tmp2 )
                rect_tmp3 = co.rect_scale( four_points[2], four_points[3], four_points[0], four_points[1], corner*random.uniform(1.3,1.8), corner )
                result_set.add(  rect_tmp3 )
                rect_tmp4 = co.rect_scale( four_points[3], four_points[0], four_points[1], four_points[2], corner*random.uniform(1.3,1.8), corner )
                result_set.add(  rect_tmp4 )
                
                #
                result_set = result_set.union( roof_cut( co.rect_progress(rect_tmp1[1],rect_tmp2[3], co.get_l_point(rect_tmp1[1], rect_tmp1[2], corner*random.uniform(0.6,0.9)) ) ) )
                result_set = result_set.union( roof_cut( co.rect_progress(rect_tmp2[1],rect_tmp3[3], co.get_l_point(rect_tmp2[1], rect_tmp2[2], corner*random.uniform(0.6,0.9)) ) ) )
                result_set = result_set.union( roof_cut( co.rect_progress(rect_tmp3[1],rect_tmp4[3], co.get_l_point(rect_tmp3[1], rect_tmp3[2], corner*random.uniform(0.6,0.9)) ) ) )
                result_set = result_set.union( roof_cut( co.rect_progress(rect_tmp4[1],rect_tmp1[3], co.get_l_point(rect_tmp4[1], rect_tmp4[2], corner*random.uniform(0.6,0.9)) ) ) )


            return result_set

    # Kind4:Too Larger
    width_cut, height_cut = int(rect_width / bound_B + 1), int(rect_height / bound_B + 1)
    width_side, height_side = (rect_width - gap*(width_cut-1))/width_cut, (rect_height - gap*(height_cut-1))/height_cut

    for i in xrange(width_cut):
        for j in xrange(height_cut):
            #wrong
            p0 = co.get_rect_point( four_points[0], four_points[1], four_points[2], four_points[3], \
                                   i*(width_side+gap), j*(height_side+gap) )
                                   
            p1 = co.get_rect_point( four_points[0], four_points[1], four_points[2], four_points[3], \
                                   i*(width_side+gap)+width_side, j*(height_side+gap) )
                                   
            p2 = co.get_rect_point( four_points[0], four_points[1], four_points[2], four_points[3], \
                                   i*(width_side+gap)+width_side, j*(height_side+gap)+height_side )
            
            p3 = co.get_rect_point( four_points[0], four_points[1], four_points[2], four_points[3], \
                                   i*(width_side+gap), j*(height_side+gap)+height_side )
            
            result_set = result_set.union( roof_cut( (p0,p1,p2,p3) ) )

    return result_set


###Begin the main project###
###Just have a test###
if __name__ == "__main__":
    img_origin = open_image('./t2.png')
    shape = img_origin.shape
    img = detect_white_paper(img_origin)
    img = zyw_denoising(img)
    contour = find_paper_contour(img)
    points = find_contour_points(contour)
    
    img = perspective_transform( img_origin, points)
    
    img = separate_color( img, 1 )[0]
    
    img_gray = get_gray_image(img)
    
    img_gray = close_gap( img_gray, 9 )
    print type(img_gray),img_gray.shape,img_gray.dtype
    
    contours = get_contour_cornerlists(img_gray, img_draw=img_gray)
    print len(contours)
    
    cv2.imshow("jingguan",img_gray)
    cv2.waitKey(0)
    cv2.imwrite('tmp.jpg',img_gray)
    
    




