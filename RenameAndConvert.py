"""
Created on Wed Jan 08 23:15:50 2019

@author: Renan Alboy
"""

# Parte do código para tratamento de imagens. Realiza o seguinte processo:
# -> Altera o nome da imagem para uma das opções do vetor 'name' 
# -> Altera a imagem para .pgn e salva a imagem   

import os
import cv2 

i=1
n = 1
arq = 'RenameAndConvert.py'
name = ['armario', 'cadeira', 'escada', 'geladeira', 'gaveta_aberta', 'gaveta_fechada', 'mesa', 'fogao', 'porta_aberta', 'porta_fechada']

for j in os.listdir('.'):
    
    if j != arq:
        j = cv2.imread(j)
        new = j[:-4]
        new = name[0]
        num = str(n) 
        cv2.imwrite(new + num + '.' + 'png', j )
        n = n + 1

print ('Process has end.')

