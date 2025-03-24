import json


class Account:
    def __init__(self):
        with open("account.json", "r") as file:
            data = json.load(file)
            self.__accountID = data.get("AccountID")
            self.__money = data.get("Money")
            self.__purchaseHistory = data.get("Purchases")

    def addMoney(self, amount):
        if amount > 0:
            self.__money += amount

    def withdrawMoney(self, amount):
        if amount > 0:
            self.__money -= amount

    def getBalance(self):
        return self.__money

    def getAccountID(self):
        return self.__accountID

    def addPurchase(self, purchases):
        for i in range(len(purchases)):
            self.__purchaseHistory[f"item{len(self.__purchaseHistory)}"] = {
                "name": purchases[i]._name,
                "price": purchases[i]._price,
                "SKU": purchases[i]._SKU
            }

    def getPurchaseHistory(self):
        return self.__purchaseHistory

    def saveData(self):
        with open("account.json", "w") as file:
            tempDict = {
                "AccountID": self.__accountID,
                "Money": self.__money,
                "Purchases": self.__purchaseHistory
            }
            json.dump(tempDict, file)


class Item:
    def __init__(self, name, color, price, SKU):
        self._name = name
        self._price = price
        self._color = color
        self._SKU = SKU


class Computers(Item):
    def __init__(self, Processor, iRAM, iROM, name, color, price, SKU):
        super().__init__(name, color, price, SKU)
        self._Processor = Processor
        self._iRAM = iRAM
        self._iROM = iROM


class Laptops(Computers):
    def __init__(self, Processor, iRAM, iROM, name, color,
                 price, screenSize, batteryCapacity, SKU):
        super().__init__(Processor, iRAM, iROM, name, color, price, SKU)
        self._screenSize = screenSize
        self._batteryCapacity = batteryCapacity


class Smartphones(Item):
    def __init__(self, Processor, iRAM, iROM, name, color, price,
                 screenSize, batteryCapacity, camera, SKU):
        super().__init__(name, color, price, SKU)
        self._Processor = Processor
        self._iRAM = iRAM
        self._iROM = iROM
        self._camera = camera
        self._screenSize = screenSize
        self._batteryCapacity = batteryCapacity
