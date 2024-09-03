class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
        print(f"make: {self.make}, model: {self.model}, year: {self.year}")    

car=Car("Mercedes-Benz","SUV",2024)
car.display_info()
    