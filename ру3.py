class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def drive(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return f'model: {self.__model}, year: {self.__year}'

class FueCar(Car):
    def __init__(self, model, year, ful_bank):
        # super().__init__(model, year)
        # super(FueCar).__init__(model, year)
          Car.__init__(self, model, year)

some_car = Car('Audi', 2000)
print(some_car)


