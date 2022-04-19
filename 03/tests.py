import unittest
from main import CustomList


class TestCustomList(unittest.TestCase):

    def setUp(self):
        self.a = CustomList([1, 2, 3])
        self.b = CustomList([1, 1])
        self.list1 = [2, 2]
        self.c = CustomList([3, 3, 3])
        self.d = CustomList()

    # Поэлементное сравнение списков
    def comparison(self, list1, list2):
        self.assertEqual(len(list1), len(list2))
        for elem1, elem2 in zip(list1, list2):
            self.assertEqual(elem1, elem2)

    # Тестируем метод __str__
    def test__str__(self):
        self.assertEqual(self.d.__str__(), '[] 0')
        self.assertEqual(self.a.__str__(), '[1, 2, 3] 6')

    # Тестируем метод метод делающий списки одной длины
    def test_one_size(self):
        a, b = CustomList.one_size([1, 2], [1, 2, 3, 4])

        self.comparison(a, [1, 2, 0, 0])
        self.comparison(b, [1, 2, 3, 4])

        a, b = CustomList.one_size([], [1, 2])
        self.comparison(a, [0, 0])
        self.comparison(b, [1, 2])

        a, b = CustomList.one_size([1, 2], [3, 4])
        self.comparison(a, [1, 2])
        self.comparison(b, [3, 4])

    # Тестируем сложение
    def test__add__(self):

        self.comparison(self.a + self.b, CustomList([2, 3, 3]))
        self.comparison(self.b + self.a, CustomList([2, 3, 3]))
        self.comparison(self.b + CustomList(self.list1), CustomList([3, 3]))
        self.comparison(self.a + self.list1, CustomList([3, 4, 3]))
        self.comparison(self.b + self.list1, CustomList([3, 3]))

        # Проверяем что тип результата CustomList
        self.assertIsInstance(self.a + self.b, CustomList)
        self.assertIsInstance(self.a + self.list1, CustomList)

        # Проверяем, что исходные списки не изменились
        self.comparison(self.a, CustomList([1, 2, 3]))
        self.comparison(self.b, CustomList([1, 1]))
        self.comparison(self.list1, [2, 2])

    # Тестируем сложение справа
    def test__radd__(self):

        self.comparison(self.list1 + self.a, CustomList([3, 4, 3]))
        self.comparison(self.list1 + self.b, CustomList([3, 3]))

        # Проверяем что тип результата CustomList
        self.assertIsInstance(self.list1 + self.a, CustomList)
        self.assertIsInstance(self.list1 + self.b, CustomList)

        # Проверяем, что исходные списки не изменились
        self.comparison(self.a, CustomList([1, 2, 3]))
        self.comparison(self.b, CustomList([1, 1]))
        self.comparison(self.list1, [2, 2])

    # Тестируем вычитание
    def test__sub__(self):

        self.comparison(self.a - self.b, CustomList([0, 1, 3]))
        self.comparison(self.b - self.a, CustomList([0, -1, -3]))
        self.comparison(self.b - CustomList(self.list1), CustomList([-1, -1]))
        self.comparison(self.a - self.list1, CustomList([-1, 0, 3]))
        self.comparison(self.b - self.list1, CustomList([-1, -1]))
        self.comparison(CustomList() - self.list1, [-2, -2])

        # Проверяем что тип результата CustomList
        self.assertIsInstance(self.a - self.b, CustomList)
        self.assertIsInstance(CustomList() - self.list1, CustomList)

        # Проверяем, что исходные списки не изменились
        self.comparison(self.a, CustomList([1, 2, 3]))
        self.comparison(self.b, CustomList([1, 1]))
        self.comparison(self.list1, [2, 2])

    # Тестируем вычитание справа
    def test__rsub__(self):
        self.comparison(self.list1 - self.a, CustomList([1, 0, -3]))
        self.comparison(self.list1 - self.b, CustomList([1, 1]))

        # Проверяем что тип результата CustomList
        self.assertIsInstance(self.list1 - self.a, CustomList)
        self.assertIsInstance(self.list1 - self.b, CustomList)

        # Проверяем, что исходные списки не изменились
        self.comparison(self.a, CustomList([1, 2, 3]))
        self.comparison(self.b, CustomList([1, 1]))
        self.comparison(self.list1, [2, 2])

    # Тестируем сложение +=
    def test__iadd__(self):
        self.a += self.b
        self.comparison(self.a, CustomList([2, 3, 3]))
        self.b += CustomList(self.list1)
        self.comparison(self.b, CustomList([3, 3]))
        self.b += self.list1
        self.comparison(self.b, CustomList([5, 5]))

        # Проверяем что тип результата CustomList
        self.assertIsInstance(self.b, CustomList)

    # Тестируем вычитание -=
    def test__isub__(self):
        self.a -= self.b
        self.comparison(self.a, CustomList([0, 1, 3]))
        self.b -= CustomList(self.list1)
        self.comparison(self.b, CustomList([-1, -1]))
        self.b -= self.list1
        self.comparison(self.b, CustomList([-3, -3]))

        # Проверяем что тип результата CustomList
        self.assertIsInstance(self.b, CustomList)

    # Тестируем сравнение
    def test__lt__(self):
        self.b.append(4)

        self.assertFalse(self.a < self.b)
        self.assertFalse(self.c < self.a)
        self.assertTrue(self.a < self.c)
        self.assertTrue(self.d < self.c)

    # Тестируем сравнение
    def test__le__(self):
        self.b.append(4)

        self.assertTrue(self.a <= self.b)
        self.assertFalse(self.c <= self.a)
        self.assertTrue(self.a <= self.c)
        self.assertTrue(self.d <= self.c)

    # Тестируем сравнение
    def test__eq__(self):
        self.b.append(4)

        self.assertTrue(self.a == self.b)
        self.assertFalse(self.c == self.a)
        self.assertTrue(self.d == CustomList())

    # Тестируем сравнение
    def test__ne__(self):
        self.b.append(4)

        self.assertFalse(self.a != self.b)
        self.assertTrue(self.c != self.a)
        self.assertTrue(self.d != self.c)

    # Тестируем сравнение
    def test__gt__(self):
        self.b.append(4)

        self.assertFalse(self.a > self.b)
        self.assertTrue(self.c > self.a)
        self.assertFalse(self.a > self.c)
        self.assertTrue(self.b > self.d)

    # Тестируем сравнение
    def test__ge__(self):
        self.b.append(4)

        self.assertTrue(self.a >= self.b)
        self.assertTrue(self.c >= self.a)
        self.assertFalse(self.a >= self.c)
        self.assertTrue(self.b >= self.d)


if __name__ == '__main__':
    unittest.main()
