def area(a, b): 
    '''
    Вычисляет площадь прямоугольника с длиной стороны a и шириной b.

    Параметры:
    - a (float): Длина прямоугольника.
    - b (float): Ширина прямоугольника.

    Возвращает:
    - float: Площадь прямоугольника.

    Пример использования:
    result = area(5, 10)
    print(result)  # Вывод: 50
    '''
    return a * b 
  
def perimeter(a, b): 
    '''
    Вычисляет периметр прямоугольника с длиной стороны a и шириной b.

    Параметры:
    - a (float): Длина прямоугольника.
    - b (float): Ширина прямоугольника.

    Возвращает:
    - float: Периметр прямоугольника.

    Пример использования:
    result = perimeter(5, 10)
    print(result)  # Вывод: 30
    '''
    return 2 * (a + b)
