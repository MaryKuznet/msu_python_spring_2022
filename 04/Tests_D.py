import unittest
from Descriptors import Data


class TestDescriptors(unittest.TestCase):

    # Проверяем дескриптор integer
    def test_integer(self):
        a = Data()
        self.assertEqual(a.num, None)

        a.num = 1
        self.assertEqual(a.num, 1)

        # Проверяем, что при попытке записать значение не того типа возникает ошибка
        with self.assertRaisesRegex(TypeError, 'Not Integer'):
            a.num = 'abc'

        with self.assertRaisesRegex(TypeError, 'Not Integer'):
            a.num = []

    # Проверяем дескриптор string
    def test_string(self):
        a = Data()
        self.assertEqual(a.name, None)

        a.name = 'abc'
        self.assertEqual(a.name, 'abc')

        # Проверяем, что при попытке записать значение не того типа возникает ошибка
        with self.assertRaisesRegex(TypeError, 'Not String'):
            a.name = 1

        with self.assertRaisesRegex(TypeError, 'Not String'):
            a.name = []

        # Проверяем, что, при попытке записать строку неподходящей длины, возникает ошибка
        with self.assertRaisesRegex(ValueError, 'Too long'):
            a.name = 'Aaaaaaaaaaammmmmm'

        with self.assertRaisesRegex(ValueError, 'Too small'):
            a.name = ''

    # Проверяем дескриптор положительный integer
    def test_positive_integer(self):
        a = Data()
        self.assertEqual(a.price, None)

        a.price = 1
        self.assertEqual(a.price, 1)

        # Проверяем, что при попытке записать значение не того типа возникает ошибка
        with self.assertRaisesRegex(TypeError, 'Not Integer'):
            a.price = 'abc'

        with self.assertRaisesRegex(TypeError, 'Not Integer'):
            a.price = []

        # Проверяем, что, при попытке записать не положительное число, возникает ошибка
        with self.assertRaisesRegex(ValueError, 'Not positive'):
            a.price = -5

        with self.assertRaisesRegex(ValueError, 'Not positive'):
            a.price = 0


if __name__ == '__main__':
    unittest.main()
