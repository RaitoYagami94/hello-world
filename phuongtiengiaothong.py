import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# khai báo các hằng số
BATCH_SIZE = 32
IMG_SIZE = 250
EPOCHS = 50

#  Giảm hệ số RGB của data từ 0-255 xuống từ 0-1 để dễ xử lí
training_data = ImageDataGenerator(rescale=1./255,rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')
validation_data = ImageDataGenerator(rescale=1./255)

# đưa vào dữ liệu train
train_dir = 'C:/phân loại phương tiện giao thông/transport_split/train'
train_airplane = 'C:/phân loại phương tiện giao thông/transport_split/train/airplane'
train_bike = 'C:/phân loại phương tiện giao thông/transport_split/train/bike'
train_bus = 'C:/phân loại phương tiện giao thông/transport_split/train/bus'
train_car = 'C:/phân loại phương tiện giao thông/transport_split/train/car'
train_cargo = 'C:/phân loại phương tiện giao thông/transport_split/train/cargo'
train_container = 'C:/phân loại phương tiện giao thông/transport_split/train/container'
train_cyclo = 'C:/phân loại phương tiện giao thông/transport_split/train/cyclo'
train_excavator = 'C:/phân loại phương tiện giao thông/transport_split/train/excavator'
train_motorbike = 'C:/phân loại phương tiện giao thông/transport_split/train/motorbike'
train_sailboat = 'C:/phân loại phương tiện giao thông/transport_split/train/sailboat'
train_truck = 'C:/phân loại phương tiện giao thông/transport_split/train/truck'
num_train_airplane = len(os.listdir(train_airplane))
num_train_bike = len(os.listdir(train_bike))
num_train_bus = len(os.listdir(train_bus))
num_train_car = len(os.listdir(train_car))
num_train_cargo = len(os.listdir(train_cargo))
num_train_container = len(os.listdir(train_container))
num_train_cyclo = len(os.listdir(train_cyclo))
num_train_excavator = len(os.listdir(train_excavator))
num_train_motorbike = len(os.listdir(train_motorbike))
num_train_sailboat = len(os.listdir(train_sailboat))
num_train_truck = len(os.listdir(train_truck))
train_gen = training_data.flow_from_directory(batch_size = BATCH_SIZE, directory=train_dir, shuffle=True, target_size=(IMG_SIZE, IMG_SIZE), class_mode='binary')

# đưa vào dữ liệu val
val_dir = 'C:/phân loại phương tiện giao thông/transport_split/val'
val_airplane = 'C:/phân loại phương tiện giao thông/transport_split/val/airplane'
val_bike = 'C:/phân loại phương tiện giao thông/transport_split/val/bike'
val_bus = 'C:/phân loại phương tiện giao thông/transport_split/val/bus'
val_car = 'C:/phân loại phương tiện giao thông/transport_split/val/car'
val_cargo = 'C:/phân loại phương tiện giao thông/transport_split/val/cargo'
val_container = 'C:/phân loại phương tiện giao thông/transport_split/val/container'
val_cyclo = 'C:/phân loại phương tiện giao thông/transport_split/val/cyclo'
val_excavator = 'C:/phân loại phương tiện giao thông/transport_split/val/excavator'
val_motorbike = 'C:/phân loại phương tiện giao thông/transport_split/val/motorbike'
val_sailboat = 'C:/phân loại phương tiện giao thông/transport_split/val/sailboat'
val_truck = 'C:/phân loại phương tiện giao thông/transport_split/val/truck'
num_val_airplane = len(os.listdir(val_airplane))
num_val_bike = len(os.listdir(val_bike))
num_val_bus = len(os.listdir(val_bus))
num_val_car = len(os.listdir(val_car))
num_val_cargo = len(os.listdir(val_cargo))
num_val_container = len(os.listdir(val_container))
num_val_cyclo = len(os.listdir(val_cyclo))
num_val_excavator = len(os.listdir(val_excavator))
num_val_motorbike = len(os.listdir(val_motorbike))
num_val_sailboat = len(os.listdir(val_sailboat))
num_val_truck = len(os.listdir(val_truck))
val_gen = training_data.flow_from_directory(batch_size = BATCH_SIZE, directory=val_dir, shuffle=True, target_size=(IMG_SIZE, IMG_SIZE), class_mode='binary')

# test_dir = 'C:/phân loại phương tiện giao thông/transport_split/test'
# test_gen = training_data.flow_from_directory(batch_size = BATCH_SIZE, directory=test_dir, shuffle=True, target_size=(IMG_SIZE, IMG_SIZE), class_mode='binary')

# Tính tổng dữ liệu train và val
total_train = num_train_bus + num_train_car + num_train_airplane + num_train_bike + num_train_cargo + num_train_cyclo + num_train_excavator + num_train_motorbike + num_train_sailboat + num_train_truck
total_val = num_val_bike + num_val_cargo + num_val_car + num_val_bus + num_val_airplane + num_val_container + num_val_cyclo + num_val_excavator + num_val_motorbike + num_val_sailboat + num_val_truck


# Khởi tạo model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
   
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    # tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    # tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(256, (3,3), activation='relu'),
    # tf.keras.layers.Conv2D(256, (3,3), activation='relu'),
    # tf.keras.layers.Conv2D(256, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(512, (3,3), activation='relu'),
    # tf.keras.layers.Conv2D(512, (3,3), activation='relu'),
    # tf.keras.layers.Conv2D(512, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),


    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(11, activation='softmax')

])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
history = model.fit_generator(train_gen, steps_per_epoch=int(np.ceil(total_train / float(BATCH_SIZE))), epochs=EPOCHS, validation_data=val_gen, validation_steps=int(np.ceil(total_val / float(BATCH_SIZE))) )

# Save model đã train
model.save('mymodel.phanloaigiaothong')