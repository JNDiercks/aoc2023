import re
import math
import time

def travelledDistance(loadingTime, time):
  return loadingTime * (time - loadingTime) if time >= loadingTime else 0


start = time.time()
with open('./input.txt', 'r') as f:
  data = f.read()
  rows = data.split('\n')
  times = [int(x) for x in re.findall('\d+', rows[0])]
  distances = [int(x) for x in re.findall('\d+', rows[1])]
  print(times)
  print(distances)
  winning_strategies = [sum([travelledDistance(loadingTime, time) > distance for loadingTime in range(1, time+1)]) for time, distance in zip(times, distances)]
   
  print(winning_strategies)
  print(math.prod(winning_strategies))
end = time.time()
print(end - start)
