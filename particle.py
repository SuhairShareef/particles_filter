from turtle import pos


class Particle:
    def __init__(self, weight, position=0) -> None:
        self.weight = weight
        self.position = position

    def __lt__(self, other):
        # p1 < p2 calls p1.__lt__(p2)
        return self.weight < other.weight
    
    def __eq__(self, other):
        # p1 == p2 calls p1.__eq__(p2)
        return self.weight == other.weight
    
    def __le__(self, other):
        return self.weight <= other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight
    
    def __repr__(self) -> str:
        return '(weight: ' + str(self.weight) + ', postion: ' + str(self.position) + ')\n'