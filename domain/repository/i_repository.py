from domain.entity.note import Note
from typing import List


class iRepository:
    def create(self, note: Note):
        pass

    def read(self, id: int | None = None) -> List[Note]:
        pass

    def update(self, note: Note):
        pass

    def delete(self, id: int):
        pass