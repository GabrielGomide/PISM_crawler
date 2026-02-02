import matplotlib.pyplot as plt
import numpy as np

# Dados
components = ["Portuguese", "Mathematics", "Literature", "History", 
               "Geography", "Physics", "Chemistry", "Biology"]

values = [[] for x in range(8)]
years = ['2020', '2021', '2022', '2023', '2024']

for y in years:
    with open(f'var/operated_results/average_scores/average_scores{y}.txt', 'r') as rf:
        scores = rf.readlines()[1:]
        for i in range(len(scores)):
            values[i].append(float(scores[i].strip()))

colors = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F', '#8E44AD', '#1ABC9C', '#E67E22', '#2C3E50']

# Create figure
n_years = 5
n_components = len(components)
width = 1
x = np.arange(n_years * n_components)

plt.figure(figsize=(15,6))

# Plots bars
for i, comp in enumerate(components):
    for j in range(n_years):
        plt.bar(x[i * n_years + j], values[i][j], color=colors[i], width=width, edgecolor='black')

plt.title(f"Average Score per Curricular Component in PISM I {years[0]} - {years[-1]}")


# Y Axis
plt.ylabel("Average Score")

# Defining segments in X Axis
positions = [i * n_years + (n_years - 1) / 2 for i in range(n_components)]  # centro de cada bloco
plt.xticks(positions, components)

plt.grid(True, which='both', axis='both', linestyle='-', alpha=0.6)

plt.show()
