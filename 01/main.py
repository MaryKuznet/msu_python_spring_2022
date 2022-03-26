def validate_input(string):
    if len(string) == 3:
        if string[1] == ',' and string[0] in {'0', '1', '2'} and string[2] in {'0', '1', '2'}:
            return True
    return False


class TicTac:
    def __init__(self):
        self.table = None

    # Вывод игрового поля
    def show_board(self):
        print('{:^19}'.format('Table'))
        for _i in range(3):
            print('_' * 19)
            print('|', end='')
            for j in range(3):
                print("{:^5}".format(self.table[_i][j]), end='|')
            print()
        print('_' * 19)

    # Ход 1 или 2 игрока, проверка можно ли введенным образом сделать ход и сохранение хода
    def input_step(self, player, string=''):
        if not string:
            string = input('{}-й игрок введите координаты в виде "x,y":'.format(player + 1))
        if validate_input(string):
            x, y = map(int, string.split(','))
            if self.table[x][y] == ' ':
                self.table[x][y] = 'X' * (not player) + 'O' * player
                return 1
            print('Это поле уже было использовано, попробуйте снова')
            return 0
        print('Неверный формат ввода, попробуйте снова')
        return 0

    # Начало игры
    def start_game(self):
        print('Добро пожаловать в игру крестики-нолики!')
        print('Каждый ваш ход это ввод координаты места, где вы хотите поставить X или O')
        print('Пример: "0,1" означает 0-ю строку и 1-й столбец (нумерация с нуля)')
        # Создание списка хранящего информацию о состоянии игрового поля
        self.table = [[' ' for _i in range(3)] for _j in range(3)]

    # Проверка не победил ли кто-то
    def check_winner(self):
        for letter in ['X', 'O']:
            # Проверка победы по строкам
            for _i in range(3):
                if len(set(self.table[_i])) == 1 and self.table[_i][0] == letter:
                    return letter
            # Проверка победы по столбцам
            for j in range(3):
                if self.table[0][j] == self.table[1][j] == self.table[2][j] == letter:
                    return letter
            # Проверка победы по диагоналям
            if self.table[0][0] == self.table[1][1] == self.table[2][2] == letter:
                return letter
            if self.table[2][0] == self.table[1][1] == self.table[0][2] == letter:
                return letter
        return ''

    # Основная игра
    def match(self, list_of_moves=tuple(['', '', '', '', '', '', '', '', ''])):
        victory = ''
        i = 0
        while victory == '' and i < 9:
            if self.input_step(i % 2, list_of_moves[i]):
                i += 1
            self.show_board()
            if i > 4:
                victory = self.check_winner()

        # Вывод победителя
        if victory == 'X':
            print('Победил первый игрок! Поздравляем!')
            return 0
        if victory == 'O':
            print('Победил второй игрок! Поздравляем!')
            return 1
        print('Победила дружба игрок! Поздравляем!')
        return 2


if __name__ == "__main__":

    # Начало игры
    game = TicTac()
    game.start_game()
    game.show_board()
    game.match()
