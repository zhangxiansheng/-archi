ArchiCV References
======
<h2>Image Processing</h2>
In this section there are different APIs on image processing about basic image operation and processing.
<hr>

<!--open_image-->
<code><b>open_image(address)</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L55">[source]</a>
<br><br>
<p>[<b><i>address</i></b>] is a string such like "./image_input.jpg", recommend to use  ".jpg" and ".png" as picture format.<br>
#Open a selected image file via its path and name as a variable <"numpy.ndarray">.
</p>

<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#open an image as <"numpy.ndarray">
#input address<"string">
#output image<"numpy.ndarray">
#<"numpy.ndarray">.dtype = unit8 (0-255)
#<"numpy.ndarray">.shape = (width, height, <3 is the Count of BGR>)
'''打开图像为numpy.ndarray类型的变量'''

img = archi.open_image("./image_input.jpg")
</pre>
</span>
<br><br>

<!--save_image-->
<code><b>save_image(address, img)</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L63">[source]</a>
<br><br>
<p>
[<b><i>address</i></b>] is a string such like "./image_input.jpg", recommend to use  ".jpg" and ".png" as picture format.<br>
[<b><i>img</i></b>] means which image you want to save and it is a variable <"numpy.ndarray">.<br>
#Save a selected image variable as a specified image file.
</p>
    
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#save <"numpy.ndarray"> as an image
#input output_address<"string">
#input image<"numpy.ndarray">
'''将numpy.ndarray类型的图像保存成图像文件'''

archi.save_image( "./image_output.jpg", img )
</pre>
</span>
<br><br>


<!--create_paper-->
<code><b>create_paper(shape, color=0)</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L72">[source]</a>
<br><br>
<p>
[<b><i>shape</i></b>] is an attribute of an image of the matrix of numpy, just the image class of openCV. This attribute is a tuple, like (width, height, depth), width means the width of the image, and the same with height. The depth is always 3 or 1, 3 means this is an RGB format, and 1 means this is a gray image. If depth is 1, always bypass it and just input (width, height).<br>
[<b><i>color</i></b>] means the pure color of the paper. This optional parameter can be only <"int"> between 0-255, and also <"tuple"> to express an RGB color. <br>
#Use a shape of an image and a selected color to generate an image variable at the class of <"numpy.ndarray">.
</p>
    
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#copy img.shape to create a vain paper
#0 mains Black and 255 mains White
#input1 shape<"tuple"> = <"numpy.ndarray">.shape = (width, height, <3 is the Count of BGR>)
#input2 color<"int"> = 0-255 or <"tuple"> = (255, 0, 255)
'''根据维度与颜色而预设生成一张纯色画布'''

width, height = 200, 300
shape = ( width, height, 3)
archi.create_paper( shape, 255 )
</pre>
</span>
<br><br>



<!--get_black_and_white_image-->
<code><b>get_black_and_white_image(image, threshold_value)</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L82">[source]</a>
<br><br>
<p>
[<b><i>image</i></b>] is an argument to mean the source image, which should be a grayscale image.<br>
[<b><i>threshold_value</i></b>] is used to classify the pixel values.  <br>
#It is a simple package for user indirectly to use the functhion of cv2.threshold. Although I recommend every archicv user best to learn openCV, but archicv want to more architects to directly program for themselves. So the function is simple and the name of every function is also simple. Just input a grayscale image and threshold_value(0-255), then output a black and white image.<br>
#This api maybe will be deleted or changed later.
</p>
<br><br>


<!--get_gray_image-->
<code><b>get_gray_image( image )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L93">[source]</a>
<br><br>
<p>
[<b><i>image</i></b>] means which image you want to transform to become a grayscale image <"numpy.ndarray">.<br>
#Input a colorscale image and output a grayscale image.
</p>

<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a colorful image
#input_image.shape = (width, height, <3 is the Count of BGR>)
#output a gray image
#output_image.shape = (width, height)
#input <"numpy.ndarray"> and output <"numpy.ndarray">
'''将RGB格式图像转换成灰度图像'''

img_output = archi.get_gray_image( img_input )
</pre>
</span>
<br><br>


<!--get_thick-->
<code><b>get_thick( img, a )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L100">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is an image numpy.ndarray to input.<br>
[<b><i>a</i></b>] means how many pixels to erode and make the lines to be thicker.<br>
#Function of make black lines in the picture thicker at a selected value of how many pixels to erode.
</p>

