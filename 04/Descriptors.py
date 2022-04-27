class Integer:
    def __init__(self):
        self.val = None

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, obj, value):
        if isinstance(value, int):
            self.val = value
        else:
            raise TypeError('Not Integer')

    def __del__(self):
        del self.val


class String:
    def __init__(self):
        self.val = None

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, obj, value):
        if isinstance(value, str) and 0 < len(value) < 10:
            self.val = value
        elif not isinstance(value, str):
            raise TypeError('Not String')
        elif len(value) >= 10:
            raise ValueError('Too long')
        else:
            raise ValueError('Too small')

    def __del__(self):
        del self.val


class PositiveInteger:
    def __init__(self):
        self.val = None

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, obj, value):
        if isinstance(value, int) and value > 0:
            self.val = value
        elif not isinstance(value, int):
            raise TypeError('Not Integer')
        else:
            raise ValueError('Not positive')

    def __del__(self):
        del self.val


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self):
        pass
