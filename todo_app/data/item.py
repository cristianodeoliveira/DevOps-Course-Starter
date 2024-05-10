class Item:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status
        
    #def __init__(self, id, name, status='Doing'):
    #    self.id = id
    #    self.name = name
    #    self.status = status
        
    #def __init__(self, id, name, status='Done'):
    #    self.id = id
    #    self.name = name
    #    self.status = status
        
    @classmethod
    def from_trello_card (cls, card, list):
        return Item(card['id'],card['name'],list['name'])