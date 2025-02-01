# Polymorphism

# Poly - many
# Morph - forms

class Vehicle:
    def __init__(self, model, year, engine):
        self.model = model
        self.year = year
        self.engine = engine

    #START
    def start(self):
        print("Starting...")
    #STOP
    def stop(self):
        print("Stoping...")

class Car(Vehicle):
    def __init__(self, model, year, engine, capacity):
        super().__init__(model, year, engine)
        self.capacity = capacity

class Bike(Vehicle):
    def __init__(self, model, year, engine, cc):
        super().__init__(model, year,engine)
        self.cc = cc

vehicles: list[Vehicle] = [
    Car("Mercedes C200", 2023, "V6", 4),
    Bike("Kawasaki Demon", 2024, "V2 Twin-Turbo", 1000)
]

for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()

