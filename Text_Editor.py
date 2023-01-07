import PySimpleGUI as sg

smileys = [
    'happy',[':)','XD',':D','<3'],
    'sad',[':(','T_T'],
    'other',[':3']
]
smiley_events = smileys[1] + smileys[3] + smileys[5]

menu_layout = [
    ['File', ['Open','Save','---','Exit']],
    ['Tools', ['Word Count']],
    ['Add', smileys]
]

sg.theme('GrayGrayGray')
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key = '-DOCNAME-')],
    [sg.Multiline(no_scrollbar=True, size = (40,30), key = '-TEXTBOX-')]
]

window = sg.Window('Text Editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Word Count':
        full_text = values['-TEXTBOX-']
        clean_text = full_text.replace('\n', ' ').split(' ')
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        sg.popup(f'words {word_count}\ncharacters: {char_count}')

    if event in smiley_events:
        current_text = values['-TEXTBOX-']
        new_text = current_text + ' ' + event
        window['-TEXTBOX-'].update(new_text)

window.close()