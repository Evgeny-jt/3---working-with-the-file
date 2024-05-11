analyzed_files = ['1.txt', '2.txt', '3.txt']
number_of_lines_in_file = {}

for name_file in analyzed_files:
    with open(name_file, 'r', encoding='utf-8') as f:
        number_of_lines = 0
        for line in f:
            number_of_lines += 1
        number_of_lines_in_file[number_of_lines] = name_file

for key, value in sorted(number_of_lines_in_file.items()):
    with open(value, 'r', encoding='utf-8') as f:
        text_file = f.read()
    text_writ = f'{value}\n{key}\n{text_file.strip()}\n'
    with open('new file.txt', 'a', encoding='utf-8') as new_f:
        new_f.write(text_writ)
