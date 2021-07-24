# img_viewer.py
import PySimpleGUI as sg
import os.path
# window layout of two column
file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(20, 1), enable_events=True, key="-Folder-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(60, 40),
            key="-File list-"
        )
    ],
]
# show the file chosen
image_viewer_column = [
    [sg.Text("Choose an image from the list on the left :")],
    [sg.Text(size=(40, 1), key="-Tout-")],
    [sg.Image(key="-image-")],
]
# full layout
layout=[
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]
window = sg.Window("Image Viewer", layout)
# event loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WINDOW_CLOSED:
        break
    if event == "-Folder-":
        folder = values["-Folder-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
        ]
        window["-File list-"].update(fnames)
    elif event == "-File list-":
        try:
            filename = os.path.join(values["-Folder-"], values["-File list-"][0])
            window["-Tout-"].update(filename)
            window["-image-"].update(filename=filename)
        except:
            pass
window.close()



