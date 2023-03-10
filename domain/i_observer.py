from domain.entity.note import Note
from typing import List


class iObserver:
    def on_next(self, notes: List[Note]):
        pass