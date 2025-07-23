class Car:
    def __init__(self, model, color, year, transmission, electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric

    def print_cars(self):
        print(f"Car model = {self.model}")
        print(f"Color = {self.color}")
        print(f"Year = {self.year}")
        print(f"Transmission = {self.transmission}")
        print(f"Electric = {self.electric}")


class Ford(Car):
    pass

class BMW(Car):
    pass

class Tesla(Car):
    pass


# Create objects
bmw1 = BMW("x6", "Silver", 2018, "Auto", False)
tesla1 = Tesla("S", "Beige", 2017, "Auto", True)
ford1 = Ford("Focus", "White", 2020, "Auto", False)

# Test printing
ford1.print_cars()
