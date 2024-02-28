import random
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return comparisons

# Create lists of different sizes and measure average comparisons
list_sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800]
average_comparisons = []

for size in list_sizes:
    comparisons_sum = 0
    num_iterations = 100  # Number of iterations to calculate average comparisons
    for _ in range(num_iterations):
        my_list = [random.randint(1, 1000) for _ in range(size)]
        comparisons = bubble_sort(my_list.copy())  # Create a copy to avoid modifying the original list
        comparisons_sum += comparisons
    average_comparisons.append(comparisons_sum / num_iterations)

# Create the graph
plt.figure(figsize=(10, 6))
plt.plot(list_sizes, average_comparisons, marker='o', linestyle='-')
plt.title('Average Bubble Sort Comparisons vs List Size')
plt.xlabel('List Size')
plt.ylabel('Average Comparisons')
plt.grid(True)

plt.show()