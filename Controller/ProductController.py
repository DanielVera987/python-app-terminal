from Service.ProductService import ProductService
from Common.Constant import Constant

class ProductController():
    def __init__(self):
        self.service = ProductService()

    def index(self):
        return self.service.index()

    def show(self, id):
        product = self.service.show(id)

        if (product):
            return product

        return Constant.NOT_FOUND_MESSAGE

    def create(self, data = None):
        return self.service.add(data)

    def update(self, id = None, data = None):
        if (id != None and (data != None and type(data) == dict)):
            return self.service.update(id, data)

        return False

    def delete(self, id):
        if (id != None and isinstance(id, (int, float))):
            return self.service.delete(id)
        
        return False