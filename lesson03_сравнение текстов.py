
r = open('text3.txt', encoding='utf-8')
r1 = set(r.read().split())
r.close()

r = open('text2.txt', encoding='utf-8')
r2 = set(r.read().split())
r.close()


#new = r1.intersection(r2)
new = r2.difference(r1)

        
print(new)
