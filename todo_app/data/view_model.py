from todo_app.data.item import Item

class ViewModel:
    def __init__(self, items: list[Item]):
        self._items = items
 
    @property
    def items(self):
        return self._items