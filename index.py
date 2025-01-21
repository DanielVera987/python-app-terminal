from Controller.ProductController import ProductController
from Core.index import Core

product = ProductController()
app = Core(product)

option = 1
while option != 0:
    option = input("Elige una opción: ")
    app.init(option)