import unittest
from Descriptors import Data


class TestDescriptors(unittest.TestCase):

    # Проверяем дескриптор integer
    def test_integer(self):
        a = Data()
        self.assertEqual(a.num, None)

        a.num = 1
        self.assertEqual(a.num, 1)

        # Проверка изменения значения
        a.num = 2
        self.assertEqual(a.num, 2)

        # Проверяем, что при попытке записать значение не того типа возникает ошибка
        with self.assertRaisesRegex(TypeError, 'Not Integer'):
            a.num = 'abc'

        # Проверка значения после ошибки
        self.assertEqual(a.num, 2)

        with self.assertRaisesRegex(TypeError, 'Not Integer'):
            a.num = []

        self.assertEqual(a.num, 2)

    # Проверяем дескриптор string
    def test_string(self):
        a = Data()
        self.assertEqual(a.name, None)

        a.name = 'abc'
        self.assertEqual(a.name, 'abc')

        # Проверка изменения значения
        a.name = 'kitten'
        self.assertEqual(a.name, 'kitten')

        # Проверяем, что при попытке записать значение не того типа возникает ошибка
        with self.assertRaisesRegex(TypeError, 'Not String'):
            a.name = 1

        # Проверка значения после ошибки
        self.assertEqual(a.name, 'kitten')

        with self.assertRaisesRegex(TypeError, 'Not String'):
            a.name = []

        # Проверка значения после ошибки
        self.assertEqual(a.name, 'kitten')

        # Проверяем, что, при попытке записать строку неподходящей длины, возникает ошибка
        with self.assertRaisesRegex(ValueError, 'Too long'):
            a.name = 'Aaaaaaaaaaammmmmm'

        self.assertEqual(a.name, 'kitten')

        with self.assertRaisesRegex(ValueError, 'Too small'):
            a.name = ''

        self.assertEqual(a.name, 'kitten')

    # Проверяем дескриптор положительный integer
    def test_positive_integer(self):
        a = Data()
        self.assertEqual(a.price, None)

        a.price = 1
        self.assertEqual(a.price, 1)

        # Проверка изменения значения
        a.price = 2
        self.assertEqual(a.price, 2)

        # Проверяем, что при попытке записать значение не того типа возникает ошибка
        with self.assertRaisesRegex(TypeError, 'Not Integer'):
            a.price = 'abc'

        # Проверка значения после ошибки
        self.assertEqual(a.price, 2)

        with self.assertRaisesRegex(TypeError, 'Not Integer'):
            a.price = []

        self.assertEqual(a.price, 2)

        # Проверяем, что, при попытке записать не положительное число, возникает ошибка
        with self.assertRaisesRegex(ValueError, 'Not positive'):
            a.price = -5

        self.assertEqual(a.price, 2)

        with self.assertRaisesRegex(ValueError, 'Not positive'):
            a.price = 0

        self.assertEqual(a.price, 2)


if __name__ == '__main__':
    unittest.main()
