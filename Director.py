import os
import re

class Director():
    def __init__(self, nume, cale_absoluta):
        self.nume = nume
        self.cale =  cale_absoluta

    def afisare_elemente(self):
        print(os.listdir(self.cale))


    def afisare_dir_regex(self):
         patternul = 'test'
         lista = os.listdir(self.cale)
         for obj in lista:
            if re.search(patternul, obj):
                print(obj)





