#!/usr/bin/python
## -*- coding: utf-8 -*-

"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def get_work_by_age(age):
    if age <= 6:
        return "учиться в детском саду"
    elif 7 <= age <= 18:
        return "учиться в школе"
    elif 18 <= age <= 25:
        return "учиться в ВУЗе"
    else:
        return "работать"

def main():
    age = int(input("Сколько вам лет? "))
    work = get_work_by_age(age)
    print(f"ты должен {work}")

if __name__ == "__main__":
    main()
