import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython import display
import time

#%matplotlib inline

PATH = "C:\\Users\\hongq\\OneDrive\\Pictures\\flower.jpg"

for i in range(1,4):
    p = PATH.format(i)
    #print p
    image = mpimg.imread(p) # images are color images
    plt.gca().clear()
    plt.imshow(image);
    display.display(plt.gcf())
    display.clear_output(wait=True)
    time.sleep(1.0) # wait one second

# READ IMAGE from path (window)
import PySimpleGUI as sg
settings = sg.UserSettings()
layout = [[sg.Text('Enter a filename:')],
          [sg.Input(settings.get('-filename-', ''), key='-IN-'), sg.FileBrowse()],
          [sg.B('Save'), sg.B('Exit', key='Exit')]]
window = sg.Window('Filename Example', layout)
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event == 'Save':
        settings['-filename-'] = values['-IN-']

window.close()
