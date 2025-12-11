import random

word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'земля', 'машина', 'бог']

def get_word():
    return random.choice(word_list) # выбираем случайное слово из списка слов

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def update_word_completion(word, word_completion, guessed_letter):
    """Обновляет word_completion, заменяя _ на угаданную букву"""
    word_list = list(word_completion)  # превращаем строку в список
    for i in range(len(word)):
        if word[i] == guessed_letter:
            word_list[i] = guessed_letter
    return ''.join(word_list)  # собираем список обратно в строку

def play(word):
    word_completion = word[0] + (len(word) - 2) * '_' + word[-1]  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word)
    print(f'Искомое слово: {word_completion}')
    
    while tries != 0:
        # Проверка на валидность введенных символов
        user_input = input('Введите букву или слово целиком: ')
        if not user_input.isalpha():
            print('Введите корректное слово или букву!')
            continue
        if user_input in guessed_letters or user_input in guessed_words:
            print('Данное слово или буква уже были.')
            continue
        
        # Проверка на совпадение со слово, при вводе пользователем слова
        if len(user_input) > 1:
            if user_input == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
            else:
                tries -= 1
                print(display_hangman(tries))
                print(f'Неверно! Осталось {tries} попыток!')
                guessed_words.append(user_input)
                print(f'Названные буквы и слова {guessed_letters}')
        else:
            # Проверка, есть ли буква в слове
            if user_input in word:
                print(f'Вы угадали букву "{user_input}"!')
                guessed_letters.append(user_input)
                word_completion = update_word_completion(word, word_completion, user_input)
                print(f'Искомое слово: {word_completion}')
                print(f'Названные буквы и слова {guessed_letters}')
                
                # Проверка на победу
                if '_' not in word_completion:
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    break
            else:
                tries -= 1
                print(display_hangman(tries))
                print(f'Неверно! Осталось {tries} попыток!')
                guessed_letters.append(user_input)
                print(f'Искомое слово: {word_completion}')
    else:
        print('К сожалению, вы проиграли..')
        print(f'Загаданное слово было: {word}')      
        
word = get_word()
play(word)