<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input image <"numpy.ndarray">
#output image <"numpy.ndarray">
'''腐蚀图像 = 加粗图像线条'''

img_output = archi.get_thick( img_input, 12 )
</pre>
</span>
<br><br>



<!--get_thin-->
<code><b>get_thin( img, a )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L111">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is an image numpy.ndarray to input.<br>
[<b><i>a</i></b>] means how many pixels to dilate and make the lines to be thiner.<br>
#Function of make black lines in the picture thiner at a selected value of how many pixels to dilate.
</p>

<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input image <"numpy.ndarray">
#output image <"numpy.ndarray">
'''膨胀图像 = 变细图像线条'''

img_output = archi.get_thin( img_input, 12 )
</pre>
</span>
<br><br>


<!--close_gap-->
<code><b>close_gap( img, a )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L122">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is an image numpy.ndarray to input.<br>
[<b><i>a</i></b>] means to close gaps within a value, how large the gaps can be closed.<br>
#Function of close gaps at a selected value is two steps as get_thick and then get_thin.
</p>

<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input image <"numpy.ndarray">
#output image <"numpy.ndarray">
 '''缝合缺口 = 先加粗a个单位，再变细a个单位'''

img_output = archi.close_gap( img_input, 12 )
</pre>
</span>
<br><br>


<!--separate_color-->
<code><b>separate_color( img, n )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L133">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is an image numpy.ndarray to input.<br>
[<b><i>n</i></b>] means how many kinds of colors to need to be separated, and the white color is excluded in n.<br>
#This api is the use of K-means marchine learning. The second argument n is equal to K-1, which means how many kinds of colors to separate except white color.<br>
#Input an image to separate its colors and tell the argument n <"int"><br>
#Output an image list with n elements and each means a separated color.
</p>

<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a multiple-color image <"numpy.ndarray">
#input N = K - 1 (K is K-means machine learning)
#input N means how many meaningful colors except white
#output a List of image <"numpy.ndarray">
'''K-means方法进行色彩分离'''

img_list = archi.separate_color( img_input, 3 )
print len( img_list )
>>> 3
</pre>
</span>
<br><br>


<h2>Feature Detection and Optimization</h2>
In this section there are different APIs on feature detection and optimization.
<hr>

<!--separate_color-->
<code><b>get_contour_cornerlists(img_gray, img_draw=None, <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;thresh_mode=cv2.THRESH_BINARY, limit_caught=70 )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L175">[source]</a>
<br><br>
<p>
[<b><i>img_gray</i></b>] is an image numpy.ndarray to input which is grayscale.<br>
[<b><i>img_draw</i></b>] is an optional argument which means making an image show the detected contours.<br>
[<b><i>thresh_mode</i></b>] is an optional argument to control the model of threshold. <br>The default parameter is cv2.THRESH_BINARY which is equal to 1.<br> There are five modes of threshold, they are cv2.THRESH_BINARY=0, cv2.THRESH_BINARY_INV=1, cv2.THRESH_TRUNC=2, cv2.THRESH_TOZERO=3, cv2.THRESH_TOZERO_INV=4. The most frequent using is cv2.THRESH_BINARY and cv2.THRESH_BINARY_INV. More about this argument is with how to get a binary image with cv2.threshold.
<br>
[<b><i>limit_caught</i></b>] is an optional argument to control the lower limit of how many points in which contour should be detected so as to remove some of the noise from detected results.<br>
#This API is used to detect all the inner contours in a gray image as a list of contours.
</p>


<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input1 img_gray <"numpy.ndarray"> which shape is just (width, height)
#input2 img_draw is for the contours to be drawt on
#output cornerlists=[cornerlist1,cornerlist2...]
#cornerlist[i]=[(x1,y1), (x2,y2), (x3,y3)...]
'''根据灰度图片识别出所有的内轮廓的点集'''

cornerlists = archi.get_contour_cornerlists( img_gray )
</pre>
</span>
<br><br>



<!--get_rectangle-->
<code><b>get_rectangle( contour )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L207">[source]</a>
<br><br>
<p>
[<b><i>contour</i></b>] is a list of contour points, such like [(x1,y1), (x2,y2)...]<br>
#Get the smallest rectangle which can include all the contour points.
</p>

