import sys
def t(a, b):
    for i in range(0, min(len(a), len(b))):
        if a[i] == b[i]:
            return False
    return True

k = 0
n = []
for l in sys.stdin:
    l = l.rstrip()
    if l.isdigit():
        k = int(l)
        break
    else:
        n.append(l)
s = [sum([t(a, o) for o in n if o != a]) for a in n]
t = list(s)
t.sort(reverse=True)
[print(a) for i, a in enumerate(n) if s[i] in t[:k]]
