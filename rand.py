#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ibegyourpardon
import random


def random_integer(min_num: int = 0, max_num: int = 100, step: int = 1):
    # 返回随机整数
    # 如果 step 为2，整数
    return random.randrange(min_num, max_num, step)


def random_fload(min_num: int = 0, max_num: int = 100):
    # 返回随机浮点数
    return random.uniform(min_num, max_num)


def random_string(num: int = 8):
    safe_string = 'abcdefghijklmnopqrstuvwxyz'
