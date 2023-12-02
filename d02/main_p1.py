import re

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
    red_exceeded = count_red < max([int(x) for x in re.findall(rf'(\d+(?= red))', l)])
    print(red_exceeded)
    green_exceeded = count_green < max([int(x) for x in re.findall(rf'(\d+(?= green))', l)])
    print(green_exceeded)
    blue_exceeded = count_blue < max([int(x) for x in re.findall(rf'(\d+(?= blue))', l)])
    print(blue_exceeded)

    if not red_exceeded and not green_exceeded and not blue_exceeded:
       sum = sum + index + 1

print("Result")
print(sum)
