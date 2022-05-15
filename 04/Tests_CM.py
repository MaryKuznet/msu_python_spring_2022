import unittest
from CustomMeta import CustomClass


class TestCustomMeta(unittest.TestCase):

    # Проверяем, что наши атрибуты видоизменились
    def test_new_attributes(self):
        inst_1 = CustomClass()
        inst_2 = CustomClass(1)

        self.assertEqual(inst_1.custom_x, 50)
        self.assertEqual(inst_2.custom_x, 50)

        self.assertEqual(inst_1.custom_val, 99)
        self.assertEqual(inst_2.custom_val, 1)

        self.assertEqual(inst_1.custom_line(), 100)
        self.assertEqual(inst_2.custom_line(), 100)

        self.assertEqual(str(inst_1), "Custom_by_metaclass")
        self.assertEqual(str(inst_2), "Custom_by_metaclass")

        self.assertEqual(CustomClass.custom_x, 50)

        inst_1.custom_x = 12
        self.assertEqual(inst_1.custom_x, 12)
        self.assertEqual(inst_2.custom_x, 50)

        inst_2.custom_val = 2
        self.assertEqual(inst_1.custom_val, 99)
        self.assertEqual(inst_2.custom_val, 2)

        # Тест нового атрибута
        inst_1.dynamic = "added later"
        inst_2.dynamic = "added later"
        self.assertEqual(inst_1.custom_dynamic, "added later")
        self.assertEqual(inst_2.custom_dynamic, "added later")

    # Проверяем, что атрибуты в старом виде вызывают ошибку
    def test_old_attributes(self):
        inst_1 = CustomClass()
        inst_2 = CustomClass(1)

        with self.assertRaises(AttributeError):
            inst_1.x

        with self.assertRaises(AttributeError):
            inst_2.val

        with self.assertRaises(AttributeError):
            inst_1.line()

        with self.assertRaises(AttributeError):
            inst_2.yyy

        with self.assertRaises(AttributeError):
            CustomClass.x

        # Тест нового атрибута
        inst_1.dynamic = "added later"
        inst_2.dynamic = "added later"

        with self.assertRaises(AttributeError):
            inst_1.dynamic

        with self.assertRaises(AttributeError):
            inst_2.dynamic


if __name__ == '__main__':
    unittest.main()
