#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from packet.display_trains import display_trains
from packet.get_train import get_train
from packet.select_trains import select_trains
import sys

def main():
    """
    Главная функция программы.
    """
    trains = []
    
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
           break
        elif command == 'add':
            train = get_train()
            trains.append(train) 
        elif command == 'list':
            display_trains(trains)
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            period = int(parts[1])
            # Выбрать поезда с заданным временем.
            selected = select_trains(trains, period)
            display_trains(selected)
        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <время> - запросить поезда с временем отправления;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()