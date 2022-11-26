import logging

logging.basicConfig(level = logging.INFO, filename = "logger.log", format = "%(asctime)s - %(levelname)s - %(message)s")

banknotes = [1, 2, 4, 8, 16, 32, 64] #список с достоинством банкнот
bank= [0, 0, 0, 0, 0, 0, 0] #список количества банкнот


while True: #цикл обработки ввода
    try:
        summ = int(input("введите сумму натуральным числом больше 0: "))
        assert summ > 0
        logging.info(f'пользователь ввел сумму: {summ}')
        break
    except AssertionError:
        logging.error(f'некорректный ввод')
        print("некорректный ввод\nповторите попытку")
    except ValueError:
        logging.error(f'некорректный ввод')
        print("некорректный ввод\nповторите попытку")

#объявление вспомогательной переменной
step = 6
     
while summ > 0: #цикл подсчета
    pos = banknotes[step]
    bank[step] = summ // int(pos)
    if bank[step] != 0:
        summ = summ % int(pos)
    step -= 1

logging.info('произведен расчет')

for i in range(len(bank)): #вывод ответа
    if bank[i] != 0:
        print(f'количество купюр стоимостью {banknotes[i]}: {bank[i]}')
        logging.info(f'количество купюр стоимостью {banknotes[i]}: {bank[i]}')
    else:
        pass

logging.info('работа программы завершена')