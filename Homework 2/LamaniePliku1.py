# -*- coding: utf-8 -*-
import hashlib
import os

'''
Do stworzenia pliku dictionary1.txt uzylam pliku odm.txt, zawierajacy wszystkie slowa z internetowego slownika sjp.pl,
ktory pobralam ze strony http://sjp.pl/slownik/odmiany/.
Plik ten zajmuje ponad 50MB, wiec nie zostal on zalaczony w przeslanej paczce.
Z tego powodu fragment kodu, ktory odwoluje sie do tego pliku, zostal zakomentowany, a wynik jego dzialania
(plik dictionary1.txt) zostal umieszczony w folderze z rozwiazaniami, aby umozliwic realizacje reszty kodu bez potrzeby
dolaczania przez Pana odm.txt do tego folderu.
'''

'''
source = open('odm.txt', "r")
dic = open('dictionary1.txt', 'a')
excluded = ("ą", "ć", "ę", "ł", "ń", "ó", "ś", "ź", "ż", ".", "-", "'", " ", "à", "é", "ç", "ô", "ü", "Ł", "ö")

while True:
    line = source.readline()

    if line.startswith("ź"):
        break
    if line.islower() and not any(i in line for i in excluded):
        if "," in line:
            splitLine = line.split(",")
            dic.write(splitLine[0])
        else:
            dic.write(line)
source.close()
dic.close()
'''

dic = open('dictionary1.txt', 'r')
hashDic = open('hash_dictionary1.txt', 'a')

while True:
    line = dic.readline()
    word = ''

    if len(line) < 1:
        break
    for i in range(0, len(line)):
        if line[i] != "\n":
            word += line[i]
        else:
            break
    hashDic.write(hashlib.md5(word.encode('utf-8')).hexdigest() + "\n")
dic.close()
hashDic.close()


def find_word(hash_word):
    i = 0
    line = None
    found = False
    dic = open('hash_dictionary1.txt', 'r')

    while not found:
        line = dic.readline()
        if hash_word in line:
            found = True
        i += 1
    dic.close()

    dic = open('dictionary1.txt', 'r')
    while i > 0:
        line = dic.readline()
        i -= 1
    return line

hashes = open('1.txt')
while True:
    temp = open('temp.txt', "a")
    line = hashes.readline()
    word = ""

    if line == "":
        break
    for i in range(0, len(line)):
        if line[i] != "\n":
            word += line[i]
    temp.write(word + " ")
    word = find_word(word)
    temp.write(word)
    temp.close()
hashes.close()

words = open('res1.txt', "a")
temp = open('temp.txt', "r")
while True:
    line = temp.readline()
    if not line.startswith(" "):
        words.write(line)
    if line == "":
        break
words.close()
temp.close()
os.remove('temp.txt')
