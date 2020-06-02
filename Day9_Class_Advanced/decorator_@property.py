'''
    take home message
    @property
    @attribute.setter
    @attribute.getter
    private attribute and access to them using '_' as prefix of attribute name
    type of an attribute is the type of the returned obj
'''


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器，getter method
    @property
    def name(self):
        print('my name is %s' % self._name)
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 setter method
    @age.setter
    def age(self,age):
        self._age=age

    #修改器 setter method
    @name.setter
    def name(self,name):
        self._name=name

    def play(self):
        if self._age <=16:
            print('{} is playing chess'.format(self._name))
        else:
            print('{} is playing poker'.format(self._name))
        return 0


def main():
    person=Person('Tony', 15)
    person.name    # str obj,not a method
    #print(type(person.name))
    person.play()
    #print(type(person.play()))
   # person.age()
    person.name='Steve'
    person.age = 22
    person.play()

if __name__ == '__main__':
    main()