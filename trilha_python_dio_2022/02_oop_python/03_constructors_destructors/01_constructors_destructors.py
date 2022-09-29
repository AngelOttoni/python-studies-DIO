class Dog:
    def __init__(self, name, color, awake=True):
        print("Initializing the class...");
        self.name = name;
        self.color = color;
        self.awake = awake;

    def __del__(self):
        print("Removing the class instance.");
#latir
    def bark(self):
        print("auau");


def create_dog():
    dog1 = Dog("Zeus", "White and black", False);
    print(dog1.name);


dog1 = Dog("Chappie", "yellow");
dog1.bark();

print("Hello World!");

del dog1;

print("Hello World!");
print("Hello World!");
print("Hello World!");

create_dog();
