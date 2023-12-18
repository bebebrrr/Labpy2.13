#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_train():
    """
    Запросить данные о поездах.
    """
    nomer = input("Номер поезда? ")
    punkt = input("Пункт назначения? ")
    time = int(input("Время отправления? "))
    # Создать словарь.
    return {
            'nomer': nomer,
            'punkt': punkt,
            'time': time,
        }