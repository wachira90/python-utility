#!python
import numpy as np

a = np.array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40])
print("Original array:")
print(a,"\n")
unique_elements, counts_elements = np.unique(a, return_counts=True)
print("Frequency of unique values of the said array:")
print(np.asarray((unique_elements, counts_elements)))
