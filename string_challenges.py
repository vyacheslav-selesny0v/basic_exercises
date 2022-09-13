# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
count = 0
for i in word.lower():
    if i == 'а':
        count += 1
print(count)


# Вывести количество гласных букв в слове
word = 'Архангельск'
total = 0
for i in word.lower(): 
    if i in 'ауоыиэяюёе':
        total += 1
print(total)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.replace(' ', ''))/len(sentence.split()))