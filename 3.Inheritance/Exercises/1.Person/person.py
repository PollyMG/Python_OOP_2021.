class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Peter", 25)


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)
