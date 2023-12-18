#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select_trains(punkts, period):
    """
    Выбрать поезда с заданным временем.
    """
    result = []
    for van in punkts:
        if van.get('time', 0) >= period:
            result.append(van) 
   # Возвратить список выбранных поездов.
    return result
