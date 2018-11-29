#! Программа подсчета слов из файла
import os

def get_words(fileName):
    with open(fileName, 'r') as file:
        text = file.read()
        text = text.replace('\n', ' ')
        text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace('-', '').replace('(', '').replace(')', '')
        text = text.lower()
        spisok_words = text.split()
        spisok_words.sort()
        return spisok_words

def get_words_dict(spisok_words):
    word_dict = dict()
    for word in spisok_words:
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    return word_dict

def main():
    fileName = 'contents.txt'
    if not os.path.exists(fileName):
        print('Указанный файл не существует')
    else:
        spisok_words = get_words(fileName)
        word_dict = get_words_dict(spisok_words)
        print('Кол-во слов: %d' % len(spisok_words))
        print('Кол-во уникальных слов: %d' % len(word_dict))
        print('Все испоьзованные слова:')
        for word in word_dict:
            print(word.ljust(20), word_dict[word])

if __name__ == '__main__':
    main()