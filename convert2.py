
from os.path import splitext
from os import listdir
from rembg import remove
from PIL import Image
import os
import cv2

original = 'fotos_original/'
saida = 'fotos_sem_fundo/'


diretorio_origem = 'fotos_original'
diretorio_destino = 'fotos_sem_fundo'

for arquivo in listdir(diretorio_origem):
    nome_arquivo, extensao_arquivo = splitext(arquivo)
    if extensao_arquivo == '.jpg':
        print('Convertendo arquivo: {}'.format(arquivo))
        input_path = diretorio_origem + '/' + arquivo
        output_path = diretorio_destino + '/' + nome_arquivo + '.jpg'
        input = Image.open(input_path)
        result = remove(input)
        result = result.convert("RGB")
        result.save(output_path)
