#! .Python3-env/bin/python

#Program Libraries
import cv2
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont #dynamic import
from os import listdir
from os.path import isfile, join
from skimage.morphology import disk

#Structure for saved files in paste
PathTypeApp = ("Erode","Dilate","Opening","Closing")
PathFileImagens = ("BW","Gray")

nameBW = [f for f in listdir("Original/PB") if isfile(join("Original/PB", f))]
nameGray = [f for f in listdir("Original/Cinza") if isfile(join("Original/Cinza", f))]

#Criation directories of the imagens output
os.makedirs("Output/", exist_ok=True)
for i in range(len(PathTypeApp)):
    for j in range(len(PathFileImagens)):
        for k in range(len(nameBW)):
            os.makedirs("Output/"+ PathTypeApp[i] + "/" + PathFileImagens[j] + "/" + str(k+1), exist_ok=True)

##kernel
kernel = ([[cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)),cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)),cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))],
            [np.ones((1, 3), dtype=np.uint8),np.ones((1, 5), dtype=np.uint8),np.ones((1, 7),  dtype=np.uint8)],
            [disk(3/2),disk(5/2),disk(7/2)]]) 


def apErosion(imagem, kernel, local, id, idK):
    cv2.imwrite("Output/Erode/" + local + "/"+ str(id+1) + "/img"+ str(id+1) + "Kernel"+ str(idK) + ".png", cv2.erode(imagem,kernel,iterations = 1))

def apDilate(imagem, kernel, local, id, idK):
    cv2.imwrite("Output/Dilate/" + local + "/"+ str(id+1) + "/img"+ str(id+1) + "Kernel"+ str(idK) + ".png", cv2.dilate(imagem,kernel,iterations = 1))

def apOpening(imagem, kernel, local, id, idK):
    cv2.imwrite("Output/Opening/" + local + "/"+ str(id+1) + "/img"+ str(id+1) + "Kernel"+ str(idK) + ".png", cv2.morphologyEx(imagem, cv2.MORPH_OPEN, kernel))

def apClosing(imagem, kernel, local, id, idK):
    cv2.imwrite("Output/Closing/" + local + "/"+ str(id+1) + "/img"+ str(id+1) + "Kernel"+ str(idK) + ".png", cv2.morphologyEx(imagem, cv2.MORPH_CLOSE, kernel))

for i in range(len(nameBW)):
    for j in range(3):
        for k in range(3):
            apErosion(cv2.cvtColor(cv2.imread("Original/PB/" + str(nameBW[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[0],i, str(j+1) + str(k+1))
            apErosion(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[1],i, str(j+1) + str(k+1))

            apDilate(cv2.cvtColor(cv2.imread("Original/PB/" + str(nameBW[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[0],i, str(j+1) + str(k+1))
            apDilate(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[1],i, str(j+1) + str(k+1))

            apOpening(cv2.cvtColor(cv2.imread("Original/PB/" + str(nameBW[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[0],i, str(j+1) + str(k+1))
            apOpening(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[1],i, str(j+1) + str(k+1))

            apClosing(cv2.cvtColor(cv2.imread("Original/PB/" + str(nameBW[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[0],i, str(j+1) + str(k+1))
            apClosing(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[1],i, str(j+1) + str(k+1))