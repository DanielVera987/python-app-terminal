from abc import ABC, abstractmethod

class IService(ABC):
    @abstractmethod
    def index():
        pass

    @abstractmethod
    def show():
        pass

    @abstractmethod
    def add():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def delete():
        pass