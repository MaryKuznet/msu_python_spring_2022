
class CustomList(list):

    def __str__(self):
        return super.__str__(self) + ' ' + str(sum(self))

    # Функция, делающая одинаковый размер у 2-х списках
    @staticmethod
    def one_size(list1, list2):
        while len(list1) > len(list2):
            list2.append(0)
        while len(list1) < len(list2):
            list1.append(0)
        return list1, list2

    def __add__(self, other: list):
        copy, other = CustomList.one_size(self.copy(), other.copy())
        for i in range(len(copy)):
            copy[i] += other[i]
        return CustomList(copy)

    def __sub__(self, other: list):
        copy, other = CustomList.one_size(self.copy(), other.copy())
        for i in range(len(copy)):
            copy[i] -= other[i]
        return CustomList(copy)

    def __radd__(self, other: list):
        copy, other = CustomList.one_size(self.copy(), other.copy())
        for i in range(len(copy)):
            copy[i] += other[i]
        return CustomList(copy)

    def __iadd__(self, other: list):
        return self.__add__(other)

    def __rsub__(self, other: list):
        copy, other = CustomList.one_size(self.copy(), other.copy())
        for i in range(len(copy)):
            other[i] -= copy[i]
        return CustomList(other)

    def __isub__(self, other: list):
        return self.__sub__(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)
