"""This program displays simple vaccination details and date of vaccicnation of a person
 which uses only lists,dicts,getters and setters"""
import os
clear = lambda: os.system('cls')
class vaccination():

    def __init__(self,Name,Vaccination,date):
        self.__Name=Name
        self.__vaccination=Vaccination
        self.__date=date

    def info(self):
        clear()
        data=dict(zip(self.__vaccination,self.__date))
        return self.__Name+" is vaccinated with \n"+ ("\n".join("{} on {}".format(k,v)for k,v in data.items())) 

    #getters
    def getName(self):
        return self.__Name

    def getvaccination(self):
        return self.__vaccination

    def getdate(self):
        return self.__date

    #setters
    def setName(self,name):
        self.__Name=name

    def setvaccination(self,vaccination):
        self.__vaccination=vaccination

    def setdate(self,date):
        self.__date=date


  


# """The codes below is a basic program that uses getters and setters.We removed login system for a quicker presentation"""
# a=vaccination("asw",["Covid","Polio","TB"],["19-05-2020","20-05-1999","19-08-2016"])
# print(a.getName())
# a.setName("Aswath")
# print(a.getName())
# print(a.info())