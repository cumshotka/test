class Cart:

    def __init__(self):
        self.a = []

    def add(self, obj):

        self.a.append(obj)

    def remove(self, indx):
        self.a.remove(indx)

    def get_list(self):
        print([f'{i.name}: {i.cost}' for i in self.a])


class Stol:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Styl:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Divan:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


cart = Cart()
stol = Stol('styl', 30)
cart.add(stol)
styl = Styl('lystra', 40)
cart.add(styl)
cart.get_list()