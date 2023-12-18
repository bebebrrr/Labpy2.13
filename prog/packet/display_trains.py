#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def display_trains(punkts):
    """
    Отобразить список поездов.
    """
    # Проверить, что список поездов не пуст.
    if punkts:
       # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 17
        )
        print(line)
        print('| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
            "№",
            "Номер поезда",
            "Пункт назначения",
            "Время отправления"
            )
        )
        print(line)
        # Вывести данные о всех поездах.
        for idx, train in enumerate(punkts, 1):
            print('| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                idx,
                train.get('nomer', ''),
                train.get('punkt', ''),
                train.get('time', 0)
                )
            )
        print(line)
       
    else:
        print("Список поездов пуст.")