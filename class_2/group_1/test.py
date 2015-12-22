class Population(object):
    POPULATION = 0

    def __init__(self):
        self.__class__.POPULATION += 1
        print(self)

    @classmethod
    def increment_population(cls):
        cls.POPULATION += 1

    @classmethod
    def population_count(cls):
        return cls.POPULATION


class Animal(object):

    def __init__(self, name):
        self.name = name
        super(Animal, self).__init__()
        print(super())


class Duck(Animal, Population):
    pass


class Rabbit(Animal, Population):
    pass


donald = Duck("Donald")
Duck("Duffy")
Duck("Lucas")

bugs = Rabbit("Bugs")


print(Duck.population_count())
print(Rabbit.population_count())

print(bugs.name)
print(donald.name)