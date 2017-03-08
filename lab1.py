import random


def sets():
    lst = []
    while len(lst) < 20:
        n = random.randint(1, 40)
        if n not in lst:
            lst.append(n)
    return lst

x, a, b, c, d = [i + 1 for i in range(40)], sets(), sets(), sets(), []

print(' Множина A = %s \n Множина B = %s \n Множина C = %s' % (a, b, c,))

na = x
for i in a:
    for j in x:
        if i == j:
            na.remove(i)
            break

print(' Доповнення множини А', na)

for i in na:
    for j in b:
        if i == j:
            for l in c:
                if i == l:
                    d.append(i)
                    break

print(' Перетин множин', chr(195), 'B C =', d)