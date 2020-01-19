#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: run_all_case.py
@time: 2020/1/14
"""
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from common .HTMLTestRunner_cn import HTMLTestRunner
import time

test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern="test*.py")

if __name__ == '__main__':
    report_dir = './test_report'
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # report_name = report_dir+'/'+now+'result.html'
    report_name = report_dir+'/'+'result.html'
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title="Demo测试报告",
                                description="！！！！",
                                retry=1)
        runner.run(discover)
    f.close()
