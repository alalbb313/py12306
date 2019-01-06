from py12306 import config
import functools


def singleton(cls):
    """
    将一个类作为单例
    来自 https://wiki.python.org/moin/PythonDecoratorLibrary#Singleton
    """

    cls.__new_original__ = cls.__new__

    @functools.wraps(cls.__new__)
    def singleton_new(cls, *args, **kw):
        it = cls.__dict__.get('__it__')
        if it is not None:
            return it

        cls.__it__ = it = cls.__new_original__(cls, *args, **kw)
        it.__init_original__(*args, **kw)
        return it

    cls.__new__ = singleton_new
    cls.__init_original__ = cls.__init__
    cls.__init__ = object.__init__

    return cls


# 座位
def get_seat_number_by_name(name):
    return config.SEAT_TYPES[name]


def get_seat_name_by_number(number):
    return [k for k, v in config.SEAT_TYPES.items() if v == number].pop()


# def test: