import os
import re
from Director import Director
from Fisier1 import Fisier

#creeam directoarele si fisierele
os.chdir("C:\\Users\\Antoo\\Desktop")
#os.mkdir("1")
os.chdir("C:\\Users\\Antoo\\Desktop\\1")
# os.mkdir("2")
# os.mkdir("3")
# os.mkdir("4")

os.chdir("C:\\Users\\Antoo\\Desktop\\1\\4")
with open(os.getcwd()+'\\test4.txt', mode='w') as f:
    f.writelines(['Test4 \n','Test4 \n', 'Test4'])

os.chdir("C:\\Users\\Antoo\\Desktop\\1\\3")
with open(os.getcwd()+'\\test3.txt', mode='w') as f:
    f.writelines(['Test3\n','Test3\n','Stop\n','Test3'])

os.chdir("C:\\Users\\Antoo\\Desktop\\1\\2")
# os.mkdir("5")
# os.mkdir("6")

with open(os.getcwd()+'\\test2.txt', mode='w') as f:
    f.writelines(['Test2\n', 'Test2\n', 'Test2\n'])

os.chdir("C:\\Users\\Antoo\\Desktop\\1\\2\\5")
with open(os.getcwd()+"\\test5.txt", mode='w') as f:
    f.writelines(['Test5\n', 'Test5\n','Test5\n'])

os.chdir("C:\\Users\\Antoo\\Desktop\\1\\2\\6")
with open(os.getcwd()+'\\test6.txt', mode='w') as f:
    f.writelines(['Test6\n', 'Test6\n', 'Test6\n'])


file_list=[]
dir_list = []
def lista_dir(cale):

    for element in os.listdir(cale):

        if os.path.isdir(os.path.abspath(cale) + "\\" + element):

            dir_list.append(Director(element, os.path.abspath(cale)+"\\"+element))

            lista_dir(os.path.abspath(cale) + "\\" + element)

lista_dir("C:\\Users\\Antoo\\Desktop\\1")
#print(dir_list)

def lista_fisier(cale):
    for element in os.listdir(cale):


        if os.path.isdir(os.path.abspath(cale) + "\\" + element):

            lista_fisier(os.path.abspath(cale) + "\\" + element)

        else:
            file_list.append(Fisier(element,os.path.abspath(cale) + "\\" + element ))

lista_fisier("C:\\Users\\Antoo\\Desktop\\1")
#print(file_list)

for obj in dir_list:
    print(obj.afisare_elemente())

for obj in file_list:
    print(obj.afisare_fisier())

for obj in file_list:
    print(obj.afisare_fisier_regex())