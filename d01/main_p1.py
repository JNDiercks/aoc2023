import re

with open('./input.txt', 'r') as f:
  data = f.read()
  data = data.split('\n')
  data = [d for d in data if len(d) > 0]
        
  sum = 0
  for l in data: 
    print(l)
    numbers = re.sub('[^0-9]+', '', l)
    print(numbers)
    calibration_values = numbers[0] + numbers[len(numbers)-1] 
    print(calibration_values)
    sum = sum + int(calibration_values)

print("Result")
print(sum)
