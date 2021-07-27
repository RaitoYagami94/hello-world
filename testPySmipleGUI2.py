from tkinter.constants import X
import PySimpleGUI as sg
import os
import pandas
import csv
import matplotlib.pyplot as plt






layout = [  [sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Get filename example', layout)

event, values = window.read()
window.close()

url = values[0].replace("/", "\\")



x = []
y = []

with open(url, "r") as csv_file:
    plots = csv.reader(csv_file, delimiter = ",")

    for row in plots:
        x.append(row[1])
        y.append(int(row[2]))

#matplotlib
plt.bar(x, y, color = 'b', width = 0.72, label = "Age") #Màu cột, chiều rộng cột và tên chú thích cột
plt.xlabel('Names')# tên thanh x
plt.ylabel('Ages')# tên thanh y
plt.title('Ages of different persons') #tên bảng
plt.legend()# cái này em không rõ
plt.show()# show bảng

df = pandas.read_csv(url)
print(df)


