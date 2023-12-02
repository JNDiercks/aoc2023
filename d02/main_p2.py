import re
import time

start = time.time()
with open('./input.txt', 'r') as f:
  data = f.read()
  data = data.split('\n')
  data = [d for d in data if len(d) > 0]
        
  count_red = 12
  count_green = 13
  count_blue = 14
  
  sum = 0
  for index, l in enumerate(data): 
    print(l)
    red_max = max([int(x) for x in re.findall(rf'(\d+(?= red))', l)])
    print(red_max)
    green_max = max([int(x) for x in re.findall(rf'(\d+(?= green))', l)])
    print(green_max)
    blue_max = max([int(x) for x in re.findall(rf'(\d+(?= blue))', l)])
    print(blue_max)

    sum = sum + (red_max * green_max * blue_max)

print("Result")
print(sum)
end = time.time()
print(end - start)
