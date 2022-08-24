
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
