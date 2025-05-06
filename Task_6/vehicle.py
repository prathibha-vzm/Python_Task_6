#Question 3
from abc import ABC,abstractmethod
#Base Class
class Vehicle(ABC):
    #Constructor with two arguments empty name and rental rate as 0
    def __init__(self,model="",rental_rate=0):
        self.model=model
        self.rental_rate=rental_rate

    #An abstract method , no implementation here
    @abstractmethod
    def calculate_rental(self):
        pass #not using

#Subclass with parent class Vehicle
class Car(Vehicle):
    def __init__(self,model):
        super().__init__(model)

        self.model=model
        self.rental_rate = 0

    #to get the model name
    def get_model(self):
        return self.model

    #to set the modified rental rate
    def set_rental_rate(self,rate):
        self.rental_rate=rate

    # Method Over-riding
    def calculate_rental(self):
        #Getting Rental hour
        print("Enter Rental hour")
        rental_hour=int(input())

        #Checking the condition according to the input and calculating the rental rate
        if self.get_model()=="Luxury":
            self.set_rental_rate(5000*rental_hour)

        elif self.get_model()=="SUV":
            self.set_rental_rate(500*rental_hour)

        elif self.get_model()=="Economy":
            self.set_rental_rate(50*rental_hour)

        print(f"{self.get_model()}:{rental_hour}hr--${self.rental_rate}")

#Subclass with parent class Vehicle
class Bike(Vehicle):
    def __init__(self,model):
        super().__init__(model)

        self.model = model
        self.rental_rate=0

    def get_model(self):
        return self.model

    def set_rental_rate(self,rate):
        self.rental_rate=rate

    def calculate_rental(self):
        # Getting Rental Days
        print("Number of Rental Days")
        rental_day = int(input())

        # Checking the condition according to the input and calculating the rental rate
        if self.get_model()=="Electric":
            self.set_rental_rate(500*rental_day)

        elif self.get_model()=="Scooter":
            self.set_rental_rate(250*rental_day)

        elif self.get_model()=="Hybrid":
            self.set_rental_rate(450*rental_day)

        print(f"{self.get_model()}-{rental_day}days--${self.rental_rate}")

#Subclass with parent class Vehicle
class Truck(Vehicle):
    def __init__(self,model):
        super().__init__(model)

        self.model = model
        self.rental_rate=0

    def get_model(self):
        return self.model

    def set_rental_rate(self,rate):
        self.rental_rate=rate

    def calculate_rental(self):
        # Getting Kilometers travelled
        print("Number of Kilometers")
        rental_km = int(input())

        # Checking the condition according to the input and calculating the rental rate
        if self.get_model()=="Closed_Van":
            self.set_rental_rate(40 * rental_km)

        elif self.get_model()=="Open_Truck":
            self.set_rental_rate(35 * rental_km)

        elif self.get_model()=="6_Wheeler":
            self.set_rental_rate(30 * rental_km)

        print(f"{self.get_model()}-{rental_km}km--${self.rental_rate}")


#Asking to choose the vehicle type
print("Guvi Rental\nChoose the type of Vehicle\n1. Car\n2. Bike\n3. Truck")
vehicle_option=int(input())

#Creating object for the subclasses and Calling the method according to the input
if vehicle_option==1:
    #getting the input out of the class and sending the model name as argument
    model_name=input("Choose the Model\nLuxury\nSUV\nEconomy: ")
    car_object = Car(model_name)
    car_object.calculate_rental()

elif vehicle_option==2:
    model_name = input("Choose the Model\nElectric\nScooter\nHybrid: ")
    bike_object = Bike(model_name)
    bike_object.calculate_rental()

elif vehicle_option==3:
    model_name = input("Choose the Model\nClosed_Van\nOpen_Truck\n6_Wheeler: ")
    truck_object = Truck(model_name)
    truck_object.calculate_rental()

else:
    print("Enter Valid option")
