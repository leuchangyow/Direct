# Project REIP

 _"REIP: Resolution Enhancement Image Project"_
 A package to classify damaged SEM images and do image restoration.
 
## Project Objective

The goal of this project is to develop a software to help new comer students to get familiar in SEM. A common question for new comers is how to judge the quality of images. In this case, the software is developed to distinguish whether the image is noisy, well-exposed or suffer from unsharpness or blur with the function of image optimization. After the judgement from the software is been made, students decide whether spending time to optimize the image or not. Image restoration packages, such as pillow and open.cv, is included to optimize the picture in this software. Depending on the quality of the image, the restoration time varies. Receiving the final image, students are able to get the ideal images for their research.

## Requirements:
Package REIP has following main dependencies:
1. Python = 3.7
2. opencv
3. Tensorflow = 2.

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
