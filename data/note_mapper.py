import json
from domain.entity.note import Note


class NoteMapper(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Note):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


def note_from_json(obj):
        return Note(id=obj['id'], title=obj['title'], body=obj['body'], date=obj['date'])