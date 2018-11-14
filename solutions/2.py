s = str
[print(x) for x in range(1, 999999) if (x % 3 == 0 or x % 5 == 0 or x % 7 == 0) and (x < 10 or s(x)[0] == s(x)[-1])]