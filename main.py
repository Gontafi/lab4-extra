from models import *

person = Person(age=18, full_name='Alibek')
driver = Driver(experience=5, age=25, full_name='John Doe')
engine = Engine(power=250, company='Mercedes')
car = Car(carClass='B', driver=driver, engine=engine, marka='Mercedes')
lorry = Lorry(carClass='D',
              engine=Engine(power=800, company='Kamaz'),
              driver=Driver(age=35, full_name='Tolebekov Dauren', experience=8),
              marka='Kamaz',
              carrying=1500)
sport_car = SportCar(carClass='B',
                     engine=Engine(power=980, company='Nissan'),
                     driver=Driver(age=36, full_name='Scorr Pruett',experience=10),
                     marka='BMW',
                     speed=450.5)

print(f'Person: {person}')
print(f'driver: {driver}')
print(f'engine: {engine}')
print(f'car info: {car}')
print(f'lorry info: {lorry}')
print(f'sport car info: {sport_car}')
