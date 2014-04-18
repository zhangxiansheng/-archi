archiCV
======

OpenCV work for Architecture, especially the Landscape Architecture, and we free the so-called LA planning or design workers, because only we free the architector then they can do the true thing not just be used as a tool to copy picture to cad or to just make a picture more beautiful but not to make the true design and plan.

more details on ArchiCV website: http://www.caup.cn

<!--start-->
<h2>Get started</h2>
Install and start to use archicv.
<hr>
<code><b>$pip install archicv</b></code>
<br><br>
<p>
Archicv is a python library, so it's recommended to use pip to install archicv.<br>
Archicv is based on OpenCV and NumPy, so that required to install OpenCV and NumPy.<br>
NumPy is easy to install, <code>$pip install numpy</code> is the best way.<br>
If you use Mac OS system, we recommend much the use of HomeBrew to install opencv, <br>
just one step, <code>$brew install opencv</code>.If you are using Ubuntu, you can use pip or apt-get to install opencv. <br>
On mac, pip can't install opencv.<br>
There are three ways to install archicv, <code>$pip install archicv</code> and <code>$easy_install archicv</code>, pip is more recommended. The third way is download the setup package of archicv from <a href="https://pypi.python.org/pypi/archicv">pypi</a>, and install it manually.
</p>

<b>&nbsp;pip:</b>
<span class="pre-python">
<pre>
$pip install numpy
$brew install opencv

$pip install archicv
</pre>
<b>&nbsp;easy_install:</b>
<pre>
$pip install numpy
$brew install opencv

$easy_install archicv
</pre>
<b>&nbsp;manually install:</b>
<pre>
$pip install numpy
$brew install opencv
    
$tar -xf archicv archicv-0.0.1.18.32.tar.gz
$cd archicv-0.0.1.18.32
$python setup.py install
</pre>
<br>
<p>
When successfully install the library,
<br>
we can have a test to write a little program to generate a ".jpg" file from a ".png" one.
</p>
<b>&nbsp;example.py:</b>
<pre>
import archicv.archi as archi

#open an image as <"numpy.ndarray">
img = archi.open_image( "./image_input.png" )

#save <"numpy.ndarray"> as an image
archi.save_image( "./image_output.jpg", img )
</pre>
</span>
<br><br>


<!--read image-->
<h2>Read An Image</h2>
How to read an image as a variable at the class of numpy.ndarray.
<hr>
<p>
Just input the file address and name with format,<br>
and output a variable at the class of numpy.ndarray.
</p>
<b>&nbsp;ReadImage.py:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#open an image as <"numpy.ndarray">
img = archi.open_image( "./image_input.png" )
</pre>
</span>
<br><br>

<!--perspective-->
<h2>Perspective Transform</h2>
Perspective transform an image within a white paper.
<hr>
<p>
There are several algorithms to do this work.<br>
One is via HoughLines to detect the contour of paper, and other two are via paper color to detect paper.<br>
Below is two examples via color to detect a paper and perspective transform it. One is using white color to detect directly, the other is using K-means marchine learning to detect the paper.<br>


<b>left:</b> image_input.png  <br><b>right:</b> image_perspective_transformed.jpg<br>
<img src="http://www.caup.cn/static/demo-perspective.jpg" class="img-thumbnail" style="width:38%">
<img src="http://www.caup.cn/static/result-perspective.jpg"  class="img-thumbnail" style="width:40%">
<br>

</p>

<b>&nbsp;Perspective1.py:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#open an image as <"numpy.ndarray">
img = archi.open_image( "./image_input.png" )

#directly detect paper color
img_tmp = archi.detect_white_paper( img )

#zyw denoising
img_tmp = archi.zyw_denoising( img_tmp )

#find the contour of paper
contour = archi.find_contour_points( img_tmp, thresh_mode=0 )

#find four corner points of paper
points = archi.find_contour_points( contour )

#perspective transform
img_output = archi.perspective_transform( img, points )

#save image
archi.save_image( "./image_perspective_transformed.jpg", img_output )
</pre>
<b>&nbsp;Perspective2.py:</b>
<pre>
import archicv.archi as archi

#open an image as <"numpy.ndarray">
img = archi.open_image("./image_input.png")

#K-means to detect paper color
img_tmp = archi.separate_color( img, 1 )[0]

#get a grayscale image
img_tmp = archi.get_gray_image( img_tmp )

#find the contour of paper
contour = archi.find_contour_points( img_tmp, thresh_mode=0 )

#find four corner points of paper
points = archi.find_contour_points( contour )

#perspective transform
img_output = archi.perspective_transform( img, points )

#save image
archi.save_image( "./image_perspective_transformed.jpg", img_output )
</pre>
</span>


<br><br>


<!--gray image-->
<h2>Get A Gray Image</h2>
Transform an image to a grayscale image.
<hr>
<p>
Input a colorscale image at the class of numpy.ndarray,<br>
and output a variable which is the grayscale image at class of numpy.ndarray.
</p>
<b>&nbsp;GrayScale.py:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#open an image as <"numpy.ndarray">
img = archi.open_image("./image_perspective_transformed.jpg")

