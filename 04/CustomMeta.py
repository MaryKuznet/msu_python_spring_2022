def setattr(self, name, value):
    if name in self.__dict__ or name in self.__class__.__dict__:
        self.__dict__[name] = value
    else:
        self.__dict__['custom_' + name] = value


class CustomMeta(type):
    def __new__(mcs, name, bases, class_dict):
        new_dict = {}
        for name_, value in class_dict.items():
            if name_[:2] != '__':
                new_dict['custom_' + name_] = value
            else:
                new_dict[name_] = value
        return super(CustomMeta, mcs).__new__(mcs, name, bases, new_dict)

    def __init__(cls, name, bases, class_dict):
        cls.__setattr__ = setattr
        super(CustomMeta, cls).__init__(name, bases, class_dict)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
