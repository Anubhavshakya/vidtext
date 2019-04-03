from image_utils import ImageText
import random
import string
import cv2,glob,tempfile,shutil
import numpy as np
import os
from .directory import TempDir
from .text import Text
def TextToVideo(sourceData):
	i = 'A'
	color = 'white'
	font = "calibri.ttf"
	backcolor = ['#210f05','#444441','#16082d','#3d091f','#420000','#012824','#332401','#250130','#011d30']
	li = Text(sourceData)
	secure_random = random.SystemRandom()
	dir_path = TempDir()
	img_array = []
	for text in range(len(li)):
		img = ImageText((800, 600), background=secure_random.choice(backcolor))
		img.write_text_box((50, 150), li[text], box_width=700, font_filename=font,font_size=30, color=color, place='justify')
		img.save(dir_path+i+'.png')
		i = ''.join(random.choices(string.ascii_uppercase + string.digits))
	for filename in glob.glob(dir_path+'*.png'):
	    img = cv2.imread(filename)
	    height, width, layers = img.shape
	    size = (width,height)
	    img_array.append(img)
	out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 3, size)
	for i in range(len(img_array)):
	    out.write(img_array[i])
	out.release()
	shutil.rmtree(dir_path, ignore_errors=True)