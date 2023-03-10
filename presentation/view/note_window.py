import PySimpleGUI as sg
from domain.entity.note import Note
import datetime


def note_window(note: Note) -> Note | None:

    layout = [[sg.Text('Enter a title and body for the note:')],
              [sg.InputText(key='title', default_text=note.title)],
              [sg.Multiline(key='body', default_text=note.body)],
              [sg.Button('Save'), sg.Button('Cancel')]]

    window = sg.Window('Note window', layout)

    event, values = window.read()
    window.close()

    if event == 'Save':
        note.title = values['title']
        note.body = values['body']
        note.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return note
    else:
        return None