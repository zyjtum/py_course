'''
    和静态方法比较类似，Python还可以在类中定义类方法
    类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象
    （类本身也是一个对象，有的地方也称之为类的元数据对象）
    通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象
'''


from time import time, localtime, sleep

class Clock:

    def __init__(self, hour=0, minute=0, second=0):
        self._hour=hour
        self._minute=minute
        self._second=second

    @classmethod
    def damn(cls):