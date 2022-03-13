import pandas as pd
import numpy as np
from numpy import asarray
from matplotlib import image
import matplotlib.pyplot as plt
import PIL

def convert_to_dfimage(image):
    converted = image.convert('L')
    image_nparray = asarray(converted)
    df = pd.DataFrame(image_nparray)
    return df

def adjust_gray_value(df, start_point, end_point, level = 4):
    """
    adjust_gray_value(df, start_point, end_point, level = 4)
    df = the image dataframe
    start point / end point = a list indicates the x, y
    level ( default = 4 ) the count adjust the gray level
    """
    df_copied = df.copy()
    df_copied.iloc[start_point[0]:end_point[0], start_point[1]:end_point[1]] = df.iloc[start_point[0]:end_point[0], start_point[1]:end_point[1]]+ level
    return df_copied
def show_edited_image(df_copied):
    edited_image = PIL.Image.fromarray(df_copied.values)
    return edited_image