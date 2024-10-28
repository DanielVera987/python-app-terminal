from Service.ProductService import ProductService

class ProductController():
    def __init__(self):
        self.service = ProductService()

    def index(self):
        products = self.service.index()

        for product in products:
            print("Nombre: " + product["title"])

    def show(self, id):
        pass

    def create():
        pass

    def update():
        pass

    def delete():
        pass
        