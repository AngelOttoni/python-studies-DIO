class Bike:
    def __init__(self, color, model, year, value, rim=18):
        #Attributes
        #self = this, mas por convensão é self
        #o self é a ref para o object, em Py é uma ref explicíta
        self.color = color;
        self.model = model;
        self.year = year;
        self.value = value;
        #aro
        self.rim = rim;
        
    #methods are functions within classes
    #Buzinar
    def honk(self):
        print("Plim plim...");
    
    def stop(self):
        print("Stopping bicycle...");
        print("Bicycle stopped!");
        
    def run(self):
        print("Vrummmmmm...");
        
    # def __str__(self):
    #     return f"Bicycle description\nColor: {bike2.color}, Model: {bike2.model}, Year: {bike2.year}, Price: R${bike2.value:.2f}.";
    #or
    #Forma automatizada
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}";
        
        
#Instantiating a class              
# bike1 = Bike("red", "caloi", 2022, 900);
# bike1.honk();
# bike1.run();
# bike1.stop();
# print(f"Bicycle description\nColor: {bike1.color}, Model: {bike1.model}, Year: {bike1.year}, Price: R${bike1.value:.2f}.");

bike2 = Bike("green", "monark", 2000, 600);
bike2.honk(); #This is the same as Bike.honk(bike2);
print(f"Bicycle description\nColor: {bike2.color}, Model: {bike2.model}, Year: {bike2.year}, Price: R${bike2.value:.2f}.");
# print(bike2);
