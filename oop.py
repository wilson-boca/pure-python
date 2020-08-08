# self means create an instance od the class
class Person(object):

    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print('My name is {}'.format(self.name))


class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print('... and My super hero name is {}'.format(self.hero_name))


p = Person('Pessoa nome')
p2 = Person('Pessoa nome 2')

p2.reveal_identity()
p.reveal_identity()

sh = SuperHero('Wade Wilson', 'DeadPool')
sh.reveal_identity()
