class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod #decorator
    def create_of_date_of_birth(cls, year, month, day, name):
        age = 2022 - year
        return cls(name, age)

    @staticmethod #decorator
    def is_legal_age(age):
        return age >= 18


p = Person.create_of_date_of_birth(1994, 3, 21, "Guilherme")
print(p.name, p.age)

print(Person.is_legal_age(18))
print(Person.is_legal_age(8))
