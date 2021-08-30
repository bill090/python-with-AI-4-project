from collections import deque

fruits = ['apple','banana','cherry']
print(*fruits)

memory = deque()
memory.append(['Auston Matthews',34,'C'])
memory.append(['John Tavares',91,'C'])
memory.append(['Jack Campbell',36,'G'])

print(memory)
names,numbers,positions = zip(*memory)
print(names)
print(numbers)
print(positions)

