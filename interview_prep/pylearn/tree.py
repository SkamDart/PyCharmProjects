
class Node:
    def __init__(self, val, next):
        self._next = next
        self._val = val


    @property
    def next(self):
        return self._next

    @property
    def val(self):
        return self._val