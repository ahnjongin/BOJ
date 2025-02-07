import sys
import heapq

def heap(operations):
    min_heap = []
    results = []

    for x in operations:
        if x == 0:
            if min_heap:
                results.append(heapq.heappop(min_heap))
            else:
                results.append(0)
        else:
            heapq.heappush(min_heap, x)

    return results

n = int(sys.stdin.readline().strip())
operations = [int(sys.stdin.readline().strip()) for _ in range(n)]

for result in heap(operations):
    print(result)