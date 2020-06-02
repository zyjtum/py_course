"""
    public, private or protected?
    in python, only two categories here, private and public
    defaultly speaking, public
    adding __  as prefix makes the method private
    在method 和variable前面都可以加_设为private， 但是想要调用的话，ObjName._ClassName__AttributeName/MethodName
"""


class Test:
    def __init__(self, foo,loo):
        self.__foo=foo
        self.loo=loo

    def bar(self):
        print(self.__foo)
        print('__bar func called')

    def __fuck(self):
        print(self.loo)
        print('fuck_func called')


def main():
    test = Test('hello')
    test.__bar()        #AttributeError: 'Test' object has no attribute '__bar'
    test.bar()    #obj._ClassName__MethodName()
    print(test._Test__foo)


if __name__ == '__main__':
    main()
