# . В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.
import  random
def less_2_4():
    sycret = int(random.randint(0, 100))
    print(sycret)
    i = 10
    while True:
        num = int(input('Введіть цифру: '))

        if i == 0:
            print('Перебільшена кількість спроб')
            break
        if num == sycret:
            print('Ти виграв')
            break
        else:
            if num < sycret:
                i  = i -1
                print(f'Ваше число меньше (Залишилось {i} спроб)')
            if num > sycret:
                i = i-1
                print(f'Ваше число більше (Залишилось {i} спроб)')


less_2_4()