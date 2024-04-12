from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError
from typing import Dict, List

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance, multiplication)

        return self.__format_response(variance)

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise HttpUnprocessableEntityError('Body bad formatted')
        
        input_data = body['numbers']
        return input_data
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        return self.__driver_handler.variance(numbers)
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for number in numbers: multiplication *= number
        return multiplication
    
    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequestError("Variance is less than multiplication")
        
    def __format_response(self, variance: float) -> Dict:
        return {
            'data': {
                'Calculator': '3',
                'value': variance,
                'Success': True
            }
        }