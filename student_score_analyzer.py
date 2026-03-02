import numpy as np

# Student exam scores across 5 subjects
students = np.array([
    [85, 92, 78, 90, 88],   # Student 0
    [72, 68, 75, 70, 73],   # Student 1
    [90, 95, 92, 98, 94],   # Student 2
    [55, 60, 58, 52, 57],   # Student 3
    [78, 82, 80, 85, 79],   # Student 4
    [40, 45, 38, 42, 41],   # Student 5
])

normalized = np.round((students - students.min()) / (students.max() - students.min()),2)
mean = np.round(normalized.mean(axis = 1),2)
category = []
for i,score in enumerate(mean):
    if mean[i] > 0.7:
        category.append((mean[i],'High'))
    elif mean[i] > 0.4 and mean[i] < 0.7:
        category.append((mean[i],'Mid'))
    else: 
        category.append((mean[i],'Low'))
for i,score in enumerate(mean):
    print(f"Student {i}    avg = {mean[i]}  -->  {category[i][1]}")