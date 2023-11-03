import heapq

data = [10,20,43,1,2,65,17,44,2,3,1]
#print(sorted(data))
heapq.heapify(data)
print(data)

copy = data[:]
print(heapq.heappop(data))

print(heapq.heappush(data, 2))
print(data)
print(heapq.heappush(data, 4))
print(heapq.heappush(data, 19))
print(heapq.heappush(data, 21))
heapq._heapify_max(data)
print(data)
# print(copy.pop(0))
# print(data)
# print(copy)
