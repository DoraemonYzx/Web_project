#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: 123.py
@time: 2020/01/17
"""


class Dog:

    tricks = "123"

    def __init__(self, name):
        self.name = name

    def add(self, trick):
        print(self.tricks)
        self.tricks = trick
        print(self.tricks)


if __name__ == "__main__":
    d = Dog("1")
    e = Dog("2")
    d.add("4")
    e.add("5")
    print(d.tricks, e.tricks)


