#! .Python3-env/bin/python

#Program Libraries
import cv2
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont #dynamic import
from os import listdir
from os.path import isfile, join
from skimage.morphology import disk
from matplotlib import pyplot as plt

#Structure for saved files in paste
PathTypeApp = ("Erode","Dilate","Opening","Closing")
PathFileImagens = ("BW","Gray")

nameBW = [f for f in listdir("Original/PB") if isfile(join("Original/PB", f))]
nameGray = [f for f in listdir("Original/Cinza") if isfile(join("Original/Cinza", f))]

#Criation directories of the imagens output
os.makedirs("Output/", exist_ok=True)
os.makedirs("Output/Hist-Input/BW", exist_ok=True)
os.makedirs("Output/Hist-Input/Gray", exist_ok=True)

for i in range(len(PathTypeApp)):
    for j in range(len(PathFileImagens)):
        for k in range(len(nameGray)):
            if((j == 0) and (k == 3)): 
                continue;
            else:
                os.makedirs("Output/"+ PathTypeApp[i] + "/" + PathFileImagens[j] + "/" + str(k+1), exist_ok=True)

##kernel
kernel = ([[cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)),cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)),cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))],
            [np.ones((1, 3), dtype=np.uint8),np.ones((1, 5), dtype=np.uint8),np.ones((1, 7),  dtype=np.uint8)],
            [disk(int(3/2)),disk(int(5/2)),disk(int(7/2))]]) 


def apErosion(imagem, kernel, local, id, idK):
    
    imagEroTemp = cv2.erode(imagem,kernel,iterations = 1)

    pathWrite = "Output/Erode/" + local + "/"+ str(id+1) + "/img"+ str(id+1) + "Kernel"+ str(idK) 
    
    cv2.imwrite(pathWrite + ".png", imagEroTemp)
    
    plt.cla()
    
    plt.clf()

    plt.hist(imagEroTemp.ravel(),256,[0,256], fc='k', ec='k')
    
    plt.xlabel('Intensidade', fontsize=18)

    plt.ylabel('Quantidade de pixel', fontsize=16)

    plt.savefig(pathWrite + "-H.png")

def apDilate(imagem, kernel, local, id, idK):

    imagEroTemp = cv2.dilate(imagem,kernel,iterations = 1)

    pathWrite = "Output/Dilate/" + local + "/"+ str(id+1) + "/img"+ str(id+1) + "Kernel"+ str(idK) 

    cv2.imwrite(pathWrite + ".png", imagEroTemp)
     
    plt.cla()
    
    plt.clf()

    plt.hist(imagEroTemp.ravel(),256,[0,256], fc='k', ec='k')
    
    plt.xlabel('Intensidade', fontsize=18)

    plt.ylabel('Quantidade de pixel', fontsize=16)

    plt.savefig(pathWrite + "-H.png")

def apOpening(imagem, kernel, local, id, idK):
    
    imagEroTemp = cv2.morphologyEx(imagem, cv2.MORPH_OPEN, kernel)

    pathWrite = "Output/Opening/" + local + "/"+ str(id+1) + "/img"+ str(id+1) + "Kernel"+ str(idK)

    cv2.imwrite(pathWrite + ".png", imagEroTemp)
    
    plt.cla()
    
    plt.clf()

    plt.hist(imagEroTemp.ravel(),256,[0,256], fc='k', ec='k')
    
    plt.xlabel('Intensidade', fontsize=18)

    plt.ylabel('Quantidade de pixel', fontsize=16)

    plt.savefig(pathWrite + "-H.png")

def apClosing(imagem, kernel, local, id, idK):

    imagEroTemp = cv2.morphologyEx(imagem, cv2.MORPH_CLOSE, kernel)
    
    pathWrite = "Output/Closing/" + local + "/"+ str(id+1) + "/img"+ str(id+1) + "Kernel"+ str(idK) 

    cv2.imwrite(pathWrite + ".png", imagEroTemp)
    
    plt.cla()
    
    plt.clf()

    plt.hist(imagEroTemp.ravel(),256,[0,256], fc='k', ec='k')
    
    plt.xlabel('Intensidade', fontsize=18)

    plt.ylabel('Quantidade de pixel', fontsize=16)

    plt.savefig(pathWrite + "-H.png")

for i in range(len(nameGray)):
   
    if(i==3):
        

        plt.cla()
        
        plt.clf()

        plt.hist(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY).ravel(),256,[0,256], fc='k', ec='k')
    
        plt.xlabel('Intensidade', fontsize=18)

        plt.ylabel('Quantidade de pixel', fontsize=16)

        plt.savefig("Output/Hist-Input/Gray/" + str(nameGray[i]) + "-H.png")


    else:
        
        plt.cla()
        
        plt.clf()
        
        plt.hist(cv2.cvtColor(cv2.imread("Original/PB/" + str(nameBW[i])), cv2.COLOR_BGR2GRAY).ravel(),256,[0,256], fc='k', ec='k')
        
        plt.xlabel('Intensidade', fontsize=18)

        plt.ylabel('Quantidade de pixel', fontsize=16)

        plt.savefig("Output/Hist-Input/BW/" + str(nameBW[i]) + "-H.png")

        plt.cla()
        
        plt.clf()

        plt.hist(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY).ravel(),256,[0,256], fc='k', ec='k')
    
        plt.xlabel('Intensidade', fontsize=18)

        plt.ylabel('Quantidade de pixel', fontsize=16)

        plt.savefig("Output/Hist-Input/Gray/" + str(nameGray[i]) + "-H.png")

    for j in range(3):
        for k in range(3):
            if(i==3):
                
                apErosion(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[1],i, str(j+1) + str(k+1))

                apDilate(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[1],i, str(j+1) + str(k+1))

                apOpening(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[1],i, str(j+1) + str(k+1))

                apClosing(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[1],i, str(j+1) + str(k+1))

            else:                
                apErosion(cv2.cvtColor(cv2.imread("Original/PB/" + str(nameBW[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[0],i, str(j+1) + str(k+1))
                apErosion(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[1],i, str(j+1) + str(k+1))

                apDilate(cv2.cvtColor(cv2.imread("Original/PB/" + str(nameBW[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[0],i, str(j+1) + str(k+1))
                apDilate(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[1],i, str(j+1) + str(k+1))

                apOpening(cv2.cvtColor(cv2.imread("Original/PB/" + str(nameBW[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[0],i, str(j+1) + str(k+1))
                apOpening(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[1],i, str(j+1) + str(k+1))

                apClosing(cv2.cvtColor(cv2.imread("Original/PB/" + str(nameBW[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[0],i, str(j+1) + str(k+1))
                apClosing(cv2.cvtColor(cv2.imread("Original/Cinza/" + str(nameGray[i])), cv2.COLOR_BGR2GRAY),kernel[j][k], PathFileImagens[1],i, str(j+1) + str(k+1))