# 아래에 코드를 작성하시오.
class Animal :
    def __init__(self, name, sound="hi") :
        self.name = name
        self.sound = sound
    def speak(self) :
        print(self.sound)

    
class Dog(Animal) : 
    def __init__(self, name, sound= "Woof!") :
        super().__init__(name, sound )
    def speak(self):
        super().speak()

class Cat(Animal) : 
    def __init__(self, name, sound= "Meow!") :
        super().__init__(name, sound )
    def speak(self):
        super().speak()

class Flyer() : 
    def __init__(self, name, fl= "Flying") :
        self.name = name
        self.fl = fl
    def fly(self):
        print(self.fl)

class Swimmer() : 
    def __init__(self, name, swi = "Swimming") :
        self.name = name
        self.swi  = swi
    def swim (self):
        print(self.swi )

class Duck(Animal, Flyer, Swimmer) : 
    def __init__(self, name, sound= "Quack!") :
        super().__init__(name, sound )
    def speak(self):
        super().speak()

def make_animal_speak(type) :
    ani = type("name")
    if type == Flyer :
        ani.fly()
    elif type == Swimmer :
        ani.swim()
    else :
        ani.speak()

make_animal_speak(Dog)
make_animal_speak(Cat)
make_animal_speak(Duck)
make_animal_speak(Flyer)
make_animal_speak(Swimmer)


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# class Flyer:
#     def fly(self):
#         return "Flying"

# class Swimmer:
#     def swim(self):
#         return "Swimming"

# class Duck(Animal, Flyer, Swimmer):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         return "Quack!"

# def make_animal_speak(animal):
#     print(animal.speak())

# # Test cases
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# duck = Duck("Daffy")

# make_animal_speak(dog)  # Output: Woof!
# make_animal_speak(cat)  # Output: Meow!
# make_animal_speak(duck)  # Output: Quack!

# print(duck.fly())  # Output: Flying
# print(duck.swim())  # Output: Swimming
