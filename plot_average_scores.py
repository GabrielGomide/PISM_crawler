import matplotlib.pyplot as plt

# Data
components = ["Portuguese", "Mathematics", "Literature", "History", 
               "Geography", "Physics", "Chemistry", "Biology"]

year = int(input('Year: '))
with open(f'var/operated_results/average_scores/average_scores{year}.txt') as rf:
    values = [float(x[:-1]) for x in rf.readlines()[1:]]
    rf.close()

# Create the graph
plt.figure(figsize=(10,6))
bars = plt.bar(components, values)

# Attributes different colors to each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F', '#8E44AD', '#1ABC9C', '#E67E22', '#2C3E50']
for i, bar in enumerate(bars):
    bar.set_color(colors[i])

# Titles and labels
plt.xlabel("Curricular Component")
plt.ylabel("Average Score")
plt.title(f"Average Score per Curricular Component in PISM I {year}")
plt.xticks(rotation=30)

plt.grid(True, which='both', axis='both', linestyle='-', alpha=0.6)

# Show the graph
plt.show()