<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#get a uniformal rectangle
#input a contour list [(x1,y1), (x2,y2)...]
#output rectangle<"list"> [center(x,y),size(width,height),angle]
'''根据一个矩形内轮廓角点集识别出此矩形'''

contour = [ (0,1), (1,2), (2,1), (1,0) ]
rectangle = archi.get_rectangle( contour )
print rectangle
>>> [(0.9999999403953552, 1.0), (1.4142134189605713, 1.4142134189605713), -45.0]
</pre>
</span>
<br><br>




<!--machine_classify-->
<code><b>machine_classify( rectangles )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L224">[source]</a>
<br><br>
<p>
[<b><i>rectangles</i></b>] is a list of rectangles, just like [rectangle1, rectangle2, rectangle3...] <br>and each rectangle is a list like [ (center_x, center_y), (width, height), angle ].<br>
#Output is a list of lists which contain rectangles at approximately the same angles and orientations, <br>just like [ [rect1,rect2...], [rect8, rect9..].. ] and each rectangle is not at class of list but tuple, which is at the format of ( (center_x, center_y), (width, height), angle_adjusted )<br>
#This function is to classify different rectangles by the standard of angle. And this function maybe has a very little bug existing.
</p>

<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a list of rectangles
#output <"list"> = [ [rect1,rect2...], [rect8, rect9..]..]
#output's every rect is not a list but a tuple
#recti = (center(x,y), size(width,height), angle_adjusted)
'''根据矩形的角度对矩形进行角度优化与分类'''

rect1 = [(0.99, 1.0), (1.4, 13), -40.0]
rect2 = [(6.11, 4.0), (1.4, 32), -41.0]
rect3 = [(4.33, 1.0), (1.4, 14), 14.01]
rect4 = [(2.44, 4.0), (1.4, 23), -14.5]
rect5 = [(9.24, 4.0), (1.4, 10), -13.5]
rect6 = [(2.24, 2.0), (1.4, 10), 13.53]
rectangles_list = [ rect1, rect2, rect3, rect4, rect5, rect6 ]
rectangles_classified = archi.machine_classify( rectangles_list )

print len( rectangles_classified )
for i in rectangles_classified: print i

>>> 3
>>>[ ((0.99, 1.0), (1.4, 13), -40.0), ((6.11, 4.0), (1.4, 32), -41.0) ]
>>>[ ((4.33, 1.0), (1.4, 14), 14.01), ((2.24, 2.0), (1.4, 10), 13.53) ]
>>>[ ((2.44, 4.0), (1.4, 23), -14.5), ((9.24, 4.0), (1.4, 10), -13.5) ]
</pre>
</span>
<br><br>


<!--machine_optimize-->
<code><b>machine_optimize( rectangles )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L259">[source]</a>
<br><br>
<p>
[<b><i>rectangles</i></b>] is just the results of machine_classify(), which is is a list of lists which contain rectangles at approximately the same angles and orientations, just like [ [rect1,rect2...], [rect8, rect9..].. ] and each rectangle is not at class of list but tuple, which is at the format of ( (center_x, center_y), (width, height), angle_adjusted )<br>
#Input the argument above, and output the same list of rectangles but in another format of each rectangle element as the tuple of four corner points like (point1, point2, point3, point4), which is adjusted at the standards of whether each two rectangles are designed border-upon or border-in-one-orientation by landscape architect or what is better as a plan designed or planned.
</p>

<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input <"list"> = [ [rect1,rect2...], [rect8, rect9..]..]
#input recti = (center(x,y), size(width,height), angle_adjusted)
#output <"list"> = [ [rect1,rect2...], [rect8, rect9..]..]
#output recti = (point1, point2, point3, point4)
'''对列表中的矩形进行边角重合并线优化'''

list1 = [ ((0.99, 1.0), (1.4, 13), -40.0), ((6.11, 4.0), (1.4, 32), -41.0) ]
list2 = [ ((4.33, 1.0), (1.4, 14), 14.01), ((2.24, 2.0), (1.4, 10), 13.53) ]
list3 = [ ((2.44, 4.0), (1.4, 23), -14.5), ((9.24, 4.0), (1.4, 10), -13.5) ]
rectangles_input = [ list1, list2, list3 ]

#get the result
rectangles_output = archi.machine_optimize( rectangles_input )

