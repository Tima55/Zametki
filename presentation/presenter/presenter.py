from presentation.view.i_view import iView
from domain.entity.note import Note
from domain.i_observer import iObserver
from domain.interactor.interactor import Interactor
from typing import List


class Presenter(iObserver):

    def __init__(self, interactor: Interactor, view: iView):
        self.interactor: Interactor = interactor
        self.view: iView = view

    def on_attach(self, view: iView):
        self.interactor.subscribe(self)

    def on_detach(self):
        self.interactor.unsubscribe(self)

    def on_next(self, notes: List[Note]):
        self.view.show_notes(notes)

    def get_note(self, id: int) -> Note:
        return self.interactor.get_note(id=id)

    def add_note(self, note: Note):
        self.interactor.create(note)

    def edit_note(self, note: Note):
        self.interactor.update(note)

    def delete_note(self, id: int):
        self.interactor.delete(id)