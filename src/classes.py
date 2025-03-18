class Item:
    def __init__(self, name, color, price):
        self._name = name
        self._price = price
        self._color = color

class Computers(Item):
    def __init__(self, Processor, iRAM, iROM, name, color, price):
        super().__init__(name, color, price)
        self._Processor = Processor
        self._iRAM = iRAM
        self._iROM = iROM
    
    def returnItems(self):
        return self.__Processor, self.__iRAM, self.__iROM, self.__name, self.__color, self.__price

class Laptop(Computers):
    def __init__(self, Processor, iRAM, iROM, screenSize, batteryCapacity, name, color, price):
        super().__init__(Processor, iRAM, iROM, name, color, price)
        self._screenSize = screenSize
        self._batteryCapacity = batteryCapacity
    def returnItems(self):
       return self.__Processor, self.__iRAM, self.__iROM, self.__name, self.__color, self.__price


class Smartphones(Item):
    def __init__(self, Processor, iRAM, iROM, camera, screenSize, batteryCapacity, name, color, price):
        super().__init__(name, color, price)
        self._Processor = Processor
        self._iRAM = iRAM
        self._iROM = iROM
        self._camera = camera
        self._screenSize = screenSize
        self._batteryCapacity = batteryCapacity
