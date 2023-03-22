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

unicode_words = []

for word in words:
    unicode_word = ''
    for letter in word:
        unicode_word += f'\\u{ord(letter):04x}'
    unicode_words.append(unicode_word)

for i, unicode_word in enumerate(unicode_words):
    print(f'{i+1}. {type(unicode_word)} {unicode_word}')

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

for word in words:
    print(type(word), word, len(word))


"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

words = ['attribute', 'класс', 'функция', 'type']

for word in words:
    try:
        b_word = bytes(word, 'utf-8')
        print(f'{word} можно записать в байтовом типе: {b_word}')
    except:
        print(f'{word} нельзя записать в байтовом типе')


"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    b_word = word.encode('utf-8')
    print(f'{word} в байтовом представлении: {b_word}')
    decoded_word = b_word.decode('utf-8')
    print(f'{b_word} в строковом представлении: {decoded_word}')



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
