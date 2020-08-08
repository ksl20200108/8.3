# from utils import Singleton


# class Singleton1(object):
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#
#         if cls.__instance is None:
#             cls.__instance = super(Singleton1, cls).__new__(cls)
#         return cls.__instance


class StopMine():
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)

    def __init__(self):
        if not hasattr(self, "h"):
            self.h = 0
        if not hasattr(self, "mine_h"):
            self.mine_h = 1
        if not hasattr(self, "ip"):
            self.ip = None
