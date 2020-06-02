'''
    之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。
    实际上，我们写在类中的方法并不需要都是对象方法，
    例如我们定义一个“三角形”类，通过传入三条边长来构造三角形，并提供计算周长和面积的方法，
    但是传入的三条边长未必能构造出三角形对象，
    因此我们可以先写一个方法来验证三条边长是否可以构成三角形，
    这个方法很显然就不是对象方法，因为在调用这个方法时三角形对象尚未创建出来
    (因为都不知道三条边能不能构成三角形)
    所以这个方法是属于三角形类而并不属于三角形对象的。我们可以使用静态方法来解决这类问题，

    declare a static method :
    after def __init__(self,*kwargs):
    @staticmethod
    def StaticMethod_Name(arguments WITHOUT self):
        function body


    distinguish instance method, class method and static method
'''

from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a=a
        self._b=b
        self._c=c


    @staticmethod
    def is_valid(a,b,c):     #self is not needed
            return a+b>c and b+c>a and a+c>b

    def perimeter(self):
        return self._a+self._b+self._c

    def area(self):
        half=self.perimeter() / 2
        return sqrt(half * (half-self._a) * (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 8
    if Triangle.is_valid(a,b,c):
        t=Triangle(a,b,c)
        print(t.perimeter())
        print(t.area())
    else:
        print('No triangle with these edges')


if __name__ == '__main__':
    main()
