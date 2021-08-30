from collections import deque
import random

MAX_MEMORY = 2000
memory = deque([1, 2, 3,4, 5, 6],maxlen=MAX_MEMORY)
print(f"length of queue: {len(memory)}")
print(memory)
print("Pop")
print(memory.pop())
print(memory)

print("Pop left")
print(memory.popleft())
print(memory)

print("Append and append left")
memory.append("a")
memory.appendleft("b")
print(memory)

print("Randomly take 3 samples")
for i in range(4):
    sample = random.sample(memory,3)
    print(sample)

