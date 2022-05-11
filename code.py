# открываю файл с текстом
file_text = open('text_book.txt', 'r')
# запрашиваю слово для поиска
word_search = input('Введите слово для поиска: ')
# временная переменная для прохода по символам с целью исключения знаков препинания
temp_list = []
# итоговый список со словами
end_list = []
# цикл прохода по исходному тексту (словам)
for i_file_text in file_text:
    # цикл прохода по буквам в словах
    for j_file_name in i_file_text:
        # если встречается знак препинания, значит обрываю цикл и формирую слово 
        if j_file_name != '.' and j_file_name != ' ' and j_file_name != '!' and j_file_name != ',' \
                and j_file_name != '-' and j_file_name != '\n':
            # добавляю по-символьно во временный лист
            temp_list.append(j_file_name)
        # иначе "склеиваю" слово в итоговое
        else:
            temp_list = ''.join(temp_list)
            # добавляю в итоговый список
            end_list.append(temp_list)
            # обнуляю временный список 
            temp_list = []
# считаю кол-во слов
count_word = end_list.count(word_search)
# принтую
print(f'Слово {word_search} встречается', count_word, 'раз.')
