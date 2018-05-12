from django.test import SimpleTestCase
from .numbersinword import NumberInWords


class NumberTestCase(SimpleTestCase):
    dictionary = {
        "2200000": "dwa miliony dwieście tysięcy",
        "1": "jeden",
        "13": "trzynaście",
        "123000": "sto dwadzieścia trzy tysiące",
        "127000": "sto dwadzieścia siedem tysięcy",
        "129000": "sto dwadzieścia dziewięć tysięcy",
        "3000000": "trzy miliony",
        "5000": "pięć tysięcy",
        "6000": "sześć tysięcy",
        "7000": "siedem tysięcy",
        "002": "dwa",
        "21000": "dwadzieścia jeden tysięcy",
        "22000": "dwadzieścia dwa tysiące",
        "23000": "dwadzieścia trzy tysiące",
        "124": "sto dwadzieścia cztery",
        "125000": "sto dwadzieścia pięć tysięcy",
        "126": "sto dwadzieścia sześć",
        "22000000": "dwadzieścia dwa miliony",
        "100000000": "sto milionów",
        "111": "sto jedenaście",
        "2345": "dwa tysiące trzysta czterdzieści pięć",
        "99999": "dziewięćdziesiąt dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć",
        "900021": "dziewięćset tysięcy dwadzieścia jeden",
        "993999994999959": "dziewięćset dziewięćdziesiąt trzy biliony dziewięćset dziewięćdziesiąt dziewięć miliardów dziewięćset dziewięćdziesiąt cztery miliony dziewięćset dziewięćdziesiąt dziewięć tysięcy dziewięćset pięćdziesiąt dziewięć"}

    def test_numbers(self):
        n = NumberInWords()

        self.assertEqual(n.toString(0), 'zero')
        self.assertEqual(n.toString(3), 'trzy')
        self.assertEqual(n.toString(''), False)
        self.assertEqual(n.toString('asdfsdfsd'), False)
        self.assertNotEqual(n.toString(22), 'trzydzieści dwa')

        for key, value in self.dictionary.items():
            self.assertEqual(n.toString(int(key)), value)

        self.assertEqual(n.convertIntToList(123), [1, 2, 3])
        self.assertNotEqual(n.convertIntToList(123999), [1, 2, 3])
        self.assertEqual(n.cutOnGroup([1, 2, 3, 4]), [[1], [2, 3, 4]])
