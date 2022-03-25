import unittest
from main import TicTac


class TestTicTacMethods(unittest.TestCase):

    def test_start_game(self):
        play = TicTac()
        play.start_game()
        # Проверяем, что у нас создалась пустая таблица
        self.assertEqual(play.table, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    def test_check_winner(self):
        play = TicTac()
        # Проверяем, что работает выигрыш по строке
        play.table = [[' ', ' ', 'O'], ['X', 'X', 'X'], ['O', 'O', ' ']]
        self.assertEqual(play.check_winner(), 'X')
        # Проверяем, что работает выигрыш по диагонали
        play.table = [['O', ' ', ' '], ['X', 'O', 'X'], ['O', 'X', 'O']]
        self.assertEqual(play.check_winner(), 'O')
        # Проверяем, что работает выигрыш по столбцам
        play.table = [['O', ' ', ' '], ['O', 'X', 'X'], ['O', 'X', ' ']]
        self.assertEqual(play.check_winner(), 'O')
        # Проверяем, что может быть ничья
        play.table = [['O', 'X', 'O'], ['X', 'X', 'O'], ['0', 'O', 'X']]
        self.assertEqual(play.check_winner(), '')

    def test_input_step(self):
        play = TicTac()
        play.start_game()
        # Проверяем, что можем сделать ход в любую свободную ячейку, заполняя таблицу частично О, частично X
        for i in range(3):
            for j in range(3):
                if i <= 1 and j <= 1:
                    self.assertEqual(play.input_step(0, (i, j)), 1)
                    self.assertEqual(play.table[i][j], 'X')
                else:
                    self.assertEqual(play.input_step(1, (i, j)), 1)
                    self.assertEqual(play.table[i][j], 'O')
        # Проверяем, что у нас не вносятся изменения в уже заполненные ячейки
        self.assertEqual(play.input_step(0, (0, 0)), 0)


if __name__ == '__main__':
    unittest.main()
