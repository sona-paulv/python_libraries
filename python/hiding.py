class myclass:
    __hiddenvariable=10
    def add(self,increment):
        self.__hiddenvariable+=increment
        print(self.__hiddenvariable)
nyc=myclass()
print(nyc._myclass__hiddenvariable)