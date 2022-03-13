#Import packages
import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras

#Identify the model path
model_dir = 'model/' 


#load in model and weight 
weightfile = model_dir+'REIP.10-0.8500.hdf5' #reading the model you trained above
model = keras.models.load_model(model_dir+'REIP.h5') #load the basemodel, 
model.load_weights(weightfile) #add the weight file that just trained to the basemodel 
#create a model to predict the feature space. 



def prediction(image_folder_path): # ex : '/gdrive/My Drive/REIP/imagedata/clear/27.tif')
    '''This prediction function take input picture file and return the predicted class'''
    reip_dict = {0:'clear', 1:'blur', 2:'surface_charge'}             # label dict
    rd_image = cv2.cvtColor(cv2.imread(image_folder_path), cv2.COLOR_BGR2RGB)     # read image
    cropre_pic = np.expand_dims(cv2.resize(rd_image[0:890, :],(300,300)),axis=0)    # crop and resize
    predict = reip_dict.get(np.argmax(model(cropre_pic)[0]))            # predict and get classes
    pre_string = f'It is predicted to be {predict}.'
    return pre_string