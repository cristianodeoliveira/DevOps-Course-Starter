from todo_app.data.item import Item

class ViewModel:
    def __init__(self, items: list[Item]):
        self._items = items
 
    @property
    def todo_items(self) -> list[Item]:
        output = []
        
        for item in self._items:
            if item["status"] == "To Do":
                output.append(item)
        print ("Todo items",output)        
        return output
    
    @property
    def doing_items(self) -> list[Item]:
        output = []
        for item in self._items:
            if item["status"] == "Doing":
                output.append(item)
        print ("Doing items",output)  
        return output

    @property
    def done_items(self) -> list[Item]:
        output = []
        for item in self._items:
            if item["status"] == "Done":
                output.append(item)
        print ("Done items",output)  
        return output