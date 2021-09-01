#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ibegyourpardon

def sort_by_field_in_dict(param: dict) -> dict:
    # 给字典按照value按照从大到小排序
    new_dict = sorted(param.iteritems(), key=lambda d: d[1], reverse=True)
    return new_dict


def sort_by_field(param: dict, field: str) -> dict:
    # 按照list中的字典的某key排序:
    """
            s=[
        {"no":28,"score":90},
        {"no":25,"score":90},
        {"no":1,"score":100},
        {"no":2,"score":20},

        ]
    """
    new_s = sorted(param, key=lambda e: e.__getitem__(field))
    return new_s


def sort_by_fields(param: dict, fields: list) -> dict:
    # 多级排序,先按照score，再按照no排序
    new_s_2 = sorted(param, key=lambda e: (e.__getitem__('score'), e.__getitem__('no')))
    #todo
    return new_s_2