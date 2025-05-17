from abc import ABCMeta, abstractmethod


class Pet(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name
        self.isHealthy = True
        self.isHungry = False
        self.isHappy = True
        

    @abstractmethod
    def accept(self, visitor):
        pass
    #def treat(self):
        #pass
    def __str__(self):
        return f"Dein Tier Heißt {self.name}"
    

     

class Cat(Pet):
    def accept(self, visitor):
        visitor.visit(self)
    def feed(self):
        self.isHungry = False
    def play(self):
        self.isHungry = True
        self.isHappy = True

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.skills = 1
        self.isHappy = True
    def accept(self, visitor):
        visitor.visit(self)
    def getBone(self):
        self.isHungry = False
    def training(self):
        self.isHappy = False
        self.skills += 1
    def walk(self):
        self.isHappy = True
        self.isHungry = True


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, pet):
        pass

#class Veterinarian(Visitor):
   # def visit(self, pet):
        #pet.treat()

class Master(Visitor):
    def visit(self, pet):
        if isinstance(pet, Cat):
            pet.feed()
        elif isinstance(pet, Dog):
            pet.getBone()

class Trainer(Visitor):
    def visit(self, pet):
        if isinstance(pet, Dog):
            pet.training()
        else:
            pass

class Child(Visitor):
    def visit(self, pet):
        if isinstance(pet, Dog):
            pet.walk()
        elif isinstance(pet, Cat):
            pet.play()






cat = Cat('Marj')
dog = Dog('Rex')
visitors = [Master(), Child(), Trainer()]
for pet in [cat, dog]:
    print(pet)
    for visitor in visitors:
        visitor.visit(pet)
        print(f"Deint Tier ist \'happy = {pet.isHappy} and hungry = {pet.isHungry}\'")