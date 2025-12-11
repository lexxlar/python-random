import random

def is_valid(n, border):
    return n.isdigit() and 1 <= int(n) <= border

print('Добро пожаловать в числовую угадайку!')

def game():
    # Запрашиваем границу один раз в начале игры
    while True:
        user_border = input('Введите целое число правой границы диапазона: ')
        if user_border.isdigit():
            user_border = int(user_border)
            break
        else:
            print('Введите корректное целое число.')
    
    random_number = random.randint(1, user_border)
    count_attempts = 0
    
    # Основной игровой цикл
    while True:
        user_num = input(f'Введите число от 1 до {user_border}: ')
        
        if is_valid(user_num, user_border):
            user_num = int(user_num)
            count_attempts += 1
            
            if user_num < random_number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif user_num > random_number:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                print(f'Количество сделанных попыток: {count_attempts}')
                
                while True:
                    user_input = input('Хотите ли продолжить игру? (да - д, нет - н): ').lower()
                    if user_input in ['д', 'y', 'yes', 'да']:
                        game()  # Рекурсивный вызов для новой игры
                        return
                    elif user_input in ['н', 'n', 'no', 'нет']:
                        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                        return
                    else:
                        print('Пожалуйста, введите "д" или "н"')
        else:
            print(f'А может быть все-таки введем целое число от 1 до {user_border}?')

game()