def func(a, b):
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        return a + b
    else:
        return 'Ошибка'

