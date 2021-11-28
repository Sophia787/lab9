def sort_sentence(sentence):
    words = sentence.split()            # Разделяем слова через пробел и вносим в список words
    words = sorted(words, key=len)      # Сортировка слов по длине
    return " ".join(words).capitalize() # Соединение слов в одну строку через пробел. Затем первый символ переводим верхний регистр


if __name__ == '__main__':
    while True:
        sentence = input("Вход: ")
        print("Вывод:", sort_sentence(sentence))
