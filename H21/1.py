class Kaarten:
    def __init__(self, value, sort):
        self.value = value
        self.sort = sort
    def __repr__(self):
        return "{} {}".format(self.value, self.sort)
    def __eq__(self, other):
        return self.value == other.value

k1 = Kaarten("aas", "Harten")
k2 = Kaarten("aas", "Schoppen")
print(k1)
print(k2)
print(k1 == k2)