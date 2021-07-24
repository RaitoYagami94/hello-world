import PySimpleGUI as sg
import os


layout = [  [sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Get filename example', layout)

event, values = window.read()
window.close()

url = values[0].replace("/", "\\")

print(url)

f = open(url, "r")

print("noi dung:" +f.read())
f.close()


