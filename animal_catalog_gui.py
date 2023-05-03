import PySimpleGUI as sg
from animal_catalog import *


# window = sg.Window('Animal Catalog')

NAME_SIZE = 30

def name(name):
    dots = NAME_SIZE-len(name)-2
    return sg.Text(name + ' ' + ' '*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

layout_main = [
    [name("Insert animal Name/Species:"), sg.Input("")],
    [name("Insert animal Class:"), sg.Input("")],
    [name("Insert animal Order:"), sg.Input("")],
    [name("Insert animal Family:"), sg.Input("")],
    [name("Insert animal Genus:"), sg.Input("")],
    [sg.Button('Approve'), sg.Button('Add new animal'), sg.Button('View animal list')]
]

layout_animal_list = [
    
]

window = sg.Window('Animal catalog', layout_main, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True)

while True:
    event, values = window.read()
    # sg.Print(event, values)
    if event == sg.Button('View animal list'):
        make_window
        break

window.close()
# sg.Button('Remove animal')