#output the result
print len( rectangles_output )
for rect_list in rectangles_output:
    print "#"
    print "rectangles list:"
    for rect in rect_list:
        print "a rectangle four points:"
        for point in rect: print point

>>>3
>>>#
>>>rectangles list:
>>>a rectangle four points:
>>>(5.824828974499669, 5.428244221929315)
>>>(-2.5314100698091937, -4.530333679701778)
>>>(-2.5314099933536567, -4.530333588585617)
>>>(5.824829069844625, 5.428244335557009)
>>>a rectangle four points:
>>>(15.530270251606769, 16.994738731633838)
>>>(-5.035801007514753, -7.51495057697276)
>>>(-5.05150657862965, -7.533667747772683)
>>>(15.51456483973066, 16.976021750607316)
>>>#
>>>rectangles list:
>>>a rectangle four points:
>>>(3.263969464572509, 1.4977746904006708)
>>>(3.263969464572509, 1.4977746904006708)
>>>(3.263969464572509, 1.4977746904006708)
>>>(3.263969464572509, 1.4977746904006708)
>>>a rectangle four points:
>>>(3.263969464572509, 1.4977746904006708)
>>>(3.263969464572509, 1.4977746904006708)
>>>(3.263969464572509, 1.4977746904006708)
>>>(3.263969464572509, 1.4977746904006708)
>>>#
>>>rectangles list:
>>>a rectangle four points:
>>>(7.946251592276422, 11.970011440466621)
>>>(2.789724742426462, -7.968798454045148)
>>>(2.789724734546405, -7.968798484515068)
>>>(7.946251592276422, 11.970011440466621)
>>>a rectangle four points:
>>>(7.946251592276422, 11.970011440466621)
>>>(4.840619542763151, -0.03857667332354334)
>>>(4.846737105904849, -0.014921811814667332)
>>>(7.946251592276422, 11.970011440466621)
</pre>
</span>
<br><br>




<!--adjust_rect_list-->
<code><b> adjust_rect_list( angle, rectangle_list )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L281">[source]</a>
<br><br>
<p>
[<b><i>angle</i></b>] is the adjusted angle of a list of rectangles which have the nearest angle.<br>
[<b><i>rectangle_list</i></b>] the list of rectangles said above of which element is the tuple of four corner points tuple.<br>
#This is a complicated core functhion to support machine_optimize(), which is adjusting each rectangle element by the standards of which members are border-upon or border-in-one-orientation.
#This functhion is not perfect enough in optimization design and algorithms which is worth to update future.
</p>

<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input one rectangle list
#input  <"list"> = [rect1,rect2...]
#input recti = (point1, point2, point3, point4)
#output <"list"> = [rect1_adjusted,rect2_adjusted...]
'''边角重合并线优化的核心处理函数'''

result_list = archi.adjust_rect_list( angle, rectangle_list )
</pre>
</span>
<br><br>




<!--get_circle_tree-->
<code><b>get_circle_tree( img, close_value = 20, img_show = None, limit_caught=70 )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L381">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is a grayscale image to input on which are circles to express the tree design or plan with.<br>
[<b><i>close_value</i></b>] is a values to control closing the gaps on the image above which affect detecting. If close_value is zero, skip closing gaps. The default value is 20 pixels.<br>
[<b><i>img_show</i></b>] is a canvas for representing the progress of recognization of tree circles.<br>
[<b><i>limit_caught</i></b>] is a value to control the smallest contour to be detected. The default value is 70 points in one contour detected.<br>
#In the working of landscape architect, circles is always  a kind of expressing that one circle means one tree because tree crown projections are circles. This functhion is used to recognize circles. The default values are based on experience but which are not perfect enough. And there are different kinds of algorithms to do this detecting job, such as HoughCircle, contours detecting and so on, here is with use fo contours detecting. This api is not perfect but not worth to update. Because its functhion is not the most helpful in the working of landscape architect, although landscape architect are of more touch with trees than other architect.  Not to be the most helpful functhion is according to that the working about tree drawing or other graphics operations about tree is not the most time-consuming work. The case is applied to the recognization of revclound, lakestrandlines.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a gray img <"numpy.ndarray">
#input close_value is used to forbid some small crossing
#recommended close_value = 20
#if close_gap the img out of this def then set close_value 0
#output a set of tuples like ( center, radius )
'''识别点状树木图标'''

