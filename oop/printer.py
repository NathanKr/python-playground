from abc import ABC , abstractmethod

@abstractmethod
class Printer(ABC):
    def write(self,text : str):
        pass



