import random


class Animal:
    """
    Class for animal representation.
    """
    def __init__(self, position):
        self.position = position
        self.old_position = position

    def move(self):
        """
        Move animal randomly to the left, to the right or keep it at old position.
        """
        rand = random.randint(0, 2)
        if rand == 0:
            pass
        elif rand == 1:
            self.old_position = self.position
            self.position += 1
        elif rand == 2:
            self.old_position = self.position
            self.position -= 1

    def move_back(self):
        """
        Move animal to its old position.
        """
        self.position = self.old_position

    def __str__(self):
        return self.__class__.__name__[0]


class Bear(Animal):
    """
    Class for bear representation.
    """
    pass


class Fish(Animal):
    """
    Class for fish representation.
    """
    pass
