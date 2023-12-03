import re
import time

def has_adjacent_symbols(index, input, row_length):
  for row in [-1,0,1]:
    for column in [-1,0,1]:
      current_index = (index + (row*row_length) + column)
      if current_index >=0 and current_index < len(input):
        print(index, current_index, input[current_index])
        if re.search(r'[^\d.\r\n]',input[current_index]):
          return True

def is_machine_part(start_index, end_index, input, row_length):
  for i in range(start_index, end_index):
    if has_adjacent_symbols(i, input, row_length): 
      return True

start = time.time()
with open('./input.txt', 'r') as f:
  data = f.read()
  rows = data.split('\n')
  row_count = len(data)
  max_row_length = max([len(x) for x in rows]) + 1 # +1 accounts for the newline symbol
  print(max_row_length)

  for match in re.finditer(r'\d+',data): 
    match_group = match.group()
    match_length = len(match_group)
    match_start = match.start()
    match_end = match.end()
    print("match", match_group, "start index", match_start, "End index", match_end)

    if not is_machine_part(match_start,match_end, data, max_row_length):
      data = data[:match_start] + '.' * match_length + data[match_end:]

  print(data)
  numbers = re.findall('\d+', data)
  print(numbers)
  result = sum([int(x) for x in numbers])
  print(result)

end = time.time()
print(end - start)
