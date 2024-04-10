from abc import ABC, abstractmethod

class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass


class EmailSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f'Sending email: {message}')

class SMSSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f'Sending SMS: {message}')

class Notificator:
    def __init__(self, sender: NotificationSender) -> None:
        self.__sender = sender

    def send(self, message: str) -> None:
        self.__sender.send_notification(message)

obj = Notificator(SMSSender())
obj.send('Hello World!')