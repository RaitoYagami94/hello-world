import numpy as np
import cv2
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
# load model đã train
model = load_model('C:/Users/Admin/PycharmProjects/untitled/phanloaiphuongtien/code/mymodel.phanloaigiaothong')

# đưa ảnh test vào + xử lí ảnh
img = cv2.imread('0081.jpg')
img = cv2.resize(src=img, dsize=(150, 150))
img = np.reshape(img, [1, 150, 150, 3])

#plt.imshow(img)
#plt.show()

#X= image.img_to_array(img)
#X= np.expand_dims(X,axis=0)
#images = np.vstack([X])

# dự toán class từ ảnh đưa vào
classes = model.predict_classes(img)

#trả về tên class từ giá trị class
i = 0
for things in classes:
    if (things == 0):
        print('%d.Airplane' % (i))
    else:
        i  = i + 1
        if (things == 1):
            print('%d.Bike' % (i))
        else:
            i = i + 1
            if (things == 2):
                print('%d.Bus' % (i))
            else:
                i = i +1
                if (things == 3):
                    print('%d.Car' % (i))
                else:
                    i = i + 1
                    if (things == 4):
                        print('%d.Cargo' % (i))
                    else:
                        i = i + 1
                        if (things == 5):
                            print('%d.Container' % (i))
                        else:
                            i = i + 1
                            if (things == 6):
                                print('%d.Cyclo' % (i))
                            else:
                                i = i + 1
                                if (things == 7):
                                    print('%d.Car' % (i))
                                else:
                                    i = i + 1
                                    if (things == 8):
                                        print('%d.Motorbike' % (i))
                                    else:
                                        i = i + 1
                                        if (things == 9):
                                            print('%d.Airplane' % (i))
                                        else:
                                            i = i + 1
                                            if (things == 10):
                                                print('%d.Truck' % (i))
                                            else:
                                                i = i + 1

