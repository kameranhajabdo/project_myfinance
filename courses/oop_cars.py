class Car:
    def __init__(self, model: str, brand: str, price: int):
        self.model = model
        self.brand = brand
        self.price = price

vw = Car("golf", "volkswagen", 30000)

class Volkswagen(Car):
    def __init__(self,model: str, price: int):
        super().__init__(model, "volkswagen",price)

class VolkswagenGolf(Volkswagen):
    def __init__(self):
        super().__init__("golf", 30000)

vw2 = VolkswagenGolf()
print(vw2.__dict__)