circle_list = archi.get_circle_tree( img_gray )
</pre>
</span>
<br><br>






<!--get_lake_strandline-->
<code><b>get_lake_strandline( img, close_value = 4, img_show = None )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L409">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is a grayscale image to input on which are lakestrandlines.<br>
[<b><i>close_value</i></b>] is a values to control closing the gaps on the image above which affect detecting. If close_value is zero, skip closing gaps. The default value is 4 pixels.<br>
[<b><i>img_show</i></b>] is a canvas for representing the progress of recognization of lakestrandlines.<br>
#The api to close gaps and detect the contours of lake strandlines, including island strandline in lake.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a gray img <"numpy.ndarray">
#input close_value is used to forbid some small crossing
#recommended close_value = 20
#if close_gap the img out of this def then set close_value 0
#output a list of contour points
'''识别湖岸线'''

contour_list = archi.get_lake_strandline( img_gray )
</pre>
</span>
<br><br>





<!--get_tree_revclound-->
<code><b>get_tree_revclound( img, close_value = 10, img_show = None )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L438">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is a grayscale image to input on which is tree revclound.<br>
[<b><i>close_value</i></b>] is a values to control closing the gaps on the image above which affect detecting. If close_value is zero, skip closing gaps. The default value is 10 pixels.<br>
[<b><i>img_show</i></b>] is a canvas for representing the progress of recognization of tree revclound.<br>
#The api to close gaps and detect the contours of tree revclound.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a gray img <"numpy.ndarray">
#input close_value is used to forbid some small crossing
#recommended close_value = 10
#if close_gap the img out of this def then set close_value 0
#output a list of contour points
'''识别树丛云线'''

contour_list = archi.get_tree_revclound( img_gray )
</pre>
</span>
<br><br>




<h2>Draw CAD Results</h2>
In this section there are different APIs on drawing results in the format of ".dxf" with use of SDXF library.<br>
SDXF library is an open source python library invented by Stany which is included in archicv and the bug of polylines and lwpolylines is mended in the SDXF module in archicv. SDXF is a simple but great helpful library. <br>Thanks for Stany. Hope more geeks to fork SDXF on github and to develop it, which is very helpful.
<hr>




<!--open_dxf-->
<code><b>open_dxf() </b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L479">[source]</a>
<br><br>
<p>
#The api is to open a variable which means a space to store the output primitive.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#output a dxf_drawing <type 'instance'>
'''生成dxf绘图域,并对图层进行初始化'''

drawing = archi.open_dxf()
</pre>
</span>
<br><br>


<!--save_dxf-->
<code><b>save_dxf( drawing, save_address_name )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L493">[source]</a>
<br><br>
<p>
[<b><i>drawing</i></b>] is the variable of drawing space which will be saved.<br>
[<b><i>save_address_name</i></b>] is a string which is file saving path and name.<br>
#The api is to save the variable of drawing space as a file with the format of ".dxf"
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#output a dxf_drawing <type 'instance'>
'''生成dxf绘图域,并对图层进行初始化'''

drawing = archi.open_dxf()
archi.save_dxf( drawing, "./output.dxf" )
</pre>
</span>
<br><br>




<!--dxf_draw_roof-->
<code><b>dxf_draw_roof( drawing, list_of_roof )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L500">[source]</a>
<br><br>
<p>
[<b><i>drawing</i></b>] is the variable of drawing space.<br>
[<b><i>list_of_roof</i></b>] is the results of building recognization, just the element of direct result of machine_optimize(), which is a list of each building data.<br>
#The api has a functhion of drawing the show and expression of results of building recognization on the dxf drawing space.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a dxf_drawing <type 'instance'>
#input list_of_roof <'set'> or <'list'>
'''在指定drawing域中绘制屋顶'''

drawing = archi.open_dxf()
for list_of_roof in results_roof_recognize_and_optimize:
    archi.dxf_draw_roof(drawing, list_of_roof)
</pre>
</span>
<br><br>


<!--dxf_draw_tree-->
<code><b>dxf_draw_tree( drawing, list_of_tree )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L540">[source]</a>
<br><br>
<p>
[<b><i>drawing</i></b>] is the variable of drawing space.<br>
[<b><i>list_of_tree</i></b>] is the results of tree circles recognization, just the element of direct result of get_circle_tree(), which is a list of each tree circle.<br>
#The api has a functhion of drawing the show and expression of results of tree circles recognization on the dxf drawing space.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a dxf_drawing <type 'instance'>
#input list_of_tree means circles <'list'> or <'set'>
 '''在指定drawing域中绘制点树'''

