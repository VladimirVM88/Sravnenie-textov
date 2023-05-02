
r = open('text1.txt', encoding='utf-8') # Первый текст помещается в файл text1.txt в корне папки с программой
r1 = set(r.read().split())
r.close()

r = open('text2.txt', encoding='utf-8') # Второй текст помещается в файл text2.txt в корне папки с программой
r2 = set(r.read().split())
r.close()


# new = r1.intersection(r2)  # Раскомментировать строку, если необходимо сравнить тексты на предмет использования одинаковых слов в обоих текстах
# new = r2.difference(r1) # Показывает слова, которые не используются в r1
new = r1.difference(r2) # Показывает слова, которые не используются в r2
        
print(new)
