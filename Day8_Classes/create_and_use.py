class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, subject_name):
        print('Line 1: %s is learning %s' % (self.name, subject_name))
        print('Line 2: {} is studying {}'.format(self.name, subject_name))
        print('Line 3: {one} is studying {two}'.format(one=self.name, two=subject_name))

    def watch_av(self):
        if self.age < 18:
            print('%s can only watch Batman' % self.name)
        else:
            print('%s is watching adult video'% self.name)


def main():
    stu1 = Student('tony', 19)
    stu1.study("Python Programming")
    stu2 = Student("Steve", 16)
    stu2.study("C++ programming")
    stu2.watch_av()


if __name__ == "__main__":
    main()
