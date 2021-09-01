#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ibegyourpardon
import random
import string


def random_integer(min_num: int = 0, max_num: int = 100, step: int = 1) -> int:
    # 返回随机整数
    # 如果 step 为2，整数
    return random.randrange(min_num, max_num, step)


def random_fload(min_num: int = 0, max_num: int = 100) -> float:
    # 返回随机浮点数
    return random.uniform(min_num, max_num)


def simple_random_string(num: int = 8) -> str:
    # string.printable=string.ascii_letters(大小写）+string.digits(数字)+string.punctuation(标点符号）+string.whitespace(空白符号）
    x = string.ascii_letters
    result = ''
    for i in range(num):
        result += random.choice(x)
    return result


def complex_random_string(num: int = 8) -> str:
    x = string.printable
    result = ''
    for i in range(num):
        result += random.choice(x)
    return result
