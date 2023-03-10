from domain.entity.note import Note
from typing import List
from presentation.adapter.note_view import view_note


def submit_list(notes: List[Note]):
    if len(notes) > 0:
        for note in notes:
            view_note(note)
    else:
        print('Empty list of notes...')