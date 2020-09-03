
class Expense():
    """ Class expense """
    def __init__(self, name, cost):
        """ Init function """
        self.name = name
        self.cost = cost

    def __str__(self):
        """ Printing functionality """
        return f"{self.name} - {self.cost}"

    @property
    def name(self):
        """ Name getter """
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def cost(self):
        """ Cost getter """
        return self.cost

    @cost.setter
    def cost(self, cost):
        if cost < 0: # Cost cannot be negative
            raise ValueError("Cost cannot be negative")

        self.cost = cost
