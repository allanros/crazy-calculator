from flask import Request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        return self.__format_response(calculated_number)

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise Exception('Body bad formatted')
        
        input_data = body['numbers']
        return input_data
    
    def __process_data(self, numbers: List[float]) -> float:
        first_process_result = [(num * 11) ** .95 for num in numbers]
        result = self.__driver_handler.standard_derivation(first_process_result)

        return 1/result
    
    def __format_response(self, result: float) -> Dict:
        return {
            'data': {
                'Calculator': '2',
                'result': round(result, 2)
            }
        }