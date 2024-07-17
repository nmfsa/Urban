info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
    strings_positions = {}
    line_number = 1
    position = None
    for string in strings:
        file = open(file_name, 'a', encoding='utf-8')
        position = file.tell()
        file.write(string)
        file.write('\n')
        strings_positions[line_number, position] = string
        line_number += 1
        file.close()
    return strings_positions


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
