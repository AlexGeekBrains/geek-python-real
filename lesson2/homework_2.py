"""
1. Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2
"""
import math


def type_of():
    print(type(15 * 3))
    print(type(15 / 3))
    print(type(15 // 3))
    print(type(15 ** 3))


# type_of()


"""
2,3. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками 
(добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. 
Главное: дополнить числа до двух разрядов нулём!
"""


def temperature_alert():
    message = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    i = 0
    while i < len(message):
        if message[i].isdigit() or message[i][1:].isdigit():
            sign = message[i][0] if not message[i][0].isdigit() else ''
            message[i] = sign + '{:02}'.format(int(message[i]))
            message.insert(i + 1, '"')
            message.insert(i, '"')
            i += 2
            continue
        i += 1
    print(' '.join(message))


# temperature_alert()


"""
4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' 
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. 
Можно ли при этом не создавать новый список?
"""


def names():
    stuff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
    for i in stuff:
        print(f'Привет {i.split()[-1].capitalize()}')


# names()


"""
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, 
цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). 
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, 
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, 
новый список не создавать (доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""


def products():
    prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78,
              48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

    for i in prices:
        r = math.floor(i * 100 // 100)
        k = math.floor(i * 100 % 100)
        print(f'{r:02} руб {k:02} коп, ', end='')

    old_id = id(prices)
    prices.sort()
    new_id = id(prices)
    print(old_id == new_id)

    desc_prices = prices[::-1]
    print(desc_prices)
    print(desc_prices[4::-1])


products()
