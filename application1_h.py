class Car:
    """Designing the Car class"""

    def __init__(self,modelname,year,price):
        self.modelname = modelname #attribue -->class attributes -->can be used globally inside the class
        self.year = year
        self.price = price


    def drive(self):
        print(f"I am driving , {self.modelname}")

honda = Car('city',2009,1200000)
honda.cc = 1500  #instance objects/ object attributes  --->these are local to the particular object.
#print(honda.modelname)
#print(honda.year)
#print(honda.price)
#print(honda.cc)

#Usage of name funcion in python

print(honda.__dict__)
