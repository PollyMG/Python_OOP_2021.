class AttrDict(object):
    def __init__(self, init=None):
        init = init if init is not None else {}
        self.__dict__ = init

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value