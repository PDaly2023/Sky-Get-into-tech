class Animal:
    numCreated = 0
    def __init__(self, name, tricks):
        Animal.numCreated +=1

        self.name = name
        self.tricks = tricks
        