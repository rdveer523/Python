"""
20200423---Abstract by Telusko
-------------------------------
Here you will have an Error (as below) if you tried with Abstract class only.
because abstract class can not be instantiate with it's abstract methods because
python doesn't have abstract class method as default itself. so, To overcome
with this we should make a child or sub class to instantiate

TypeError: Can't instantiate abstract class with abstract methods.

Ex:

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

com = Computer()
print(com.process())
"""
#another way-1
"""
# here also the same error you will get if you do the child class as declaration
# because Lap class instantiated the Computer Abstract class method but method
# is not defined in child class. so while instantiating the abstract class from
# child class then method should be defined then only abstract class will work.
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Lap(Computer):
    pass

#com = Computer()
com1 = Lap()
#print(com1.process())
"""
#child class-1
"""
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Lap(Computer):
    def process(self):
        print("SUccess...Abstract class instantiated from Lap child class with defined method.")

#com = Computer() #you can not call the abstract class to an object because method
        #is not defined and to define the method you should have sub class
com1 = Lap()
#com1.process()
"""
#adding more child classes

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Lap(Computer):
    def process(self):
        print("Abstract class (Computer) instantiated by Lap child class.")

class programmer:
    def work(self,prog):
        print("programmer class instantiated the Lap class")
        prog.process()

class Developer:
    def dev(self,devlap):
        print("Developer class instantiated the Lap class method and programmer method")
        #devprog.work()
        devlap.process()
        
#com = Computer() #you can not call the abstract class to an object because method
        #is not defined and to define the method you should have sub class
com = Lap()
com.process()

com1 = programmer()
com1.work(com) #here i should pass the object of first child class (Laptop)

com2 = Developer()
com2.dev(com)
