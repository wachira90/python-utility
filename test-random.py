import os
import sys
import random

min = 0
max = 999
digits = [str(random.randint(min, max)) for i in range(1500)]
digits = [(len(str(max))-len(digit))*'0'+digit for digit in digits]
print(digits)