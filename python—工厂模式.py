
class Stor(object):
    def select_car(self, car_type):
        pass
    def order(self,car_type):
        return self.select_car(car_type)

class BMWstor(Stor):
    def select_car(self, car_type):
        return BMWFactory().select_car_type(car_type)

class AODIstor(Stor):
    def select_car(self, car_type):
        return AODIFactory().select_car_type(car_type)

class BMWFactory():
    def select_car_type(self, car_type):
        if car_type =='x6':
            return X6()

class AODIFactory():
    def select_car_type(self, car_type):
        if car_type =='a6':
            return A6()

class Car(object):
    pass

class X6(Car):
    pass

class A6(Car):
    pass