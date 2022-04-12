import unittest
from faker import Faker
from unittest.mock import patch
from main import parse_html


class TestParseHtml(unittest.TestCase):

    @patch('main.foo', return_value=None)
    def test_open_tag_callback(self, foo_mock):
        parse_html('Текст', foo_mock, len, len)
        self.assertEqual(foo_mock.call_count, 0)
        foo_mock.assert_not_called()

        parse_html('<p><i>Текст</i></p>', foo_mock, len, len)
        self.assertEqual(foo_mock.call_count, 2)
        foo_mock.assert_any_call('<p>')
        foo_mock.assert_any_call('<i>')

        parse_html('<m> Tекст', foo_mock, len, len)
        self.assertEqual(foo_mock.call_count, 3)
        foo_mock.assert_any_call('<m>')

        fake = Faker()
        parse_html(fake.bothify(text="<a>?? ????? <?> ? <?>? </a>"), foo_mock, len, len)
        self.assertEqual(foo_mock.call_count, 6)

    @patch('main.foo', return_value=None)
    def test_close_tag_callback(self, foo_mock):
        parse_html('Текст', len, len, foo_mock)
        self.assertEqual(foo_mock.call_count, 0)
        foo_mock.assert_not_called()

        parse_html('<a>Текст', len, len, foo_mock)
        self.assertEqual(foo_mock.call_count, 0)
        foo_mock.assert_not_called()

        parse_html('<m>Tекст1</m><p>Tекст_2<p>Tекст_3</p>', len, len, foo_mock)
        self.assertEqual(foo_mock.call_count, 2)
        foo_mock.assert_any_call('</p>')
        foo_mock.assert_any_call('</m>')

    @patch('main.foo', return_value=None)
    def test_data_callback(self, foo_mock):
        fake = Faker()
        parse_html(fake.text(max_nb_chars=50), len, foo_mock, len)
        self.assertEqual(foo_mock.call_count, 0)
        foo_mock.assert_not_called()

        parse_html('<m>Tекст', len, foo_mock, len)
        self.assertEqual(foo_mock.call_count, 1)
        foo_mock.assert_any_call('Tекст')

        parse_html('<m>Tекст1</m><p>Tекст_2<p>Tекст_3</p>', len, foo_mock, len)
        self.assertEqual(foo_mock.call_count, 4)
        foo_mock.assert_any_call('Tекст1')
        foo_mock.assert_any_call('Tекст_3')
        foo_mock.assert_any_call('Tекст_2<p>Tекст_3</p>')

        parse_html(fake.bothify(text="<a>?? ????? <?> ??? </a>"), len, foo_mock, len)
        self.assertEqual(foo_mock.call_count, 6)


if __name__ == '__main__':
    unittest.main()
