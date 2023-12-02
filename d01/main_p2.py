import re

def string_to_int(input):
    names_to_values = [
        'zero', 'one', 'two', 
        'three', 'four', 'five', 
        'six', 'seven', 'eight', 
        'nine'
    ]
    try:
        return int(input)
    except ValueError:
        return names_to_values.index(input)

with open('./input.txt', 'r') as f:
  data = f.read()
  data = data.split('\n')
  data = [d for d in data if len(d) > 0]
        
  sum = 0
  for l in data: 
    print(l)
    numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', l) 
    print(numbers)
    calibration_values = int(f"{string_to_int(numbers[0])}{string_to_int(numbers[-1])}") 
    print(calibration_values)
    sum = sum + calibration_values

print("Result")
print(sum)
