"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""
words = ['разработка', 'сокет', 'декоратор']

for line in words:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длина строки: {}\n'.format(len(line)))


words = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
       b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
       b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']

for line in words:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длина строки: {}\n'.format(len(line)))

"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
words = [b'class', b'function', b'method']

for line in words:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длинна строки: {}\n'.format(len(line)))

"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

"""
word1 = b'attribute'
word2 = b'класс'
word3 = b'функция'
word4 = b'type'

#на строки, написанные на кириллице, выдается исключение

File "C:\Users\Lyubov\PycharmProjects\pythonProject\seminars_python\Final test.py", line 2
    word2 = b'класс'
          ^
SyntaxError: bytes can only contain ASCII literal characters.'''
"""

"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции

words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    b_word = word.encode('utf-8')
    print(f'{word} в байтовом представлении: {b_word}')
    decoded_word = b_word.decode('utf-8')
    print(f'{b_word} в строковом представлении: {decoded_word}')

"""

"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
""" 

import subprocess
import chardet

class Ping:
    def __init__(self, urls):
        self.urls = urls

    def run_ping(self):
        for url in self.urls:
            process = subprocess.Popen(['ping', '-c', '4', url],stdout=subprocess.PIPE)
            output, error = process.communicate()
            encoding = chardet.detect(output)['encoding']
            decoded_output = output.decode(encoding)
            print(f'Ping для {url}:')
            print(decoded_output)


urls = ['yandex.ru', 'youtube.com']
ping = Ping(urls)
ping.run_ping()