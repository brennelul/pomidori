import classes
import json

def checkInput(maxInt):
    while True:
        try:
            returnOption = int(input("Выберете пункт: "))
            if 0 >= returnOption > maxInt: raise ValueError("Error")
            break
        except:
            print("Ошибка, попробуйте снова")
    return returnOption

class FSM:
    __state = 0
    
    def __init__(self):
        with open ("db.json", "r") as file:
            __data = json.load(file)
            # print(__data)
            __computers = []
            for i in __data["Computers"].items():
                __computers.append(classes.Computers(i[1].get("Processor"),\
                                                     i[1].get("iRAM"), i[1].get("iROM"),\
                                                     i[1].get("name"), i[1].get("color"),\
                                                     i[1].get("price")))
                print(__computers.)

    def FSM_States(self):
        if self.__state == 0: self.__state = self.menu()
        elif self.__state == 1: self.__state = self.checkCategories()
        elif self.__state == 5: return -1
        # elif self.__state == 2:

    def menu(self):
        print("Привет, это DNS\n\t\
              1) посмотреть категории\n\t\
              2) перейти в корзину\n\t\
              3) перейти в историю покупок\n\t\
              4) посмотреть счет\n\t\
              5) выход")
        return checkInput(5)

    def checkCategories(self):
        # if self.__state != 1: return 1
        print("Категории:\n\t\
              1) Компьютеры\n\t\
              2) Ноутбуки\n\t\
              3) Смартфоны")
        self.printCategory(checkInput(3))
    
    # def printCategory(option):


def main():
    store = FSM()
    while True:
        if store.FSM_States() == -1: break
        

if __name__ == "__main__":
    main()