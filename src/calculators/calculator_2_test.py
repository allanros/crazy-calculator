from .calculator_2 import Calculator2
from typing import Dict
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest({
        'numbers': [2.12, 4.62, 1.32]
    })

    calculator2 = Calculator2()
    formated_response = calculator2.calculate(mock_request)
    
    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': '2', 'result': 0.08}}