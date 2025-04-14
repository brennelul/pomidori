import classes
import json
import os


def checkInput(maxInt):
    while True:
        try:
            returnOption = int(input("Выберете пункт: "))
            if 0 >= returnOption > maxInt:
                raise ValueError("Некорректный пункт")
            break
        except BaseException:
            print("Ошибка, попробуйте снова")
    return returnOption


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class FSM:
    __state = 99
    __computers = []
    __laptops = []
    __smartphones = []
    __cart = []
    __account = classes.Account()

    def __init__(self):
        with open("db.json", "r") as file:
            __data = json.load(file)
            for i in __data["Computers"].items():
                self.__computers.append(classes.Computers(i[1].get("Processor"),
                                                          i[1].get("iRAM"), i[1].get(
                                                              "iROM"),
                                                          i[1].get("name"), i[1].get(
                                                              "color"),
                                                          i[1].get("price"), i[1].get("SKU")))
            for i in __data["Laptops"].items():
                self.__laptops.append(classes.Laptops(i[1].get("Processor"),
                                                      i[1].get("iRAM"), i[1].get(
                                                          "iROM"),
                                                      i[1].get("name"), i[1].get(
                                                          "color"),
                                                      i[1].get("price"), i[1].get(
                                                          "screenSize"),
                                                      i[1].get("batteryCapacity"), i[1].get("SKU")))
            for i in __data["Smartphones"].items():
                self.__smartphones.append(classes.Smartphones(i[1].get("Processor"),
                                                              i[1].get("iRAM"), i[1].get(
                                                                  "iROM"),
                                                              i[1].get("name"), i[1].get(
                                                                  "color"),
                                                              i[1].get("price"), i[1].get(
                                                                  "screenSize"),
                                                              i[1].get("batteryCapacity"), i[1].get(
                                                                  "camera"),
                                                              i[1].get("SKU")))

    def FSM_States(self):
        if self.__state == 99:
            self.__state = self.menu()
        elif self.__state == 1:
            self.__state = self.checkCategories()
        elif self.__state == 2:
            self.__state = self.goToCart()
        elif self.__state == 3:
            self.__state = self.purchaseHistory()
        elif self.__state == 4:
            self.__state = self.checkAccount()
        elif self.__state == 0:
            return -1

    def menu(self):
        cls()
        print("Привет, это DNS\n"
              "\t1) посмотреть категории\n"
              "\t2) перейти в корзину\n"
              "\t3) перейти в историю покупок\n"
              "\t4) посмотреть счет\n"
              "\t0) выход")
        return checkInput(4)

    def checkCategories(self):
        cls()
        print("Категории:\n"
              "\t1) Компьютеры\n"
              "\t2) Ноутбуки\n"
              "\t3) Смартфоны")
        return self.printCategory(checkInput(3))

    def printCategory(self, option):
        if option == 1:
            self.printData(self.__computers)
            return self.addToCart(checkInput(
                len(self.__computers)), self.__computers)
        elif option == 2:
            self.printData(self.__laptops)
            return self.addToCart(checkInput(
                len(self.__laptops)), self.__laptops)
        elif option == 3:
            self.printData(self.__smartphones)
            return self.addToCart(checkInput(
                len(self.__smartphones)), self.__smartphones)

        return 99

    def printData(self, data):
        cls()
        for i in range(len(data)):
            print(f"{i + 1}. {data[i]._name}: Процессор: {data[i]._Processor}, ОЗУ: {data[i]._iRAM} GB, Накопитель: {data[i]._iROM} GB, Артикул: {data[i]._SKU}\n"
                  f"Цена: {data[i]._price} руб.")
        print("0. Выход")

    def addToCart(self, option, data):
        if option > 0 and option <= len(data):
            self.__cart.append(data[option - 1])
        elif option > len(data):
            print("Некорректное значение")

        return 99

    def goToCart(self):
        cls()
        if len(self.__cart) > 0:
            total = 0
            for i in range(len(self.__cart)):
                print(
                    f"{i + 1}. {self.__cart[i]._name}, Цена: {self.__cart[i]._price} руб.")
                total += self.__cart[i]._price

            print(f"Всего: {total} руб.")
            if self.__account.getBalance() < total:
                print("На счету недостаточно средств")
            else:
                print("\t1) Купить")
            print("\t2) Очистить корзину\n"
                  "\t0) Выход")

            option = checkInput(2)
            if option == 1 and self.__account.getBalance() >= total:
                self.buyCart(total)
            elif option == 2:
                self.__cart.clear()

        else:
            print("Пусто!\n"
                  "\t0) Выход")
            checkInput(0)
        return 99

    def buyCart(self, total):
        if self.__account.getBalance() >= total:
            self.__account.withdrawMoney(total)
            self.__account.addPurchase(self.__cart)
            self.__cart.clear()
            self.__account.saveData()

    def purchaseHistory(self):
        cls()
        print(f"История покупок для аккаунта {self.__account.getAccountID()}:")
        total = 0
        puchases = self.__account.getPurchaseHistory()
        for i in puchases.items():
            print(f"{i[1].get("name")}, Цена: {i[1].get("price")}")
        print("\t0) Выход")
        checkInput(0)

        return 99

    def checkAccount(self):
        cls()
        print(f"На счету {self.__account.getAccountID()} сейчас {self.__account.getBalance()} руб\n"
              "\t1) Пополнить баланс\n"
              "\t2) Получить газзилион долларов\n"
              "\t0) Выход")
        option = checkInput(2)
        if option == 1:
            while True:
                try:
                    money = int(input("Введите необходимую сумму: "))
                    if 0 >= money:
                        raise ValueError("Сумма не может быть отрицательной")
                    break
                except BaseException:
                    print("Ошибка, попробуйте снова")
            self.__account.addMoney(money)
            self.__account.saveData()
        elif option == 2:
            self.__account.addMoney(9999999999)
            self.__account.saveData()
        return 99


def main():
    store = FSM()
    while True:
        if store.FSM_States() == -1:
            break


if __name__ == "__main__":
    main()
