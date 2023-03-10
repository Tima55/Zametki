import json
from domain.entity.note import Note
from domain.repository.i_repository import iRepository
from data.note_mapper import NoteMapper, note_from_json
from typing import List
import datetime


class Repository(iRepository):
    def __init__(self, filename: str):
        self.filename: str = filename
        self.notes: dict[int, Note] = dict()
        self.__load()

    def __load(self):
        with open(self.filename, 'r') as f:
            notes_list = [note_from_json(note) for note in json.load(f)]
            self.notes = dict((note.id, note) for note in notes_list)

    def __save(self):
        with open(self.filename, 'w') as f:
            json.dump(list(self.notes.values()), f,  indent=4, cls=NoteMapper)

    def create(self, note: Note):
        if len(list(self.notes.keys())) > 0:
            note.id = max(list(self.notes.keys())) + 1
        else:
            note.id = 1
        note.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.notes[note.id] = note
        self.__save()

    def read(self, id: int | None = None) -> List[Note]:
        if id is None:
            return list(self.notes.values())
        elif id in self.notes.keys():
            return [self.notes[id]]
        else:
            return []

    def update(self, note: Note):
        note.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.notes[note.id] = note
        self.__save()

    def delete(self, id: int):
        if id in self.notes:
            del self.notes[id]
            self.__save()