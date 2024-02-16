class Car:
    total_count = 0
    def __init__(self, model) -> None:
        self.__model = model

    @property
    def model(self):
        return self.__model

    @staticmethod
    def get_model():
        return "This is static method from Car class"
    
my_car = Car("Toyata")
print(my_car.get_model())
print(my_car.model)