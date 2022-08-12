from abc import ABC, abstractmethod

class DailyCheck(ABC):
    name: str
    prefix: str
    environment: str

    def __init__(self, environment, prefix):
        self.environment = environment
        self.prefix = prefix

    @abstractmethod
    def perform_check(self):
        pass