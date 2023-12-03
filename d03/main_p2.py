import re
import time
import math

def has_adjacent_symbols(index, input, row_length):
  matched_indices = []
  for row in [-1,0,1]:
    for column in [-1,0,1]:
      current_index = (index + (row*row_length) + column)
      if current_index >=0 and current_index < len(input):
        is_match = input[current_index] == '*'
        if is_match:
          matched_indices.append(current_index)
  return matched_indices
          
def is_gear_candidate(start_index, end_index, input, row_length):
  adjacent_star_indices = []
  for i in range(start_index, end_index):
    adjacent_star_indices = adjacent_star_indices + has_adjacent_symbols(i, input, row_length)
  return set(adjacent_star_indices)

start = time.time()
with open('./input.txt', 'r') as f:
  data = f.read()
  rows = data.split('\n')
  row_count = len(data)
  max_row_length = max([len(x) for x in rows]) + 1 # +1 accounts for the newline symbol

  gear_indices = {}
  for match in re.finditer(r'\d+',data): 
    match_group = match.group()
    match_start = match.start()
    match_end = match.end()
    print("match", match_group, "start index", match_start, "End index", match_end)
    gear_matches = is_gear_candidate(match_start,match_end, data, max_row_length)
    if len(gear_matches) > 0:
      print(gear_matches)
      for i in gear_matches:
        if not i in gear_indices:
          gear_indices[i] = [int(match_group)]
        else:
          gear_indices[i] += [int(match_group)]

  result = sum([math.prod(value) for (key,value) in gear_indices.items() if len(value) == 2])
  print(result)

end = time.time()
print(end - start)
