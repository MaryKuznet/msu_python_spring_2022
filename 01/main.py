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
    def input_step(self, player, step=tuple()):
        if step:
            x, y = step
        else:
            x, y = map(int, input('{}-й игрок введите координаты в виде "x,y":'.format(player + 1)).split(','))
        if self.table[x][y] == ' ':
            self.table[x][y] = 'X' * (not player) + 'O' * player
        else:
            print('Это поле уже было использовано, попробуй снова')
            return 0
        return 1

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


if __name__ == "__main__":

    # Начало игры
    game = TicTac()
    game.start_game()
    game.show_board()

    # Основная игра
    victory = ''
    i = 0
    while victory == '' and i < 9:
        if game.input_step(i % 2):
            i += 1
        game.show_board()
        if i > 4:
            victory = game.check_winner()

# Вывод победителя
    if victory == 'X':
        print('Победил первый игрок! Поздравляем!')
    elif victory == 'O':
        print('Победил второй игрок! Поздравляем!')
    else:
        print('Победила дружба игрок! Поздравляем!')
