import numpy as np
import cv2
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
# load model đã train
model = load_model('C:/Users/Admin/PycharmProjects/untitled/phanloaiphuongtien/code/mymodel.phanloaigiaothong')

# đưa ảnh test vào + xử lí ảnh
img = cv2.imread('7.jpg')
img = cv2.resize(src=img, dsize=(150, 150))
img = np.reshape(img, [1, 150, 150, 3])

# dự toán class từ ảnh đưa vào
classes = model.predict_classes(img)


label = dict(enumerate(open('label.txt')))
print(label)
print(classes)
print(label[int(classes)])