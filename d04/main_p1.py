import re
import collections
import time

start = time.time()
with open('./input.txt', 'r') as f:
  data = f.read()
  rows = data.split('\n')
  
  game_data = [x.split(':')[1].split('|') for x in rows if len(x) > 0]
  print(game_data)
  game_numbers = [[[int(z) for z in re.findall(r'\d+',y)] for y in x] for x in game_data]
  print(game_numbers)
  game_duplicates = [list(set(x[0])) + list(set(x[1])) for x in game_numbers]
  print(game_duplicates)
  winning_number_count_per_game = [len([item for item, count in collections.Counter(x).items() if count > 1]) for x in game_duplicates]
  print(winning_number_count_per_game) 
  result = sum([2**(x-1) for x in winning_number_count_per_game if x > 0]) 
  print(result)


end = time.time()
print(end - start)
