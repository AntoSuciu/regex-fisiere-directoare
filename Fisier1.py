import os
import re

class Fisier():
    def __init__(self, nume, cale_absoluta):
        self.nume = nume
        self.cale = cale_absoluta

    def afisare_fisier(self):
        with open(self.cale, mode='rt', encoding='UTF-8') as file:
           print(file.readlines())


    def afisare_fisier_regex(self):
        with open(self.cale, mode='rt', encoding='UTF-8') as file:
            for line in file:
                if re.search("Test", line):
                    print(line)
