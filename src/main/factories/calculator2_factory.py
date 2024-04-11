from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

def calculator2_factory():
    calc = Calculator2(NumpyHandler())
    return calc