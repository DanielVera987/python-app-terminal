from abc import ABC, abstractmethod

class BaseReporitory(ABC):
    @abstractmethod
    def getAll(self):
        pass
            
    @abstractmethod
    def getById(self, id = None):
        pass
        
    @abstractmethod
    def create(self, data = None):
        pass

    @abstractmethod
    def update(self, id, data = None):
        pass

    @abstractmethod
    def delete(self, id):
        pass