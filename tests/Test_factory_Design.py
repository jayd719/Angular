import pytest
from DesignPatterns.FactoryPattern import *


def test_creation_cheese_pizza():
    assert isinstance(PizzaFactory.create_pizza("cheese"),CheesePizza)
    assert isinstance(PizzaFactory.create_pizza("Cheese"), CheesePizza)

def test_creation_veggie_pizza():
        assert isinstance(PizzaFactory.create_pizza("veggie"), VeggiePizza)
        assert isinstance(PizzaFactory.create_pizza("veGGie"), VeggiePizza)

def test_creation_pepperoni_pizza():
    assert isinstance(PizzaFactory.create_pizza("pepperoni"), PepperoniPizza)

def test_invalid_pizza_type():
    with pytest.raises(ValueError):
        PizzaFactory.create_pizza("xyb")
