def new_setattr(self, name, value):
    if not (name in self.__dict__ or name in self.__class__.__dict__) \
            and name[:2] != '__' and name[-2:] != '__':
        name = 'custom_' + name
    object.__setattr__(self, name, value)


class CustomMeta(type):
    def __new__(cls, name, bases, class_dict):
        new_dict = {}
        for name_, value in class_dict.items():
            if name_[:2] != '__' and name_[-2:] != '__':
                new_dict['custom_' + name_] = value
            else:
                new_dict[name_] = value
        return super().__new__(cls, name, bases, new_dict)

    def __init__(cls, name, bases, class_dict):
        cls.__setattr__ = new_setattr
        super().__init__(name, bases, class_dict)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    @staticmethod
    def line():
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
