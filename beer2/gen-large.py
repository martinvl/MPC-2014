from random import randint

m = int(1e6)

num = ''.join(map(str, (randint(0, 9) for j in xrange(m - 3))))

e = sum(map(int, num[0::2]))
o = sum(map(int, num[1::2]))

d = [0, 0, 0]

# find last three digits to make divisible
for i in xrange(0, 1000):
    d = [i/100, (i % 100)/10, (i % 10)]

    de = sum(map(int, d[0::2]))
    do = sum(map(int, d[1::2]))

    if (m - 3) % 2:
        de = sum(map(int, d[1::2]))
        do = sum(map(int, d[0::2]))

    if d[-1] % 2:
        continue

    if (e + o + de + do) % 9:
        continue

    if (e - o + de - do) % 11:
        continue

    break

num += ''.join(map(str, d))

print num
