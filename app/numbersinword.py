#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# units
J = ('', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć', 'dziesięć', 'jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście', 'osiemnaście', 'dziewiętnaście')

# dozens
D = ('', 'dziesięć', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt')

# hundreds of
S = ('', 'sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset')
# thousands, milions

T = ('', 'tysiąc', 'tysiące', 'tysięcy')
NAMES = ('', '', 'y', 'ów')
M = ('', 'milion', 'miliony', 'milionów', )
Mi = ('', 'miliard', 'miliardy', 'miliardów', )
B = ('', 'bilion', 'biliony', 'bilionów', )
Bi = ('', 'biliard', 'biliardy', 'biliarów', )
Tr = ('', 'trylion', 'tryliony', 'trylionów', )

#Groups
G = ('', T, M, Mi, B, Bi, Tr)


class NumberInWords(object):
    """From int(numbers) to string version"""

    def __init__(self):
        pass

    def toString(self, number=None):
        """Główna funkcja która zamienia liczby na wersję słowną
        :number int
        :returns: str"""
        word = ''
        if type(number) is not int:
            return False
        if number == 0:
            return 'zero'

        list_number = []
        list_number = self.convertIntToList(number)
        list_number = self.cutOnGroup(list_number)

        """iteruje od konca aby wyznaczyc numer grupy 0:nic,1:tysiące,2:miliony,3:miliardy..."""
        for x, y in enumerate(list_number[::-1]):
            word = self.convertOneGroupToString(y) + self.getNameOfGroup(x, y) + word
        return ' '.join(word.split())

    def convertIntToList(self, integer):
        """Konwertuje int do listy cyfer
        :integer: int
        returns: list"""

        return [int(x) for x in str(integer)]

    def cutOnGroup(self, list_number):
        """ Dzieli liste jednowymiarową na kilkuwymiarową. Ma to ułatwić nazywanie grup
        :list_number: list
        :return list"""

        list_number = list_number[::-1]
        i = 0
        a = []
        while len(list_number[i:i + 3]) != 0:
            b = list_number[i:i + 3]
            a.append(b[::-1])
            i += 3
        return a[::-1]

    def convertOneGroupToString(self, list_number):
        """ Tworzy string opisujący jedną grupę liczb.
        :list_number: list
        :returns: str"""

        string_number = ''
        intNumber = int("".join([str(x) for x in list_number[-2:]]))

        """Jeżeli liczba ma 3 cyfry zwraca setki"""
        if len(list_number) == 3:
            string_number += '%s ' % S[list_number[0]]

        """ Zwraca liczbę z stalej krotki J jeżeli mniejsza niż 20 lub generuje str"""
        if intNumber < 20:
            string_number += J[intNumber]
        else:
            string_number += ' '.join((D[list_number[-2]], J[list_number[-1]]))

        return ' ' + string_number + ' '

    def getNameOfGroup(self, group, list_number):
        """Każda grupa ma max 3 liczby. Do grupy 0 nie dodajemy slowa tysiące|miliony
        T = ('', 'tysiąc', 'tysiące', 'tysięcy')
        M = ('', 'milion', 'miliony', 'milionów', )
        :group int
       :list_number list
        :returns str"""
        if group == 0:
            return ''

        """j jak jednoski"""
        j = list_number[-1]
        intNumber = int("".join([str(x) for x in list_number[-3:]]))

        if intNumber == 0:
            return ''

        """ Jeżeli liczba 1 to tysiąc|milion|miliard|..."""
        if intNumber == 1:
            return G[group][1]

        if 5 <= intNumber <= 21:
            return G[group][3]

        if 2 <= j <= 4:
            return G[group][2]
        return G[group][3]


if __name__ == "__main__":
    n = NumberInWords()
    number_in_words = n.toString(22000000)
    print(number_in_words)
