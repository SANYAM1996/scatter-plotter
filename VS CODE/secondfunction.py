# write a function to check whether the number is odd or not
def evenOdd(x):
    if x%2 == 0:
        print('the number is even')
    else:
        print('the number is odd')
evenOdd(2)
evenOdd(3)

def print_models(unprinted_designs,completed_designs):
    '''simulate printing each design, untill none are left.
    move each design to completed_models after printing'''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # simulate creating a 3d print from the design
        print('printing model: ' + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    '''show all the modals that were printed.'''
    print('\n the following models have beeen printed:')
    for completed_models in completed_models:
        print(completed_models)
unprinted_designs = ['iphone case','robot pendant','dodcahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


# the car class
class car():
    '''a simple attempt to represent the car'''
    def __init__(self,make,model,year):
        '''initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
    # lets add an another attribute here
        self.odometer_reading = 0
    def get_descriptive_name(self):
        '''return a neatly formatted descriptive name.'''
        long_name = str(self.year)+' '+self.make+ ' '+self.model
        return long_name.title()
    # here i added new method of car
    def read_odometer(self):
        '''print a statement showing the car mileage.'''
        print('this car has ' + str(self.odometer_reading)+' mileage on it')
my_new_car = car('audi','a4','2006')
print(my_new_car.get_descriptive_name())
# calling the method
my_new_car.read_odometer()

# modifying the attribute values in object
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# add another class the__init__()method for a child class
class ElectricCar(car):
    '''represent aspect of a car,specific to electric vehicles'''
    def __init__(self,make,model,year):
        '''initialize attribute of the parent class.'''
        super().__init__(make,model,year)
        # adding the battery attribute
        self.battery_size = 70
    def describe_battery(self):
        '''print a statement describing the battery size.'''
        print('this car has a '+ str(self.battery_size)+ '-kwh battery.')
my_tesla = ElectricCar('tesla','s type','2016')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()



