
class Expense():
    def __init__(self, name, cost, _type):
        """ Init function """
        self.name = name
        self.cost = cost
        self.type = _type

    def __str__(self):
        return f"{self.name};{self.cost};{self.type}"
