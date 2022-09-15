# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = dict()

for student in students:
    if student['first_name'] not in names:
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1
for name, count in names.items():
    print(f'{name}: {count}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names = dict()
for student in students:
    if student['first_name'] not in names.keys():
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1
print(max(names, key=names.get))


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

from collections import Counter

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


for school_class, val in enumerate(school_students, start=1):
    names = [name['first_name'] for name in val]
    names_count = Counter(names)
    print(f'Самое частое имя в классе {school_class}: {names_count.most_common()[0][0]}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for school_class in school:
    count_man = 0
    count_girl = 0
    for student in school_class["students"]:
        if student["first_name"] in is_male and is_male[student["first_name"]] == True:
            count_man += 1
        else:
            count_girl += 1
    print(f'Класс {school_class["class"]}: девочки {count_girl}, мальчики {count_man}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

school_cl = dict()

for school_class in school:
    
    max_count_man = 0
    max_count_girl = 0
    count_man = 0
    count_girl = 0
    
    for student in school_class["students"]:
        if student["first_name"] in is_male and is_male[student["first_name"]] == True:
            count_man += 1
        else:
            count_girl += 1
        school_cl[school_class['class']] = {'man': count_man, 'girl': count_girl}

    for k, v in school_cl.items():
        if v['man'] >= max_count_man:
            max_count_man = v['man']
        else:
            v['man'] = v['man']
        
        if v['girl'] >= max_count_girl:
            max_count_girl = v['girl']
        else:
            v['girl'] = v['girl']

       
print(f'Больше всего мальчиков в классе', *[k for k, v in school_cl.items() if v['man'] == max_count_man])
print(f'Больше всего девочек в классе', *[k for k, v in school_cl.items() if v['girl'] == max_count_girl])