drawing = archi.open_dxf()
archi.dxf_draw_tree( drawing, list_of_tree )
</pre>
</span>
<br><br>




<!--dxf_draw_lake-->
<code><b>dxf_draw_lake( drawing, list_of_lake )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L548">[source]</a>
<br><br>
<p>
[<b><i>drawing</i></b>] is the variable of drawing space.<br>
[<b><i>list_of_lake</i></b>] is the results of lake strandlines recognization, just the element of direct result of get_lake_strandline(), which is a list of each lakestrandline.<br>
#The api has a functhion of drawing the show and expression of results of lake strandlines recognization on the dxf drawing space.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a dxf_drawing <type 'instance'>
#input list_of_lake mean lake_strandlines <'list'> or <'set'>
 '''在指定drawing域中绘制湖岸线'''

drawing = archi.open_dxf()
archi.dxf_draw_lake( drawing, list_of_lake )
</pre>
</span>
<br><br>



<!--dxf_draw_revclound-->
<code><b>dxf_draw_revclound( drawing, list_of_revclound )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L556">[source]</a>
<br><br>
<p>
[<b><i>drawing</i></b>] is the variable of drawing space.<br>
[<b><i>list_of_revclound</i></b>] is the results of tree revclounds recognization, just the element of direct result of get_tree_revclound(), which is a list of each revclound.<br>
#The api has a functhion of drawing the show and expression of results of tree revclound recognization on the dxf drawing space.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a dxf_drawing <type 'instance'>
#input list_of_revclound <'list'> or <'set'>
'''在指定drawing域中绘制修行云线'''

drawing = archi.open_dxf()
archi.dxf_draw_revclound( drawing, list_of_revcloud )
</pre>
</span>
<br><br>




<h2>JS call Canvas Based on Json Results</h2>
In this section there are different APIs on generate drawing data at the format of Json. If the job of recognization and optimization are done on the server and via json traffic the client can with use of javascript to call the canvas tag of html5 to draw expression of result data. ProcessingX.js is one of my another open source library developing on github, which can easily call canvas to draw. There are two kinds of json results to transfer. One is to generate the data which can directly draw with every details, the other is to generate only the results of recognization and optimization, the details will be calculated on the client in order to  reduce the server pressure and network traffic. So archicv has only done the latter.
<hr>

<!--get_roof_json-->
<code><b>get_roof_json( list_of_roof, need_dic=None )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L601">[source]</a>
<br><br>
<p>
[<b><i>list_of_roof</i></b>] is the results of building recognization, just the element of direct result of machine_optimize(), which is a list of each building data.<br>
[<b><i>need_dic</i></b>] is to control whether the result is the format of a json string or a python dictionary. The default value is None, which mean the result is a json string. If the value is "dic", the result to output will be a python dict.<br>
#The api is to generate the results of building recognization and optimization at the format of dict or json.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

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
'''返回roof类型的JSON数据'''

roof_json = archi.get_roof_json( list_of_roof )
</pre>
</span>
<br><br>



<!--get_tree_json-->
<code><b>get_tree_json( list_of_tree, need_dic=None )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L630">[source]</a>
<br><br>
<p>
[<b><i>list_of_tree</i></b>] is the results of tree circle recognization, just the element of direct result of machine_optimize(), which is a list of each building data.<br>
[<b><i>need_dic</i></b>] is to control whether the result is the format of a json string or a python dictionary. The default value is None, which mean the result is a json string. If the value is "dic", the result to output will be a python dict.<br>
#The api is to generate the results of tree circle recognization and optimization at the format of dict or json.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

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
'''返回tree类型的JSON数据'''

tree_json = archi.get_tree_json( list_of_tree )
</pre>
</span>
<br><br>



<!--get_lake_json-->
<code><b>get_lake_json( list_of_lake, need_dic=None )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L657">[source]</a>
<br><br>
<p>
[<b><i>list_of_lake</i></b>] is the results of lake strandline recognization, just the element of direct result of machine_optimize(), which is a list of each building data.<br>
[<b><i>need_dic</i></b>] is to control whether the result is the format of a json string or a python dictionary. The default value is None, which mean the result is a json string. If the value is "dic", the result to output will be a python dict.<br>
#The api is to generate the results of lake strandlines recognization and optimization at the format of dict or json.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

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
'''返回lake类型的JSON数据'''

