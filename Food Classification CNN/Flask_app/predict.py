import pickle 
import numpy as np
from keras.models import model_from_json
import keras
import cv2
import matplotlib.pyplot as plt
import os
from random import shuffle # mixing up or currently ordered data that might lead our network astray in training.
from tqdm import tqdm

def predict(arg):
	
	json_file = open('model.json','r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	# load weights into new model
	loaded_model.load_weights("CNNModelIndian.h5")
	print("Loaded model from disk")

	img = cv2.imread('static/images/'+ arg , cv2.IMREAD_GRAYSCALE) # change image name and predictions can be seen for individual images
	img_size = 280

	img_gray = cv2.resize(img,(img_size,img_size))
	data = img_gray.reshape(1,img_size,img_size,1)

	model_out=loaded_model.predict(data)


	if np.argmax(model_out) == 0: str_label='Samosa'
	elif np.argmax(model_out) == 1: str_label='Kachori'
	elif np.argmax(model_out) == 2: str_label='Aloo paratha'
	elif np.argmax(model_out) == 3: str_label='Idli'
	elif np.argmax(model_out) == 4: str_label='Jalebi'
	elif np.argmax(model_out) == 5: str_label='Tea'
	elif np.argmax(model_out) == 6: str_label='Paneer tikka'
	elif np.argmax(model_out) == 7: str_label='Dosa'
	elif np.argmax(model_out) == 8: str_label='Omlet'
	elif np.argmax(model_out) == 9: str_label='Poha'
	print(str_label)

	return str_label