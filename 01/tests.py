import unittest
from main import TicTac, validate_input


class TestTicTacMethods(unittest.TestCase):

    def test_start_game(self):
        play = TicTac()
        play.start_game()
        # Проверяем, что у нас создалась пустая таблица
        self.assertEqual(play.table, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    def test_validate_input(self):
        # Проверяем, что ввод всех верных кооринат верен
        for i in range(3):
            for j in range(3):
                self.assertTrue(validate_input(str(i) + ',' + str(j)))
        # Проверям разнообразные ошибки ввода
        self.assertFalse(validate_input('1, 1'))
        self.assertFalse(validate_input('1 1'))
        self.assertFalse(validate_input('11'))
        self.assertFalse(validate_input('3,1'))

    def test_check_winner(self):
        play = TicTac()
        # Проверяем, что работает выигрыш по строкам
        play.table = [[' ', ' ', 'O'], ['X', 'X', 'X'], ['O', 'O', ' ']]
        self.assertEqual(play.check_winner(), 'X')
        play.table = [[' ', ' ', 'X'], ['X', 'X', ' '], ['O', 'O', 'O']]
        self.assertEqual(play.check_winner(), 'O')
        play.table = [['X', 'X', 'X'], ['X', 'O', 'O'], ['O', 'O', ' ']]
        self.assertEqual(play.check_winner(), 'X')
        # Проверяем, что работает выигрыш по диагоналям
        play.table = [['O', ' ', ' '], ['X', 'O', 'X'], ['O', 'X', 'O']]
        self.assertEqual(play.check_winner(), 'O')
        play.table = [['O', ' ', 'X'], ['O', 'X', 'O'], ['X', 'X', ' ']]
        self.assertEqual(play.check_winner(), 'X')
        # Проверяем, что работает выигрыш по столбцам
        play.table = [['O', ' ', ' '], ['O', 'X', 'X'], ['O', 'X', ' ']]
        self.assertEqual(play.check_winner(), 'O')
        play.table = [['O', ' ', 'X'], ['O', 'O', 'X'], ['', 'O', 'X']]
        self.assertEqual(play.check_winner(), 'X')
        play.table = [['X', 'O', 'X'], ['O', 'O', 'X'], ['X', 'O', ' ']]
        self.assertEqual(play.check_winner(), 'O')
        # Проверяем, что может быть ничья
        play.table = [['O', 'X', 'O'], ['X', 'X', 'O'], ['0', 'O', 'X']]
        self.assertEqual(play.check_winner(), '')

    def test_input_step(self):
        play = TicTac()
        play.start_game()
        # Проверяем, что у нас определяет неправильный ввод
        self.assertEqual(play.input_step(0, '3,0'), 0)
        # Проверяем, что можем сделать ход в любую свободную ячейку, заполняя таблицу частично О, частично X
        for i in range(3):
            for j in range(3):
                if i <= 1 and j <= 1:
                    self.assertEqual(play.input_step(0, str(i) + ',' + str(j)), 1)
                    self.assertEqual(play.table[i][j], 'X')
                else:
                    self.assertEqual(play.input_step(1, str(i) + ',' + str(j)), 1)
                    self.assertEqual(play.table[i][j], 'O')
        # Проверяем, что у нас не вносятся изменения в уже заполненные ячейки
        self.assertEqual(play.input_step(0, '0,0'), 0)

    def test_match(self):
        play = TicTac()
        play.start_game()
        # Проверяем как работает метод основной игры и определяет ли все виды победы
        self.assertEqual(play.match(['1,1', '0,0', '0,1', '1,0', '2,1']), 0)
        play.start_game()
        self.assertEqual(play.match(['0,0', '2,0', '1,1', '2,2', '0,2', '2,1']), 1)
        play.start_game()
        self.assertEqual(play.match(['1,0', '0,0', '0,1', '0,2', '1,2', '1,1', '2,0', '2,1', '2,2']), 2)


if __name__ == '__main__':
    unittest.main()
