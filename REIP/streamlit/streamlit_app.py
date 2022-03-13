from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import PIL
import time


st.title('DIRECT Project')

'History'
st.write('The goal of this project is to develop a software to help new comer students to get familiar in specific microscope, including TEM, SEM and AFM etc. A common question for new comers is how to judge the quality of images. In this case, the software is developed to distinguish whether the image is noisy, well-exposed or suffer from unsharpness or blur with the function of image optimization. After the judgement from the software is been made, students decide whether spending time to optimize the image or not. Image restoration, such as denoting and inpainting, is included to optimize the picture in this software. Depending on the quality of the image, the restoration time varies. Receiving the final image, students are able to get the ideal images for their research.')

col1, col2, col3 = st.columns(3)
col1.metric('Team Member', 'Kim')
col2.metric('Team Member', 'William')
col3.metric('Team Member', 'Lilo')
col4, col5 = st.columns(2)
col4.metric('Team Member', 'Hsuan-Yu')
col5.metric('Team Member', 'Nick')

st.title('How this project works?')
'We aim to help you distinguish the quality of TEM photo. Upload your photo, this website is able to distinguish the defect types and help you to fine-tune the image!'
sc, blur = st.columns(2)
sc.subheader('Surface Charge Example')
ex_surface_charge = PIL.Image.open('./498.tif')
sc.image(ex_surface_charge)

blur.subheader('Blur Charge Example')
ex_blur = PIL.Image.open('./1386.tif')
blur.image(ex_blur)


input_data = st.file_uploader('Upload your TEM experiment photo')
if input_data is not None:
    input_image = PIL.Image.open(input_data)
    st.image(input_image)
    st.write('Uploaded the photo')

    
    