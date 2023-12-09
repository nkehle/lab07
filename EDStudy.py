# Noa Kehle
# nkehle@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 07

import time
import random
import matplotlib.pyplot as plt
from EditDistance import EditDistance 

def generate_random_string(size):
    alphabet = ['A', 'T', 'C', 'G']
    return ''.join(random.choice(alphabet) for _ in range(size))

def run_experiment_same_strings(size, num_samples):
    ed = EditDistance()
    total_time = 0

    for sample in range(num_samples):
        string = generate_random_string(size)
        start_time = time.time()
        ed.findEditDistance(string, string)
        total_time += time.time() - start_time

    return total_time / num_samples

def run_experiment_random_strings(size, num_pairs):
    ed = EditDistance()
    total_time = 0
    total_distance = 0

    for pair in range(num_pairs):
        len_str1 = random.randint(1, size - 1)
        len_str2 = size - len_str1
        string1 = generate_random_string(len_str1)
        string2 = generate_random_string(len_str2)

        start_time = time.time()
        distance = ed.findEditDistance(string1, string2)
        total_time += time.time() - start_time
        total_distance += distance

    return total_time / num_pairs, total_distance / num_pairs


if __name__ == "__main__":
    sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    num_samples = 100
    num_pairs = 200

    avg_times_same_strings = []
    avg_times_random_strings = []
    avg_distances_random_strings = []

    for size in sizes:
        avg_time_same_strings = run_experiment_same_strings(size, num_samples)
        avg_time_random_strings, avg_distance_random_strings = run_experiment_random_strings(size, num_pairs)

        avg_times_same_strings.append(avg_time_same_strings)
        avg_times_random_strings.append(avg_time_random_strings)
        avg_distances_random_strings.append(avg_distance_random_strings)

    # Plotting

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(sizes, avg_times_same_strings, label='Same Strings')
    plt.plot(sizes, avg_times_random_strings, label='Random Strings')
    plt.xlabel('String Size')
    plt.ylabel('Average Running Time')
    plt.legend()
    plt.title('Running Time Comparison')

    plt.subplot(1, 2, 2)
    plt.plot(sizes, avg_distances_random_strings, label='Random Strings')
    plt.xlabel('String Size')
    plt.ylabel('Average Edit Distance')
    plt.legend()
    plt.title('Edit Distance Comparison')

    plt.tight_layout()
    plt.show()
