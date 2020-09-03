
class Expense():
    """ Class expense """
    def __init__(self, name, cost):
        """ Init function """
        self._name = name

        if cost < 0: # Cost cannot be negative
            raise ValueError("Cost cannot be negative")
        self._cost = cost

    def __str__(self):
        """ Printing functionality """
        return f"{self.name} - {self.cost}"

    @property
    def name(self):
        """ Name getter """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def cost(self):
        """ Cost getter """
        return self._cost

    @cost.setter
    def cost(self, cost):
        if cost < 0: # Cost cannot be negative
            raise ValueError("Cost cannot be negative")

        self._cost = cost
