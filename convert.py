
from rembg import remove
from PIL import Image
import os
import cv2

original = 'fotos_original/'
saida = 'fotos_sem_fundo/'

lista = os.listdir('fotos_original')
# print(lista)
for arquivo in lista:
    arquivo_de_entrada = original+arquivo
    arquivo_de_saida = saida+arquivo
    print(arquivo_de_entrada)
    print(arquivo_de_saida)
    pause = input('Pressione qualquer tecla para continuar')
    # remover fundo da imagem
    result = remove(arquivo_de_entrada)

    # converter a imagem para RGB
    # result = result.convert("RGB")
    # Salvar a imagem sem fundo
    # result.save(arquivo_de_saida)
