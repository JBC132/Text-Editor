import PySimpleGUI as sg

smileys = []

menu_layout = [
    ['File', ['Open','Save','---','Exit']],
    ['Tools', ['Word Count']],
    ['Add', smileys]
]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key = '-DOCNAME-')],
    [sg.Multiline()]
]

window = sg.Window('Text Editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()