import random
from animal_1 import *


class River:
    """
    Class for river representation.
    """
    def __init__(self, length):
        self.length = length
        self.river = [None for i in range(length)]
        self.animals = []

    def generate(self):
        """
        Generate fish and bears at random positions.
        """
        for i in range(self.length):
            self.river[i] = random.choice([None, Bear(i), Fish(i)])
        for i in self.river:
            if i:
                self.animals.append(i)

    def print_river(self):
        """
        Print river.
        """
        print("".join([str(i) if isinstance(i, Animal) else " " for i in self.river]))

    def next_step(self):
        """
        Change river to next step.
        """
        for i in self.animals:
            i.move()
            if i.position < 0 or i.position > self.length - 1:
                i.move_back()

        new_animals = []
        for i in range(len(self.animals) - 1):
            try:
                if self.animals[i].position == self.animals[i+1].position and\
                   self.animals[i].gender != self.animals[i+1].gender:
                    if isinstance(self.animals[i], Bear) and isinstance(self.animals[i+1], Bear):
                        self.animals[i].move_back()
                        self.animals[i+1].move_back()
                        new_animals.append(Bear(None))
                    if isinstance(self.animals[i], Fish) and isinstance(self.animals[i+1], Fish):
                        self.animals[i].move_back()
                        self.animals[i+1].move_back()
                        new_animals.append(Fish(None))
                    else:
                        if isinstance(self.animals[i], Fish):
                            self.animals[i] = 0
                        elif isinstance(self.animals[i+1], Fish):
                            self.animals[i+1] = 0
                elif self.animals[i].position == self.animals[i+1].position and\
                     self.animals[i].gender == self.animals[i+1].gender and\
                     type(self.animals[i]) == type(self.animals[i+1]):
                    if self.animals[i].strength > self.animals[i+1].strength:
                        self.animals[i+1] = 0
                    else:
                        self.animals[i] = 0
            except AttributeError:
                pass
        while 0 in self.animals:
            self.animals.remove(0)

        river_new = [None for i in range(self.length)]
        for i in self.animals:
            try:
                river_new[i.position] = i
            except IndexError:
                i.position = i.old_position
                river_new[i.position] = i
            except TypeError:
                pass

        empty_indexes = []
        for i in range(len(river_new)):
            if not river_new[i]:
                empty_indexes.append(i)
        for i in new_animals:
            try:
                random.shuffle(empty_indexes)
                i.position = empty_indexes[-1]
                i.old_position = empty_indexes[-1]
                river_new[empty_indexes[-1]] = i
                empty_indexes.pop()
            except IndexError:
                pass

        self.river = river_new
        self.animals.clear()
        for i in self.river:
            if i:
                self.animals.append(i)

    def amount(self, animal):
        """
        :return: amount of certain animals in river.
        """
        count = 0
        if animal == "Bear":
            for i in self.animals:
                if isinstance(i, Bear):
                    count += 1
        elif animal == "Fish":
            for i in self.animals:
                if isinstance(i, Fish):
                    count += 1
        return count


if __name__ == "__main__":
    river = River(10)
    river.generate()
    river.print_river()
    for i in range(10):
        river.next_step()
        river.print_river()
