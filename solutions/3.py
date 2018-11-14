import sys, heapq

s = sys.stdin
T = int(s.readline())
r = s.readline
for i in range(T):
    L = list(set([x for x in r().split()]))
    k = int(r())
    max_heap = [-float(x) for x in L]
    heapq.heapify(max_heap)
    for _ in range(k):
        kth_largest = -heapq.heappop(max_heap)
    for x in L:
        if float(x) == kth_largest:
            print(x)
            break
