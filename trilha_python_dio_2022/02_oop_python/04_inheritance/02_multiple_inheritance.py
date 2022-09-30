class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"


class Mammal(Animal):
    def __init__(self, fur_color, **kw):
        #cor do pelo
        self.fur_color = fur_color
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, color_beak, **kw):
        self.color_beak = color_beak
        super().__init__(**kw)


class Cat(Mammal):
    pass


class Ornithorhynchus(Mammal, Ave):
    def __init__(self, color_beak, fur_color, num_legs):
        super().__init__(fur_color=fur_color, color_beak=color_beak, num_legs=num_legs)

print("")
cat = Cat(num_legs=4, fur_color="black")
print(f"Cat description: Fur color = {cat.fur_color}, Number of legs = {cat.num_legs}.")

print("")
ornithorhynchus = Ornithorhynchus(color_beak="orange", fur_color="red", num_legs=2)
print(f"Ornithorhynchus description: Beak color = {ornithorhynchus.color_beak}, Fur color = {ornithorhynchus.fur_color}, Number of legs = {ornithorhynchus.num_legs}.")
