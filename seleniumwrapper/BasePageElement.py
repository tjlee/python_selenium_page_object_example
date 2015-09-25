__author__ = 'v.chernov'


class BasePageElement(object):
    def __get__(self, obj, cls=None):
        pass

    def __delete__(self, obj):
        pass