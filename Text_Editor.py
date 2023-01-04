import PySimpleGUI as sg

smileys = [
    'happy',[':)','XD',':D','<3'],
    'sad',[':(','T_T'],
    'other',[':3']
]

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

    if event == 'Word Count':
        print('test')
window.close()