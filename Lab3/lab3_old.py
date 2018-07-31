import random

mi = mj = mk = ms = mt = 0
i = j = k = s = t = 0

a = [[random.randrange(1, 10) for j in range(5)] for i in range(5)]
for i in a:
    print(i)

p = 1
minp = 1000
for i in range(5):
    for j in range(5):
        for k in range(5):
            for s in range(5):
                for t in range(5):
                    if (i != j) and (i != k) and (i != s) and (i != t) and (j != k) and (j != s) and (j != t) and (
                                k != s) and (k != t) and (s != t):
                        p = a[i][j] + a[j][k] + a[k][s] + a[s][t] + a[t][i]
                        if p < minp:
                            minp = p
                            mi, mj, mk, ms, mt, = i, j, k, s, t

print(mi, mj, mk, ms, mt)
print('Minimal ', minp)
