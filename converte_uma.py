
from rembg import remove
from PIL import Image
import os
import cv2


# Caminho da Imagem
input_path = '1.jpg'
# Caminho para salvar a imagem sem fundo
output_path = '2.jpg'
# Abrir a imagem no Python
input = Image.open(input_path)


# remover fundo da imagem
result = remove(input)
# converter a imagem para RGB
result = result.convert("RGB")
# Salvar a imagem sem fundo
result.save('2.jpg')
# salvar a imagem sem fundo jpg


# Salvar a imagem
# output.save(output_path)
