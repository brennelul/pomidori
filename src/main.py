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
    __state = 99
    __computers = []
    __laptops = []
    __smartphones = []
    __cart = []
    __purchaseHistory = []

    def __init__(self):
        with open("db.json", "r") as file:
            __data = json.load(file)
            for i in __data["Computers"].items():
                self.__computers.append(classes.Computers(i[1].get("Processor"),\
                                                     i[1].get("iRAM"), i[1].get("iROM"),\
                                                     i[1].get("name"), i[1].get("color"),\
                                                     i[1].get("price")))
            for i in __data["Laptops"].items():
                self.__laptops.append(classes.Laptops(i[1].get("Processor"),\
                                                     i[1].get("iRAM"), i[1].get("iROM"),\
                                                     i[1].get("name"), i[1].get("color"),\
                                                     i[1].get("price"), i[1].get("screenSize"),\
                                                     i[1].get("batteryCapacity")))
            for i in __data["Smartphones"].items():
                self.__smartphones.append(classes.Smartphones(i[1].get("Processor"),\
                                                     i[1].get("iRAM"), i[1].get("iROM"),\
                                                     i[1].get("name"), i[1].get("color"),\
                                                     i[1].get("price"), i[1].get("screenSize"),\
                                                     i[1].get("batteryCapacity"), i[1].get("camera")))
        with open("account.json", "r") as file:
            __data = json.load(file)
            self.__account = classes.Account(__data.get("AccountID"), __data.get("Money"))

    def FSM_States(self):
        if self.__state == 99: self.__state = self.menu()
        elif self.__state == 1: self.__state = self.checkCategories()
        elif self.__state == 2: self.__state = self.goToCart()
        elif self.__state == 3: self.__state = self.purchaseHistory()
        elif self.__state == 4: self.__state = self.checkAccount()
        elif self.__state == 0: return -1

    def menu(self):
        print("Привет, это DNS\n\t"
              "1) посмотреть категории\n\t"
              "2) перейти в корзину\n\t"
              "3) перейти в историю покупок\n\t"
              "4) посмотреть счет\n\t"
              "0) выход")
        return checkInput(4)

    def checkCategories(self):
        print("Категории:\n\t"
              "1) Компьютеры\n\t"
              "2) Ноутбуки\n\t"
              "3) Смартфоны")
        return self.printCategory(checkInput(3))
    
    def printCategory(self, option):
        if option == 1:
            self.printData(self.__computers)
            return self.addToCart(checkInput(len(self.__computers)), self.__computers)
        elif option == 2:
            self.printData(self.__laptops)
            return self.addToCart(checkInput(len(self.__laptops)), self.__laptops)
        elif option == 3:
            self.printData(self.__smartphones)
            return self.addToCart(checkInput(len(self.__smartphones)), self.__smartphones)

        return 99
    
    def printData(self, data):
        for i in range(len(data)):
            print(f"{i + 1}. {data[i]._name}: Процессор: {data[i]._Processor}, ОЗУ: {data[i]._iRAM} GB, Накопитель: {data[i]._iROM} GB\n"
                    f"Цена: {data[i]._price} руб.")
        print("0. Выход")

    def addToCart(self, option, data):
        print(option)
        if option > 0 and option <= len(data):
            self.__cart.append(data[option - 1]) 
        elif option > len(data):
            print("Некорректное значение")
        
        return 99
        
    def goToCart(self):
        if len(self.__cart) > 0:
            total = 0
            for i in range (len(self.__cart)):
                print(f"{i + 1}. {self.__cart[i]._name}, Цена: {self.__cart[i]._price} руб.")
                total += self.__cart[i]._price

            print(f"Всего: {total} руб.")
            print("\t1) Купить\n\t"
              "2) Очистить корзину\n\t"
              "0) Выход")
            
            option = checkInput(2)
            if option == 1: self.buyCart(total)
            elif option == 2: self.__cart.clear()
        
        else: print("Пусто!")
        return 99
    
    def buyCart(self, total):
        if self.__account.getBalance() >= total:
            self.__account.withdrawMoney(total)
            self.__purchaseHistory.append(self.__cart)
            self.__cart.clear()
        else:
            print("Ошибка, недостаточно средств")
    
    def purchaseHistory(self):
        # print("not implemented")
        for i in range (len(self.__cart)):
            print(f"{i}. {self.__purchaseHistory[i]._name}")
        return 99 
    
    def checkAccount(self):
        print("not implemented")
        return 99

def main():
    store = FSM()
    while True:
        if store.FSM_States() == -1: break
        

if __name__ == "__main__":
    main()