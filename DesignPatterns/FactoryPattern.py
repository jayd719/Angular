# Factory Pattern is a creation pattern in that defines an interface for creating objects and defers instantiation unit run time
# Used when we don't know how many and what type of objects will be created at run time.

# Flexible, Scalable, and Bug Free
# Factory takes responsibility of creating all the objects

# Resource : https://www.youtube.com/watch?v=VgQq2B0kC0o
#          : https://www.youtube.com/watch?v=04J_fL5zg3U

from abc import ABC,abstractmethod

# Base class for shared behaviour
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        raise NotImplementedError("This Method Should be overwritten by subclass")


# Specific Pizza Classes
class CheesePizza(Pizza):
    def prepare(self):
        return "Prepare Cheese Pizza"


class PepperoniPizza(Pizza):
    def prepare(self):
        return "Prepare Pepperoni Pizza"


class VeggiePizza(Pizza):
    def prepare(self):
        return "Prepare Veggie Pizza"


# Factory Class
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type:str):
        match pizza_type.lower():
            case "cheese":return  CheesePizza()
            case "pepperoni": return PepperoniPizza()
            case "veggie": return VeggiePizza()
            case _: raise ValueError("Unknown Pizza Type")



if __name__=="__main__":
    print("Testing Pizza")
