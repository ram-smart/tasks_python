#! Программа подсчета слов из файла
import os

def get_words(fileName):
    with open(fileName, 'r', encoding="utf8") as file:
        text = file.read()
        text = text.replace('\n', ' ')
        text = text.replace('.', '').replace(':', '').replace(';', '').replace(',', '').replace('!', '').replace('?', '').replace('(', '').replace(')','').replace('"', '').replace('”','')
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


def writer_in_file(word_dict, spisok_words):
    with open('result.txt', 'w') as file:
        file.write('Кол-во слов: %d' % len(spisok_words) + '\n')
        file.write('Кол-во уникальных слов: %d' % len(word_dict) + '\n')
        file.write('Все испоьзованные слова: \n')
        for key, value in word_dict.items():
            s = key + ' - ' + str(value) + '\n'
            file.write(s)
            print('\n')


def main():
    fileName = 'contents.txt'
    if not os.path.exists(fileName):
        print('Указанный файл не существует')
    else:
        spisok_words = get_words(fileName)
        word_dict = get_words_dict(spisok_words)
        writer_in_file(word_dict, spisok_words)


if __name__ == '__main__':
    main()