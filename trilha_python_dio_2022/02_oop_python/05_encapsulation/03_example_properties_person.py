# class Person:
#     def __init__(self, name, birth_date):
#         self.name = name
#         self._birth_date = birth_date
    
    

#     @property
#     def age(self):
#         _current_year = 2022
#         return _current_year - self._birth_date


# person1 = Person("Anna", 1994)
# print(f"Name: {person1.name} \tAge: {person1.age}")


class Person:
    def __init__(self, first_name, middle_name, last_name, year_birth):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self._year_birth = year_birth
    
    @property
    def full_Name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
        
    @property
    def age(self):
        _current_year = 2022
        return _current_year - self._year_birth


person1 = Person("Anna", "Lima", "Costa", 1994)
print(f"Full Name: {person1.full_Name} \tAge: {person1.age}")

person2 = Person("Angelo", "Lima", "Costa", 1994)
print(f"Full Name: {person2.full_Name} \tAge: {person2.age}")