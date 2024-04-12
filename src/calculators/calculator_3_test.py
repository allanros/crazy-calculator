from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3
from typing import Dict, List
from pytest import raises

class MockRequest:
    def __init__(self, json_data: Dict) -> None:
        self.json = json_data

class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 3
    
class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        return 30000


def test_calculate_with_variance_error():
    
    mock_request = MockRequest({'numbers': [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)
   
    assert str(excinfo.value) == 'Variance is less than multiplication'

def test_calculate():
    
    mock_request = MockRequest({'numbers': [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandler())

    response = calculator_3.calculate(mock_request)

    assert response == {'data': {'Calculator': '3', 'value': 30000, 'Success': True}}

def test_calculate_integration():
    
    mock_request = MockRequest({'numbers': [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(NumpyHandler())

    response = calculator_3.calculate(mock_request)

    assert response == {'data': {'Calculator': '3', 'value': 1568.16, 'Success': True}}
