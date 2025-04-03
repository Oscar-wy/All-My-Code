class Item:
    def __init__(self):
        self.Name = None
        self.description = None
    def get_name(self):
        return self.Name
    def set_name(self, item_name):
        self.Name = item_name
    def set_description(self, description):
        self.description = description
    def describe(self):
        return self.description