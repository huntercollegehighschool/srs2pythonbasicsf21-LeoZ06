"""
Define a function sumofsquares that takes an integer input number. The function then adds all the first n perfect squares (starting from 1).

For example, sumofsquares(3) should return 14, since 1 + 4 + 9 = 14.
"""
import math

def sumofsquares(number):
  print(math.floor(number*(number+1)*(2*number+1)/6))