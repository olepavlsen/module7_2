def custom_write(file_name, strings):
    string_position = dict()
    for i in range(len(strings)):
        file = open(file_name, 'r', encoding='utf-8')
        file.read()
        key_ = file.tell()
        file.close()
        file = open(file_name, 'a', encoding='utf-8')
        file.seek(key_)
        file.write(strings[i])
        file.write('\n')
        file.close()
        string_position[(i+1, key_)] = strings[i]
    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
