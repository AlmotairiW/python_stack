class Vehicle:
    def __init__(self,speed,color,model,capacity,cost,availabile=True):
        self.speed=speed
        self.color=color
        self.model=model
        self.capacity=capacity
        self.cost=cost
        self.availabile = availabile

    def print_info(self):
        print(f"speed: {self.speed}, color: {self.color}, model :{self.model}, capacity: {self.capacity}. Cost: {self.cost}")
        return self
    
    def calc_pric(self,no_of_days):
        if(no_of_days>5):
            return self.cost*no_of_days*0.9
        else:
            return self.cost*no_of_days

    def update_cost(self, prec_change, is_increased):
        if is_increased:
            self.cost += (self.cost * prec_change)
        else:
            self.cost -= (self.cost * prec_change)

class bus(Vehicle):
    def __init__(self,speed,color,model,capacity, cost, availabile,length):
        super().__init__(speed,color,model,capacity,cost, availabile )
        self.length=length
    def calc_pric(self,no_of_days):
        if no_of_days>10:
            return self.cost*no_of_days*0.85
        elif no_of_days>5:
            return self.cost*no_of_days*0.90
        else:
            return self.cost*no_of_days

    
    
class Car(Vehicle):
    def __init__(self,speed,color,model,capacity, cost, availabile):
        super().__init__(speed,color,model,capacity,cost, availabile)

class CarRental:
    def __init__(self, stock = []):
        self.stock = stock
        
    def addCar( self, newCar):
        self.stock.append(newCar)
        return self

    def removeCar (self, idx):
        self.stock.pop(idx)
        return self

    def displyStock(self):
        print(f"we have currently the following  available for rent\n")
        for car in self.stock:
            if(car.availabile != False):
                car.print_info()
        return self

    def rentCar(self):
        print(f"Please choose Number of the car you want to rent:\n")

        for i in range(len(self.stock)):
            print(f"{i + 1}: ")
            self.stock[i].print_info()
        carIdx = int(input())
        if(self.stock[carIdx - 1].availabile == True):
            print(f"Please enter number of days:\n")
            numberOfDays = int(input())
            cost = self.stock[carIdx - 1].calc_pric(numberOfDays)
            self.stock[carIdx - 1].availabile = False

            print(f"you have rented the following car for {numberOfDays} days:")
            self.stock[carIdx - 1].print_info()
            print(f" Cost: ", cost)
        else:
            print(f"Car is not available\n")
        return self
    
    def returnCar(self, idx):
        print("the following car has been reterned by customer: ")
        self.stock[idx].print_info()
        self.stock[idx].availabile = True
        return self
    def update_cost(self, prec_change, is_increased):
        for car in self.stock:
            car.update_cost(prec_change, is_increased)
        return self




car1 = bus(200,'red','2001',15, 150, True, '20')
car2 = Car(340,'black', '2017',4, 100,True)
car3 = Car(350,'White', 'some',5, 200,True)
car4 = bus(190,'Yellow','x',15, 150, True, '15')
car5 = bus(190,'Yellow','x',15, 150, True, '15')


rental1 = CarRental()
rental1.addCar(car1)
rental1.addCar(car2)
rental1.addCar(car3)
rental1.addCar(car4) 
rental1.addCar(car5)


print('------------------------')
rental1.displyStock()
print('------------------------')



print('------------------------')
rental1.rentCar()
print('------------------------')
rental1.displyStock()
print('------------------------')
rental1.rentCar()
print('------------------------')
rental1.displyStock()
print('------------------------')
rental1.returnCar(1)
print('------------------------')

rental1.displyStock()
print('------------------------')

rental1.update_cost(0.1, True)
print('------------------------')
rental1.displyStock()
print('------------------------')
rental1.update_cost(0.1, False)
print('------------------------')
rental1.displyStock()
print('------------------------')