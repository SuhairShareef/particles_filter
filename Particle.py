class Particle:
    """A class that represents a particle object used for the particles filter """

    def __init__(self, weight, position=0, direction='f') -> None:
        """This is the constructor

        Args:
            weight (float): weight of the particle
            position (int): the position of the particle
            direction (str): the direction of the particle, can be 'f' --> forward
                             or 'b' --> backward. Defaults to 'f'
        """
        self.weight = weight
        self.position = position
        self.direction = direction

    def move(self, steps, start, end):
        """ this method moves the particle one step in its derection. If it hits 
            the end or the start of the path, it returns and moves in the other direction

        Args:
            steps (integer): number of steps the particle takes
            start (integer): the start of the path the particle is moving in
            end (integer): the end of the path the particle is moving in
        """

        if self.direction == 'f':
            if self.position + steps >= end:       # change direction
                self.direction = 'b'
                self.move(steps, start, end)
            else:
                self.position += steps

        else:
            if self.position - steps <= start:       # change direction
                self.direction = 'f'
                self.move(steps, start, end)
            else:
                self.position -= steps

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
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
