import unittest
from main import perimeter_square, area_square, fio
import pytest

class TestMain(unittest.TestCase):

    def test_perimeter_square(self):
        for i, (a, expected) in enumerate([
            (5, 20),
            (0, 0),
            (2.5, 10),
            (-5, 'Некоректный ввод'),
            ('jshg', 'Некоректный ввод')

        ]):
            with self.subTest(i):
                result = perimeter_square(a)
                self.assertEqual(expected, result)

    def test_area_square(self):
        for i, (a, expected) in enumerate([
            (5, 25),
            (2.5, 6.25),
            (0, 0),
            (-5, 'Некоректный ввод'),
            ('jshg', 'Некоректный ввод')

        ]):
            with self.subTest(i):
                result = area_square(a)
                self.assertEqual(expected, result)

    def test_fio(self):
        self.assertRaises(TypeError, fio, 243)
        self.assertRaises(TypeError, fio, True)
        self.assertEqual(fio(['Жан', 'Клот', 'Вандамович']), 'ЖКВ')
        self.assertEqual(fio(['Павлов', 'Иван', 'Уралович']), 'ПИУ')

if __name__ == "__main__":
    unittest.main()