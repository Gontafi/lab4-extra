from dataclasses import dataclass

@dataclass
class Person:
    age: int
    full_name: str

    def __str__(self):
        return f'Driver {self.full_name}, {self.age} age'


@dataclass
class Driver(Person):
    experience: int

    def __str__(self) -> str:
        return f'{super(Driver, self).__str__()} with experience of {self.experience} years.'


@dataclass
class Engine:
    power: int
    company: str

    def __str__(self) -> str:
        return f'{self.company} that produces this engine with {self.power} h.p.'


@dataclass
class Car:
    carClass: str
    engine: Engine
    driver: Driver
    marka: str

    def start(self) -> None:
        print(f'Driver {self.driver.full_name} turns on car.')

    def stop(self) -> None:
        print(f'Driver {self.driver.full_name} stopped car.')

    def turnRight(self) -> None:
        print(f'{self.marka} car turning right.')

    def turnLeft(self) -> None:
        print(f'{self.marka} car turning left.')

    def __str__(self) -> str:
        return f'This car has class {self.carClass} with marka {self.marka} has owner {self.driver} With engine {self.engine}'


@dataclass
class Lorry(Car):
    carrying: int

    def __str__(self) -> str:
        return f'{super(Lorry, self).__str__()} with max carrying {self.carrying}kg.'


@dataclass
class SportCar(Car):
    speed: float

    def __str__(self) -> str:
        return f'{super(SportCar, self).__str__()} with max speed of {self.speed}km/h'
