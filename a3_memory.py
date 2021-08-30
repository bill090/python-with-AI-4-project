from collections import deque
import random
import numpy as np
import torch

memory = deque()
state = (True,True,False,False, # danger 
         False,True,False,False, # move direction
         False,False,True,False  # Apple direction
        )
action = [0,0,1]
reward = -10
next_state = (True,False,False,False, # danger 
         True,False,False,False, # move direction
         False,False,True,False  # Apple direction
        )
done = False
memory.append((state, action, reward, next_state, done))
#print(memory)

state = (False,False,False,True, # danger 
         False,True,False,False, # move direction
         False,True,False,False  # Apple direction
        )
action = [1,0,0]
reward = 0
next_state = (False,False,False,True, # danger 
         False,True,False,False, # move direction
         False,True,False,False  # Apple direction
        )
done = False
memory.append((state, action, reward, next_state, done))
print(memory)

states, actions, rewards, next_states, dones = zip(*memory)
print(actions)

arr = np.array(state, dtype=int)
print(state)
print(arr)

state = torch.tensor(state, dtype=torch.float)
print(state)
state = torch.unsqueeze(state, 0)
print(state)
