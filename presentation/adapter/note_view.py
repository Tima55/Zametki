from domain.entity.note import Note


def view_note(note: Note):
    print(f'id: {note.id} Title: {note.title} Body: {note.body} Date: {note.date}')