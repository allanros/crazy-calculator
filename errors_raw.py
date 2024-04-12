class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422

try:
    print('bloco try')
    raise HttpUnprocessableEntityError('erro ocorreu')

except Exception as e:
    print('bloco except')
    print(str(e.name), e.status_code, str(e.message))