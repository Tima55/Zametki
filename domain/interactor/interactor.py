from domain.entity.note import Note
from domain.repository.i_repository import iRepository
from domain.i_observer import iObserver
from typing import List


class Interactor:

    def __init__(self, repository: iRepository):
        self.repository: iRepository = repository
        self.observers: List[iObserver] = []

    def subscribe(self, observer: iObserver):
        self.observers.append(observer)
        observer.on_next(self.repository.read())

    def unsubscribe(self, observer: iObserver):
        self.observers.remove(observer)

    def get_note(self, id: int) -> Note:
        return self.repository.read(id=id)[0]

    def create(self, note: Note):
        self.repository.create(note)
        self.__emit()

    def update(self, note: Note):
        self.repository.update(note)
        self.__emit()

    def delete(self, id: int):
        self.repository.delete(id)
        self.__emit()

    def __emit(self):
        notes = self.repository.read()
        for observer in self.observers:
            observer.on_next(notes)