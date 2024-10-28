from Repository.ProductRepository import ProductRepository

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def index(self):
        products = self.repository.getAll()    
        return products
    
    def show(self, id):
        pass

    def add():
        pass

    def update():
        pass

    def delete():
        pass
        