lake_json = archi.get_lake_json( list_of_lake )
</pre>
</span>
<br><br>





<!--get_lake_json-->
<code><b>get_revclound_json( list_of_revclound, need_dic=None )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L686">[source]</a>
<br><br>
<p>
[<b><i>list_of_lake</i></b>] is the results of tree revclound recognization, just the element of direct result of machine_optimize(), which is a list of each building data.<br>
[<b><i>need_dic</i></b>] is to control whether the result is the format of a json string or a python dictionary. The default value is None, which mean the result is a json string. If the value is "dic", the result to output will be a python dict.<br>
#The api is to generate the results of tree revclound recognization and optimization at the format of dict or json.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

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
'''返回lake类型的JSON数据'''

revclound_json = archi.get_revclound_json( list_of_revclound )
</pre>
</span>
<br><br>




<h2>Draw Results with OpenCV</h2>
In this section there are different APIs on drawing results to image files via OpenCV library.
<hr>



<!--cv_draw_roof-->
<code><b>cv_draw_roof( img, list_of_roof )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L713">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is the variable of drawing space at class of numpy.ndarray.<br>
[<b><i>list_of_roof</i></b>] is the results of building recognization, just the element of direct result of machine_optimize(), which is a list of each building data.<br>
#The api has a functhion of drawing the show and expression of results of building recognization on the image drawing space.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input img <'numpy.ndarray'>
#input list_of_roof <'set'> or <'list'>
 '''通过OpenCV在指定img中绘制屋顶'''

for list_of_roof in results_roof_recognize_and_optimize:
    archi.cv_draw_roof(img, list_of_roof)
</pre>
</span>
<br><br>


<!--cv_draw_tree-->
<code><b>cv_draw_tree( img, list_of_tree )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L753">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is the variable of drawing space at class of numpy.ndarray.<br>
[<b><i>list_of_tree</i></b>] is the results of tree circles recognization, just the element of direct result of get_circle_tree(), which is a list of each tree circle.<br>
#The api has a functhion of drawing the show and expression of results of tree circles recognization on the image drawing space.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input img <'numpy.ndarray'>
#input list_of_tree means circles <'list'> or <'set'>
 '''通过OpenCV在指定img中绘制点树'''

archi.cv_draw_tree( img, list_of_tree )
</pre>
</span>
<br><br>




<!--cv_draw_lake-->
<code><b>cv_draw_lake( img, list_of_lake )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L761">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is the variable of drawing space at class of numpy.ndarray.<br>
[<b><i>list_of_lake</i></b>] is the results of lake strandlines recognization, just the element of direct result of get_lake_strandline(), which is a list of each lakestrandline.<br>
#The api has a functhion of drawing the show and expression of results of lake strandlines recognization on the image drawing space.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input img <'numpy.ndarray'>
#input list_of_lake mean lake_strandlines <'list'> or <'set'>
 '''通过OpenCV在指定img中绘制湖岸线'''

archi.cv_draw_lake( img, list_of_lake )
</pre>
</span>
<br><br>



<!--cv_draw_revclound-->
<code><b>cv_draw_revclound( img, list_of_revclound )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L769">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is the variable of drawing space at class of numpy.ndarray.<br>
[<b><i>list_of_revclound</i></b>] is the results of tree revclounds recognization, just the element of direct result of get_tree_revclound(), which is a list of each revclound.<br>
#The api has a functhion of drawing the show and expression of results of tree revclound recognization on the image drawing space.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input img <'numpy.ndarray'>
#input list_of_revcloud <'list'> or <'set'>
'''通过OpenCV在指定img中绘制修行云线'''

archi.cv_draw_revclound( img, list_of_revcloud )
</pre>
</span>
<br><br>







<h2>Paper Perspective Transform</h2>
In this section there are different APIs on paper perspective transform.
<hr>

<!--detect_white_paper-->
<code><b>detect_white_paper( img, value=127 )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L783">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is the photo for detecting at class of numpy.ndarray.<br>
[<b><i>value</i></b>] is threshold value to detect white color.<br>
#There are two kinds of ideas to transform a perspective paper, HoughLines idea and paper color detecting. So this api is to find the range of white color, which is the color of paper. The algorithms to detect white paper is not only detect_white_paper(), and separate_color() also can do for the same target. More details can be found in tutorial.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a img
#output a grayscale img
'''用颜色来感应出白纸'''