#get a grayscale image as <"numpy.ndarray">
img_gray = archi.get_gray_image( img )
</pre>
</span>
<br><br>



<!--separate-->
<h2>Separate Color</h2>
Use K-means to separate multiple meaningful colors in one image.
<hr>
<p>
Each kind of color has one meaning, such like buildings or lakestrand or others.<br>
So for recognition, multiple colors should be separated to different image matrixs.<br>
This is doing how to separate different colors through K-means algorithms.
</p>
<b>&nbsp;Separate.py:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#open an image as <"numpy.ndarray">
img = archi.open_image("./image_input.jpg")

#set n
n = 3

#separate colors to 3 kinds
img_list = archi.separate_color( img, n )

#save each result image
for i in xrange(n):
    archi.save_image( "./image_output" + str(i) + ".jpg", img_list[i] )
</pre>
</span>

<img src="http://www.caup.cn/static/demo-separate.jpg" class="img-thumbnail" style="width:24.6%">
<img src="http://www.caup.cn/static/result-separate1.jpg" class="img-thumbnail" style="width:24.6%">
<img src="http://www.caup.cn/static/result-separate2.jpg" class="img-thumbnail" style="width:24.6%">
<img src="http://www.caup.cn/static/result-separate3.jpg" class="img-thumbnail" style="width:24.6%">
<b>pic1:</b> image_input.jpg&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<b>pic2:</b> image_output0.jpg&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<b>pic3:</b> image_output1.jpg&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<b>pic4:</b> image_output2.jpg
<br><br><br>
<!--close gaps-->
<h2>Close Gaps</h2>
Close gaps at a selected value.
<hr>
<p>
Hand drawing is also not accurate so that there are small gaps which will affect recognition program performance.<br>
Function of close gaps at a selected value is required.<br>
<b>left:</b> image_input.png <br><b>right:</b> image_gap_closed.jpg<br>
<img src="http://www.caup.cn/static/demo-gaps.jpg" class="img-thumbnail" style="width:49.7%">
<img src="http://www.caup.cn/static/result-gaps.jpg"  class="img-thumbnail" style="width:49.7%">
<br>

</p>

<b>&nbsp;CloseGaps.py:</b>
<span class="pre-python">
<pre>
import archicv.archi as archi

#open an image as <"numpy.ndarray">
img = archi.open_image( "./image_input.png" )

#set n
n = 12

#close gaps below n pixels
img_output = archi.close_gap( img, n )

#save image
archi.save_image( "./image_gap_closed.jpg", img_output )
</pre>
</span>


<br><br>





<!--roof-->
<h2>Recognize Buildings</h2>
Recognization of which are buildings, Optimization, Drawing.
<hr>
<p>
There are different kinds of drawing buildings on a plan picture.<br>
It is often wise to uniform an easiest kind of drawing for eaier drawing and easier recognization.<br>
So just drawing the contour of buildings is the wisest way to express the landscape planning and design.<br>
Then detect the contour and optimize the results from the need of working of a landscape architect.<br>
There are three kinds of results output, and they are cad results, json datas and image file from OpenCV.<br>
At the example below, it will show two kinds of results, cad result and image file output via OpenCV.<br>
Now there are still some bugs of recognize of some special cases of buildings, such as courtyard combination.<br>
For wise develop, less is more, and it only recognizes the rectangle and overlooks other kinds.<br>



<b>left:</b> image_input.png  <br><b>right:</b> image_roof_result.jpg<br>
<img src="http://www.caup.cn/static/result-gaps.jpg" class="img-thumbnail" style="width:49.7%">
<img src="http://www.caup.cn/static/result-roof.jpg"  class="img-thumbnail" style="width:49.7%">
<br>

</p>

<b>&nbsp;CloseGaps.py:</b>
<span class="pre-python">
<pre>
#For less coding to change another kind of import
from archicv.archi import *

#open an image as <"numpy.ndarray">
img = open_image( "./image_input.png" )

#set a black paper for painting results
img_black_paper = create_paper(img.shape)

#get a grayscale image
img_gray = get_gray_image(img)

#begin recognition and optimization
contours = get_contour_cornerlists( img_gray )
rectangles = [ get_rectangle(contour) for contour in contours ]
rectangles = machine_classify( rectangles )
rectangles_four_points = machine_optimize( rectangles )

#draw results image file via OpenCV
for list_of_roof in rectangles_four_points:
    cv_draw_roof( img_black_paper, list_of_roof )
save_image('image_roof_result.jpg', img_black_paper )

#generate cad results
tmp_dxf = open_dxf()
for list_of_roof in rectangles_four_points:
    dxf_draw_roof( tmp_dxf, list_of_roof )
save_dxf( tmp_dxf, 'roof_result.dxf' )
</pre>
</span>


<br><br>






