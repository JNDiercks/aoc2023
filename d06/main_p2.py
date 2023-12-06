import re
import numpy as np
import math
import time

def travelledDistance(loadingTime, time):
  return loadingTime * (time - loadingTime) if time >= loadingTime else 0

def waysToBeatRecord(record_time, record_distance):
  polynomial = [-1, record_time, -record_distance]
  roots = np.roots(polynomial)
  roots.sort()
  return math.ceil(roots[1]-1) - math.floor(roots[0]+1) + 1

with open('./input.txt', 'r') as f:
  data = f.read()
  rows = data.split('\n')
  record_time = int("".join(re.findall('\d+', rows[0])))
  record_distance = int("".join(re.findall('\d+', rows[1])))
  start_first = time.time()
  brute_force_solution = sum([travelledDistance(loadingTime, record_time) > record_distance for loadingTime in range(1, record_time+1)])
  end_first = time.time()
  start_second = time.time()
  inequation_solution = waysToBeatRecord(record_time, record_distance)
  end_second = time.time()
   
  print("brute force: ", brute_force_solution, end_first - start_first)
  print("inequation: ", inequation_solution, end_second - start_second)
