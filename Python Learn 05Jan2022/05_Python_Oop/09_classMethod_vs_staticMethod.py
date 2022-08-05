
'''Maybe a bit of example code will help: Notice the difference in the call signatures of foo, class_foo and static_foo:'''

class A(object):
    def foo(self, x):
        print(f"executing foo({self}, {x})")

    @classmethod
    def class_foo(cls, x):
        print(f"executing class_foo({cls}, {x})")

    @staticmethod
    def static_foo(x):
        print(f"executing static_foo({x})")

a = A()
a.foo(1)
a.class_foo(1)
a.static_foo(1)