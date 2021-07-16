class MenuItem(object):
    def __init__(self,n,c,r):
        self.name = n
        self.cost = c
        self.rating = r

    def __eq__(self, other):
        if self.name==other.name and self.cost==other.cost and self.rating==other.rating:
            return True
        else:
            return False

    def __str__(self):
        return "Item: " + self.name + ", Cost: " + str(self.cost) + ", Rating: " + '{0:.6f}'.format(self.rating)

    def __hash__(self):
        return hash(self.rating)

    def __lt__(self, other):
        if hash(self)<hash(other):
            return True
        else:
            return False

    def __repr__(self):
        return str(self)
