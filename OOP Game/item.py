class Item:
    def __init__(self, itemName, itemDesc):
        self.Name = None
        self.description = None
    def get_name(self):
        return self.Name
    def describe(self):
        return self.description
    
class Chest(Item):
    def __init__(self, itemName, itemDesc):
        super().__init__(itemName, itemDesc)
        self.Items = {}
    def open(self):
        pass
    def setItem(self, item):
        self.Items[item.Name] = item