img = open_image( "./img_input.jpg" )
img_paper = archi.detect_white_paper( img )
</pre>
</span>
<br><br>


<!--zyw_denoising-->
<code><b>zyw_denoising( img, fade_value=13, rise_value=66 )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L792">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is often the result of detect_white_paper(), which is needing denoising.<br>
[<b><i>fade_value</i></b>] is an argument to control denoising effect which default value is 13.<br>
[<b><i>rise_value</i></b>] is an argument to control denoising effect which default value is 66.<br>
#Close gaps is the combine functhions between get_thick and get_thin. The api zyw_denoising is another kind of combination between get_thin and get_thick.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a grayscale img
#output a grayscale img
'''苇式去噪法'''

img = open_image( "./img_input.jpg" )
img_paper = archi.detect_white_paper( img )
img_paper = archi.denoising( img_paper )
</pre>
</span>
<br><br>



<!--find_paper_contour-->
<code><b>find_paper_contour( img, thresh_mode=1 )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L803">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is the grayscale image input for detecting.<br>
[<b><i>thresh_mode</i></b>] is an optional argument to control the model of threshold. <br>The default parameter is cv2.THRESH_BINARY which is equal to 1.<br> There are five modes of threshold, they are cv2.THRESH_BINARY=0, cv2.THRESH_BINARY_INV=1, cv2.THRESH_TRUNC=2, cv2.THRESH_TOZERO=3, cv2.THRESH_TOZERO_INV=4. The most frequent using is cv2.THRESH_BINARY and cv2.THRESH_BINARY_INV. More about this argument is with how to get a binary image with cv2.threshold.

#The api is to find the contour of paper which is the longest contour in detected.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a gray img
#output the longest one of contours
#the longest one means paper
'''识别纸张的轮廓线'''

img = open_image( "./img_input.jpg" )
img_paper = archi.detect_white_paper( img )
img_paper = archi.denoising( img_paper )
contour = archi.find_paper_contour( img_paper )
</pre>
</span>
<br><br>



<!--find_contour_points-->
<code><b>find_contour_points( contour )</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L822">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is a rectangle contour list.<br>

#The api is to exactly find the four points of the rectangle.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input a contour
#output four points
#[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
#x,y numpy.float64
'''识别轮廓线4个角点'''

img = open_image( "./img_input.jpg" )
img_paper = archi.detect_white_paper( img )
img_paper = archi.denoising( img_paper )
contour = archi.find_paper_contour( img_paper )
four_points = archi.find_contour_points( contour )
</pre>
</span>
<br><br>



<!--perspective transform-->
<code><b>perspective_transform( img, points, <br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;paper_width=1684, paper_height=1191, paper_mode='A4-h')</b></code> <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/archi.py#L852">[source]</a>
<br><br>
<p>
[<b><i>img</i></b>] is the origin image for perspective transform.<br>
[<b><i>points</i></b>] is the tuple or list of four corner points for perspective transform.<br>
[<b><i>paper_width</i></b>] is width of paper in the origin image.<br>
[<b><i>paper_height</i></b>] is height of paper in the origin image.<br>
[<b><i>paper_mode</i></b>] is kind of size of paper in the origin image, the default value is "A4-h", there are 8 modes of paper size, which are "A4-h", "A4-v", "A3-h", "A3-v", "A2-h", "A2-v", "A1-h", "A1-v". "h" means horizontal, "v" means vertical. If paper_mode is set,the values of the paper_width and paper_height will be changed, no matter whether they are set.<br>

#The api is to perspective transform an origin with the argument of four points to another size of image canvas.
</p>
<b>&nbsp;example:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#input points [ up_left_point, up_right_point, down_right_point, down_left_point ]
#output image
'''透视转换成正视'''

img = open_image( "./img_input.jpg" )
img_paper = archi.detect_white_paper( img )
img_paper = archi.denoising( img_paper )
contour = archi.find_paper_contour( img_paper )
four_points = archi.find_contour_points( contour )
img_paper = archi.perspective_transform( img, four_points )
</pre>
</span>
<br><br>
