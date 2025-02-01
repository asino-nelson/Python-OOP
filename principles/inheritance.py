# Inheritance


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

mercedes = Car("Mercedes C200", 2023, "V6", 4)
mercedes.start()
print(f"Model:{mercedes.model}, Year:{mercedes.year}, Engine:{mercedes.engine}, Capacity:{mercedes.capacity}-Setaer")
mercedes.stop()
print("")
kawasaki = Bike("Kawasaki Demon", 2024, "V2 Twin-Turbo", 1000)
kawasaki.start()
print(f"Model:{kawasaki.model}, Year:{kawasaki.year}, Engine:{kawasaki.engine}, CC:{kawasaki.cc}CC")
kawasaki.stop()

print("")

print(mercedes.__dict__)
print(kawasaki.__dict__)

