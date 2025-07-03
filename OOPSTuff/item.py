import random

class Item():

    def __init__(self, name, desc, attv):
        self.item_name = name
        self.description = desc
        self._attack_value = attv     # An attribute that is "private"
        # You can call the methods of a class inside that class, like this

    # This method begins with an underscore _ because it is not meant to be called
    # outside of the class itself. This notation means 'private' in Python, although
    # there is nothing to actually stop you from calling it from outside
    def _generate_random_item(self):
        names = ["Axe", "Bow", "Feather duster"]
        descriptions = ["A sharp chopping tool", "Fires arrows", "A tickly stick"]
        attack_values = [40, 30, 5]
        self.item_name = random.choice(names)
        self.description = descriptions[names.index(self.item_name)]
        self._attack_value = attack_values[names.index(self.item_name)]

    # You can change the representation of the object as a string
    # so that it prints out something customised
    def __str__(self):
        return "Holding [" + self.item_name + "] - " + self.description + ". Attack value: " + str(self._attack_value)

    # Getters and setters
    def get_attack_value(self):
        return self._attack_value

    def set_attack_value(self, new_value):
        self._attack_value = new_value

    # Other methods
    def describe(self):
        print(self.item_name + " - " + self.description)


    # FOR INFORMATION
    # This is the more Pythonic way of creating getters and setters. The getter is
    # a method labelled as a property, and then the setter is a method with the SAME NAME which is
    # labelled as the setter for that property. Then, depending on context, you can refer to
    # Object.attack_value as either the setter or getter

    # CAUTION - you can't call the property method the same thing as one of the attributes!
    # The attribute is called _attack_value because it's meant to be private
    # and the method here is called attack_value
    """
    @property
    def attack_value(self):
        return self._attack_value

    @attack_value.setter
    def attack_value(self, new_value):
        self._attack_value = new_value
    """
