from presentation.view.i_view import iView
from domain.entity.note import Note
from typing import List
from presentation.presenter.presenter import Presenter
from di.module import provide_presenter
from presentation.adapter.notes_adapter import submit_list
from presentation.adapter.note_view import view_note


class MainView(iView):

    def __init__(self):
        self.presenter: Presenter = provide_presenter(view=self)
        self.presenter.on_attach(view=self)

    def show_controls(self):
        print('1 for add')
        print('2 edit edit')
        print('3 for delete')
        print('4 for exit')
        action = input('prompt an action ')
        if action == '1':
            self.on_add()
        elif action == '2':
            self.on_edit()
        elif action == '3':
            self.on_delete()
        elif action == '4':
            self.on_close()
        else:
            self.show_controls()

    def show_notes(self, notes: List[Note]):
        submit_list(notes)
        self.show_controls()

    def on_add(self):
        title = input('new note title: ')
        body = input('new note body: ')
        new_note = Note(id="", title=title, body=body, date="")
        self.presenter.add_note(new_note)

    def on_edit(self):
        id = int(input('specify id of a note to edit: '))
        note = self.presenter.get_note(id)
        print('editing this note: ')
        view_note(note)
        note.title = input('new title: ')
        note.body = input('new body: ')
        self.presenter.edit_note(note)

    def on_delete(self):
        id = input('specify id of a note to delete: ')
        self.presenter.delete_note(int(id))

    def on_close(self):
        self.presenter.on_detach()