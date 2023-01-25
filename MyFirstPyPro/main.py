# Ex.1
# Из строки «Python is the best programming language in the world» получить подстроку
# начиная с 6 символа с начала исходной строки и до 7 символа с конца исходной строки
# (нумерация символов начинается с нуля).
s1 = 'Python is the best programming language in the world'
s2 = s1[5:-6]
print('Ex.1: ' + s2)

# Ex.2
# Вывести каждый третий символа строки «Guido van Rossum is the benevolent dictator for life».
s1 = 'Guido van Rossum is the benevolent dictator for life'
s2 = s1[2::3]
print('Ex.2: ' + s2)

# Ex.3
# Из строки «You have a problem with authority, Mr. Anderson.» получить словарь, где ключ -это символ,
# а значение - это количество повторений символа в строке.
s1 = 'You have a problem with authority, Mr. Anderson.'
s1_chars = set(s1)
ans_map = list(map(s1.count, s1_chars))
ans_zip = dict(zip(s1_chars, ans_map))
print('Ex.3:')
print(ans_zip)