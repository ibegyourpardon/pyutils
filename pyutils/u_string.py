#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ibegyourpardon


def convert_str_to_list(original: str, u_seperator: str = ',') -> list:
    # 字符串转换成 list，可以指定分隔符
    result = original.split(u_seperator)
    return result


def get_common_prefix_of_strings(str_list: list) -> str:
    # 获取多个字符串的公共前缀
    commons = []
    for i in range(min(len(s) for s in str_list)):
        common = str_list[0][i]
        for c in str_list[1:]:
            if c[i] != common:
                return ''.join(commons)
        commons.append(common)
    return ''.join(commons)


def get_common_suffix_of_strings(str_list: list) -> str:
    """
    Return common suffix of the stings
        >>> common_suffix(['dabc', '1abc'])
        'abc'
    """
    commons = []
    for i in range(min(len(s) for s in str_list)):
        common = str_list[0][-i-1]
        for c in str_list[1:]:
            if c[-i-1] != common:
                return ''.join(reversed(commons))
        commons.append(common)
    return ''.join(reversed(commons))


def sort(s, reverse=False):
    """
    Sort given string by ascending order.
    If reverse is True, sorting given string by descending order.
    """
    return ''.join(sorted(s, reverse=reverse))
