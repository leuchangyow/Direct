from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.title('DIRECT Project')

'History'
st.write('The goal of this project is to develop a software to help new comer students to get familiar in specific microscope, including TEM, SEM and AFM etc. A common question for new comers is how to judge the quality of images. In this case, the software is developed to distinguish whether the image is noisy, well-exposed or suffer from unsharpness or blur with the function of image optimization. After the judgement from the software is been made, students decide whether spending time to optimize the image or not. Image restoration, such as denoting and inpainting, is included to optimize the picture in this software. Depending on the quality of the image, the restoration time varies. Receiving the final image, students are able to get the ideal images for their research.')

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric('Team Member', 'Kim')
col2.metric('Team Member', 'William')
col3.metric('Team Member', 'Nick')
col4.metric('Team Member', 'Hsuan-Yu')
col5.metric('Team Member', 'Lilo')

st.title('How this project works?')

'Upload your TEM photo to check'

data = st.file_uploader('Upload your TEM experiment photo')





with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
