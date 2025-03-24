class Account:
    def __init__(self, accountID, money):
        self.__accountID = accountID
        self.__money = money

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

class Item:
    def __init__(self, name, color, price):
        self._name = name
        self._price = price
        self._color = color

    def returnItems(self):
        return self._name, self._color, self._price

class Computers(Item):
    def __init__(self, Processor, iRAM, iROM, name, color, price):
        super().__init__(name, color, price)
        self._Processor = Processor
        self._iRAM = iRAM
        self._iROM = iROM
    
    def returnItems(self):
        return super().returnItems(), self._Processor, self._iRAM, self._iROM

class Laptops(Computers):
    def __init__(self, Processor, iRAM, iROM, name, color, price, screenSize, batteryCapacity):
        super().__init__(Processor, iRAM, iROM, name, color, price)
        self._screenSize = screenSize
        self._batteryCapacity = batteryCapacity

    def returnItems(self):
        return super().returnItems(), self._screenSize, self._batteryCapacity
    
class Smartphones(Item):
    def __init__(self, Processor, iRAM, iROM, name, color, price, screenSize, batteryCapacity, camera):
        super().__init__(name, color, price)
        self._Processor = Processor
        self._iRAM = iRAM
        self._iROM = iROM
        self._camera = camera
        self._screenSize = screenSize
        self._batteryCapacity = batteryCapacity

    # def returnItems(self):
        # return super().returnItems()
