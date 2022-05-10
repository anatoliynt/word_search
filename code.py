file_text = open('https://github.com/anatoliynt/word_search/blob/main/short.txt', 'r')
word_search = input('Введите слово для поиска: ')
# new = file_text.read().find(word_search)
# print(new)
temp_list = []
end_list = []
for i_file_text in file_text:
    for j_file_name in i_file_text:
        if j_file_name != '.' and j_file_name != ' ' and j_file_name != '!' and j_file_name != ',' \
                and j_file_name != '-' and j_file_name != '\n':
            temp_list.append(j_file_name)
        else:
            temp_list = ''.join(temp_list)
            end_list.append(temp_list)
            temp_list = []
count_word = end_list.count(word_search)
print(f'Слово {word_search} встречается', count_word, 'раз.')
