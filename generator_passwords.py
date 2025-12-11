import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

yes = ['д', 'y']

num_passwrds = int(input('Введите количество генерируемых паролей: '))
len_passwd = int(input('Введите длину пароля: '))
need_digits = input('Включать цифры? (д - да, н - нет) ')
need_uppercase = input('Включать прописные буквы? (д - да, н - нет) ')
need_lowercase = input('Включать строчные буквы? (д - да, н - нет) ')
need_punctuation = input('Включать спец.символы? (д - да, н - нет) ')
delete_symbols = input('Исключать однозначные символы? (д - да, н - нет) ')

if need_digits.lower() in yes:
    chars += digits
if need_uppercase.lower() in yes:
    chars += uppercase_letters
if need_lowercase.lower() in yes:
    chars += lowercase_letters
if need_punctuation.lower() in yes:
    chars += punctuation
if delete_symbols.lower() in yes:
    for symbol in 'il1Lo0O':
        chars = chars.replace(symbol, '')
        
def generate_password(length, chars):
    passwords = []
    for i in range(num_passwrds):
        password = ''
        for j in range(length):
            password += random.choice(chars)
        passwords.append(password)
    
    return f'Сгенерированные пароли {passwords}'

print(generate_password(len_passwd, chars))
    