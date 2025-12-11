import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да',
           'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего',
           'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова',
           'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет',
           'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']


def choice(answers):
    random_answer = answers[random.randint(0, len(answers)-1)]
    return random_answer

def magic_ball():
    global answer_string
    while True:
        answer_string = input('Что Вы хотели бы узнать? ')
        if is_valid_answer(answer_string):
            print('Хм... Давайте подумаем..')
            print(choice(answers))
            user_input = input('Хотите задать еще вопрос? (да - д, нет - н) ')
            if user_input == 'д':
                magic_ball()
                return
            elif user_input == 'н':
                print('Возвращайся, если возникнут вопросы!')
                return
        else:
            print('Введите корректный вопрос.')
            answer_string = input('Что Вы хотели бы узнать? ')
        


def is_valid_answer(answer):
    return answer.isalpha()

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
username = input('Как Вас зовут? ')
print(f'Привет, {username}')
magic_ball()