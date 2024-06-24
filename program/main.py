import requests

def perimeter_square(side):
    if isinstance(side, (int, float)) and side >= 0:
        return side * 4
    else:
        return 'Некоректный ввод'

def area_square(side):
    if isinstance(side, (int, float)) and side >= 0:
        return side ** 2
    else:
        return 'Некоректный ввод'
def fio(fio_list):
    initials = ''.join([x[0] for x in fio_list])
    return initials


