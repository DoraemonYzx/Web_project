#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: test_demo_pytest2.py
@time: 2020/01/21
"""
import pytest
"""
    数据驱动：经典案例
    @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
    在这里，@parametrize装饰器定义了三个不同的(test_input,expected) 元组，以便该test_eval函数依次使用它们运行三次
"""


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
