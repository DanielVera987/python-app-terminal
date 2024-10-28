from Repository.ProductRepository import ProductRepository
from Common.Constant import Constant

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def index(self):
        products = self.repository.getAll()    
        return products
    
    def show(self, id):
        product = self.repository.getById(id)
        return product

    def add(self, data):
        if (data != None):
            return self.repository.create(data)
        
        return False

    def update(self, id = None, data = None):
        if (id != None and data != None):
            return self.repository.update(id, data)

        return False

    def delete(self, id):
        try:
            product = self.repository.getById(id)

            if (product):
                return self.repository.delete(id)
            else:
                return Constant.NOT_FOUND_MESSAGE
        except Exception:
            return False
        