<!--tree circle-->
<h2>Recognize circle tree</h2>
Recognization of circle tree.
<hr>
<p>
The api of get_circle_tree() is not mature enough. <br>
But it can works and this api is not the most important.<br>
In drawing work of landscape architect, circle tree drawing is not the toughest jobs.<br>
So it's not the best area for costing develop working.<br>
There are two kinds of algorithms to detect circle tree. One is HoughCircle algorithms, and the other is find contours and calculate to get the circle, which is used in archi.get_circle_tree().<br>

<b>left:</b> image_input.png  <br><b>right:</b> image_circle_tree_result.jpg<br>
<img src="http://www.caup.cn/static/demo-circle.jpg" class="img-thumbnail" style="width:49.7%">
<img src="http://www.caup.cn/static/result-circle.jpg"  class="img-thumbnail" style="width:49.7%">
<br>

</p>

<b>&nbsp;CloseGaps.py:</b>
<span class="pre-python">
<pre>
from archicv.archi import *

#open an image as <"numpy.ndarray">
img = open_image( "./image_input.png" )

#set a black paper for painting results
img_black_paper = create_paper(img.shape)

#get a grayscale image
img_gray = get_gray_image(img)

#begin recognition and optimization
circles = get_circle_tree( img_gray )

#draw results image file via OpenCV
cv_draw_tree( img_black_paper, circles )
save_image( 'image_circle_tree_result.jpg', img_black_paper )

#generate cad results
tmp_dxf = open_dxf()
dxf_draw_tree( tmp_dxf, circles )
save_dxf( tmp_dxf, 'circle_tree_result.dxf' )
</pre>
</span>


<br><br>





<!--revclound-->
<h2>Recognize tree revclound</h2>
Recognization of tree revclound.
<hr>
<p>
Data analysis and drawing of tree revclound are not mature enough. <br>
But it can works and this api will be updated later.<br>

<b>left:</b> image_input.png  <br><b>right:</b> image_revclound_tree_result.jpg<br>
<img src="http://www.caup.cn/static/demo-revclound.jpg" class="img-thumbnail" style="width:49.7%">
<img src="http://www.caup.cn/static/result-revclound.jpg"  class="img-thumbnail" style="width:49.7%">
<br>

</p>

<b>&nbsp;CloseGaps.py:</b>
<span class="pre-python">
<pre>
from archicv.archi import *

#open an image as <"numpy.ndarray">
img = open_image( "./image_input.png" )

#set a black paper for painting results
img_black_paper = create_paper(img.shape)

#get a grayscale image
img_gray = get_gray_image(img)

#begin recognition and optimization
contours = get_contour_cornerlists( img_gray )

#draw results image file via OpenCV
cv_draw_revclound( img_black_paper, contours )
save_image( 'image_revclound_tree_result.jpg', img_black_paper )

#generate cad results
tmp_dxf = open_dxf()
dxf_draw_tree( tmp_dxf, contours )
save_dxf( tmp_dxf, 'revclound_tree_result.dxf' )
</pre>
</span>


<br><br>



<!--lake-->
<h2>Recognize lake strandline</h2>
Recognization of lake strandline.
<hr>
<p>
Close gaps and detect the contours of lake strandlines, including island strandline in lake.<br>

<b>left:</b> image_input.png  <br><b>right:</b> image_lake_result.jpg<br>
<img src="http://www.caup.cn/static/demo-lake.jpg" class="img-thumbnail" style="width:49.7%">
<img src="http://www.caup.cn/static/result-lake.jpg"  class="img-thumbnail" style="width:49.7%">
<br>

</p>

<b>&nbsp;CloseGaps.py:</b>
<span class="pre-python">
<pre>
from archicv.archi import *

#open an image as <"numpy.ndarray">
img = open_image( "./image_input.png" )

#set a black paper for painting results
img_black_paper = create_paper(img.shape)

#get a grayscale image
img_gray = get_gray_image(img)

#begin recognition and optimization
contours = get_contour_cornerlists( img_gray )

#draw results image file via OpenCV
cv_draw_lake( img_black_paper, contours )
save_image( 'image_lake_result.jpg', img_black_paper )

#generate cad results
tmp_dxf = open_dxf()
dxf_draw_tree( tmp_dxf, contours )
save_dxf( tmp_dxf, 'lake_result.dxf' )
</pre>
</span>


<br><br>


<h2>Some Hints</h2>
Some tips for deep user. More details are in the <a href="http://www.caup.cn/reference">reference</a>.
<hr>
<p>
1. This is a simple library and it is rather recommended to master every api in reference. Different api can combine to get different performance. It is worth dive into archicv api, especially for landscape architect.<br>
2. If you are a deep enough user or a geek, it is recommended to learn opencv-python and numpy, because archicv is based on opencv and numpy. If you master opencv, you will discover archicv is just a easier library for users on the area of landscape architecture and archicv will make something easier if you are doing something about computer vision on landscape architecture. It is a short but good saber.<br>
3. Because there are just several thousand lines of codes. So it is recommended to read the codes of archi.py in order to catch insights into code structure and logic.
</p>

