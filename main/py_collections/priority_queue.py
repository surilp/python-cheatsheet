from heapq import heapify, heappop, heappush

heap_queue = [(0,0)] # (cost, vertex)
heapify(heap_queue)
heappop(heap_queue)
heappush(heap_queue, (1,1))


