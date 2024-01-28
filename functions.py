def hello(name):
    return f"Hello, {name}"


def salary(hours, salary_per_hour):
    '''
    Функция возвращает общую зарплату
    :param hours: кол-во часов работы
    :param salary_per_hour: зарплата в час
    :return: общая зп
    '''
    k = 1
    return hours * salary_per_hour * k
