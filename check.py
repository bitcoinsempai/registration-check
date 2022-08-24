# Надо проверить данные из файла, для каждой строки:
# присутсвуют все три поля
# поле имени содержит только буквы
# поле email содержит @ и .
# поле возраст является числом от 10 до 99
# В результате проверки нужно сформировать два файла
# registrations_good.log для правильных данных, записывать строки как есть
# registrations_bad.log для ошибочных, записывать строку и вид ошибки.
# Для валидации строки данных написать метод, который может выкидывать исключения:
# НЕ присутсвуют все три поля: ValueError
# поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# поле email НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# поле возраст НЕ является числом от 10 до 99: ValueError Вызов метода обернуть в tr`y-except.


# поле имени содержит НЕ только буквы:
class NotNameError(Exception):
    pass


# поле email НЕ содержит @ и .(точку):
class NotEmailError(Exception):
    pass


def reg(line):
    lines = line.split()

    # проверка на три поля
    if len(lines) < 1:
        raise ValueError(f'НЕ присутсвуют все три поля, строка № {line_number}')

    # проверка на возраст
    age = int(lines[2])
    if 10 <= age <= 99:
        pass
    else:
        raise ValueError(f'Поле возраст НЕ является числом от 10 до 99')

    # проверка на отсутствие трех полей
    elem_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '?', '@', '.']
    for _ in lines[0]:
        if _ in elem_list:
            raise NotNameError


# проверка на имейл
def mail(line):
    name, email, age = line.split()

    mail_list = '@' and '.' in email
    if mail_list is True:
        pass
    else:
        raise NotEmailError

# ввел эту переменную, чтобы видно было на какой строке отсутствуют все три поля, для удобства
line_number = 0
with open('registrations_.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line[:-1]
        line_number += 1
        try:
            reg(line)
            mail(line)
            log_good = open('registrations_good.log', 'a+')
            log_good.write(f'{line} \n')
            log_good.close()

        except ValueError as exc:
            with open('registrations_bad.log', 'a+') as log_bad:
                log_bad.write(f'Ошибка в строке [{line}], {exc} \n')

        except IndexError as exc:
            with open('registrations_bad.log', 'a+') as log_bad:
                log_bad.write(f'Error in {line}, param {exc} \n')

        except NotEmailError as exc:
            with open('registrations_bad.log', 'a+') as log_bad:
                log_bad.write(f'поле возраст НЕ является числом от 10 до 99, в строке {line} \n')

        except NotNameError as exc:
            with open('registrations_bad.log', 'a+') as log_bad:
                log_bad.write(f'Поле имени содержит НЕ только буквы, {line} \n')