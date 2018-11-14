import sys, heapq as h

s = sys.stdin
T = int(s.readline())
r = s.readline
for i in range(T):
    L = list(set([x for x in r().split()]))
    k = int(r())
    m = [-float(x) for x in L]
    h.heapify(m)
    for _ in range(k):
        g = -h.heappop(m)
    for x in L:
        if float(x) == g:
            print(x)
            break
