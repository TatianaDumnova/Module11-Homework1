 # Библиотека pillow.
 # Используя  простой синтаксис можно выполнять различные задачи
 # по автоматической обработке цифровых изображений.

from PIL import Image

image = Image.open('flower.jpg')

image.show() #выводит изображение

with Image.open("flower.jpg") as im:# поворачивает на 45 градусов
    im.rotate(45).show()

new_image = image.resize((200, 385))# Изменяет размер
new_image.show()

new_image2 = image.transpose(Image.FLIP_TOP_BOTTOM)# Перевернет вверх ногами
new_image2.show()

gray_img = image.convert("L") #Сделает серым
gray_img.show()

# Библиотека numpy ускоряет и упрощает работу с массивами данных.

import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a) #Выведет массив
print(a.size) #Выведет количество элементов
print(a + 3) # Прибавит 3 к каждому элементу
print(a * 3) # Умножит каждый элемент на 3
print(a ** 3) # 3 степень каждого элемента

# Библиотека reguests помогает быстро взаимодействовать с серверами,
# используя простой синтаксис.

import requests

response = requests.get('https://lenta.ru')
print(response.text)