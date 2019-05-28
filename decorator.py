#!/usr/local/bin/python3.7

def inspect(my_func):
    def wrapped_func(*args, **kargs):
        print(f"running {my_func.__name__}")
        val = my_func(*args, **kargs)
        print(val)
        return val
    return wrapped_func

@inspect
def combine(a, b):
    return a + b

# @classmethod
# transform a method into a class method

class User:
    base_url = "https://example.com/api"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def query(cls, query_string):
        return cls.base_url + '?' + query_string

    @staticmethod
    def name():
        return 'kevin becon'

    @property
    def full_name(self):
        print(f"{self.first_name} {self.last_name}")
