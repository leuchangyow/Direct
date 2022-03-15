#model import 
import math
import pandas as pd
import streamlit as st
import PIL
import time
import importlib 
import matplotlib.pyplot as plt
from REIP.image_processing.remove_cs import convert_to_dfimage, adjust_gray_value, show_edited_image, from3d_array_image, convert_to_RGB3darray
=======
#from REIP.image_processing.remove_cs import convert_to_dfimage, adjust_gray_value, show_edited_image
#from streamlit_cropper import st_cropper

from streamlit_drawable_canvas import st_canvas
from REIP.prediction.Prediction import prediction
import os

from REIP.image_processing.restore_blur import img_processing, edsr, espcn, fsrcnn, lapsrn, uint_to_float, enhance_details, restore_again, blur_function_selection
#parameter settting
blur_method = ['img_processing', 'enhance_details', 'edsr', 'espcn', 'fsrcnn', 'lapsrn']
blur_list = pd.DataFrame(blur_method)
##########
=======


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
ex_surface_charge = PIL.Image.open('./doc/images/498.tif')
sc.image(ex_surface_charge)

blur.subheader('Blur Charge Example')
ex_blur = PIL.Image.open('./doc/images/1386.tif')
blur.image(ex_blur)

temp='./temp/'

input_data = st.file_uploader('Upload your TEM experiment photo',type=['png','tif','jpg','jpg','tiff'])
realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
gray_level = st.sidebar.slider('Surface charge remove level', -20, 30, 9)

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join(temp,uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1    
    except:
        return 0



if input_data is not None:
    if save_uploaded_file(input_data): 
        display_image = Image.open(input_data)
        st.image(display_image)
        prediction = prediction(os.path.join(temp,input_data.name))
        st.write(prediction[0])
        st.image(prediction[1])
        os.remove(temp+input_data.name)
    else:
        st.write('saving image failed')


if input_data is not None:
    if save_uploaded_file(input_data): 
        display_image = Image.open(input_data)
        st.image(display_image)
        prediction = prediction(os.path.join(temp,input_data.name))
        st.header(prediction[0])
        os.remove(temp+input_data.name)
    else:
        st.write('saving image failed')
    if prediction[0] == 'It is predicted to be surface charge.':
        
        st.subheader('Select the surface area')
        canvas_result = st_canvas(height = 300, width = 300, fill_color = 0 , 
                                      drawing_mode = 'rect', 
                                      stroke_width = 3, 
                                      background_image = from3d_array_image(prediction[1]))
        if canvas_result.json_data is None:
            st.stop()
        if canvas_result.json_data is not None:
            
            objects = pd.json_normalize(canvas_result.json_data["objects"])
            for col in objects.select_dtypes(include = ['object']).columns:
                objects[col] = objects[col].astype('str')
            df_image = convert_to_dfimage(from3d_array_image(prediction[1]))
            
            start_point = [objects['left'][0],objects['top'][0]] 
            end_point = [objects['left'][0]+objects['width'][0], objects['top'][0]+objects['height'][0]]
            df_copied = adjust_gray_value(df_image, start_point, end_point, level = gray_level)
            after_sc_image = show_edited_image(df_copied)
            RGBarray = convert_to_RGB3darray(after_sc_image)
            st.subheader('After surface charge restoration')
            st.image(after_sc_image)
            'type of restore_aga'
            Answer= st.radio('Further improve blur?', options=['Remian','Restore Blur'], index=0)
            if Answer == 'Restore Blur':
                methods= st.selectbox('Choose blur restoration method', options=blur_list, index=0)
                if methods == 'Click here select method':
                    pass
                else:
                    ml = eval(methods)
                    result_array = ml((RGBarray
                                      ))
                    result_array_copied = result_array.copy()
                    st.image(PIL.Image.fromarray(result_array_copied))
            elif Answer == 'Remain':
                pass
            
            
    elif prediction[0] == 'It is predicted to be blur.':
        st.text('Here is the list of feature in image proessing')
        st.table(blur_list)
        
        methods= st.selectbox('Choose the 1st restoration method', options=blur_list, index=0)
        ml = eval(methods)
        result_img = ml((prediction[1]))
        st.image(result_img)
        Answer= st.selectbox('Would you want to restore again', options=['Default','Yes','No'], index=0)
        if Answer == 'Yes':
            methods2= st.selectbox('Choose the restoration method', options=blur_list, index=0)
            ml2 = eval(methods2)
            result_2img = ml((result_img))
            st.image(result_2img)
            st.header('you are all set!')
        elif Answer == 'No':
            pass
    elif prediction[0] == 'It is predicted to be clear.':
        pass
#st.header('Congrats! Perfect image!')
#st.balloons()
    
    
#realtime_update = st.sidebar.checkbox(label = 'update in real time', value = True)

    


    
    
