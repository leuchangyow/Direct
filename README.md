# Project REIP

 _"REIP: Resolution Enhancement Image Project"_
 A package to classify damaged SEM images and do image restoration.
 
## Project Objective

The goal of this project is to develop a software to help new comer students to get familiar in SEM. A common question for new comers is how to judge the quality of images. In this case, the software is developed to distinguish whether the image is noisy, well-exposed or suffer from unsharpness or blur with the function of image optimization. After the judgement from the software is been made, students decide whether spending time to optimize the image or not. Image restoration packages, such as pillow and open.cv, is included to optimize the picture in this software. Depending on the quality of the image, the restoration time varies. Receiving the final image, students are able to get the ideal images for their research.

## Requirements:
Package REIP has following main dependencies:
1. Python = 3.7
2. opencv
3. Tensorflow = 2.7

## Installation:
1. In your terminal, run <code>git clone https://github.com/leuchangyow/REIP.git</code>
2. Install and activate the environment with REIP.yml
3. Change the directory to REIP root directory, by running <code>cd REIP</code> 
4. Run <code>python setup.py install</code>
5. To check installation run, <code>python -c "import REIP"</code> in your terminal


## Usage:

REIP uses Convolutional Neural Network (CNN) for train the prediction model. Later on, we used packages of OpenCV and Pillow to restore the damaged or imperfect images. The flow of information is shown in image below:
<p align="center"><img src="doc/images/workflow.jpg" width=700 alt="information flow of how the package works"/></p>


## Use Cases:
* Upload the image you want to check the quality of

* Classigy microscopic images into groups of clear, blur, surface charged

* Repair the imperfect images by their groups:
1. Repair the blurred images by an automated function
2. Repair the images with surface charge by a manual which requires you to frame the location of surface charge


## Streamlit:
Follow the below steps to run streamlit.app:
1. Make sure you've download the streamlit package
2. In your terminal, run <code>streamlit run streamlit.app</code>

In streamlit:
1. Use "Browse files" to upload the image you want to use, and the classification result will automatically show up
2. Due to the classification result, the corresponding restoration method will show up
3. For the surface charge restoration method, you first frame the surface charge area, then use the bar on the left hand side to adjust the brightness.After the surface charge restoration, you can also proceed the blurred image restoration
4. For the blurred image restoration, there are 6 kinds of methods you can choose, which are img_processing', 'enhance_details', 'edsr', 'espcn', 'fsrcnn' and 'lapscn' (see <a href=https://github.com/leuchangyow/REIP/blob/main/doc/method_description.ipynb>method description</a>) . You can choose each of them to repair the blurred image. SeeMoreover, you can also do another method after your first one is completed.


## Acknowledgment:
We would like to acknowledge the SEM images support from National Tsing Hua university (NTHU) Energy & Optoelectronic Materials Lab
