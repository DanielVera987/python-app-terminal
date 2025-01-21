import os

from Common.Constant import Constant as Const

class Core:
    def __init__(self, controller):
        self.__controller = controller
        self.__menu()

    def init(self, option = 1):
        self.__clear()
        option = int(option)

        if option == 1:
            self.__menu()
        elif option == Const.LIST:
            self.__list()
        elif option == Const.SEARCH:
            id_item = input("Id Item: ")
            self.__view(id_item)
        elif option == Const.EXIT:
            exit()

        self.__line()
        self.__footer(option)


    def __menu(self):
        print("--------------------------")
        print("|   SISTEMA PRODUCTOS    |")
        print("--------------------------")
        print("|                        |")
        print("| 1. Menú                |")
        print("| 2. Listar Productos    |")
        print("| 3. Buscar Producto     |")
        print("| 4. Actualizar Producto |")
        print("| 5. Borrar Producto     |")
        print("|                        |")
        print("--------------------------")

    def __list(self):
        items = self.__controller.index()

        for item in items:
            print(str(item["id"]) + " - " + item["title"])

    def __view(self, id):
       item = self.__controller.show(int(id))

       print("ID: " + str(item["id"]))
       print("Title: " + str(item["title"]))
       print("Price: " + str(item["price"]))
       print("Description: " + str(item["description"]))
       print("Category: " + str(item["category"]))

    def __clear(self):
        if os.name == 'nt':
            os.system('cls')  # For Windows
        else:
            os.environ['TERM'] = 'xterm'  # Set TERM to 'xterm' for other platforms like macOS and Linux
            os.system('clear')

    def __footer(self, option):
        info_more = ""

        if (option == Const.LIST):
            info_more = ", Buscar [3]"

        print("Menú [1], Salir: [0] " + info_more)

    def __line(self):
        print("\n")
