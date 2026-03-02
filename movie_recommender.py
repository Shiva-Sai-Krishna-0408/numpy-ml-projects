import numpy as np

# User preference vectors for a recommendation system
users = np.array([
    [0.99, 0.02, 0.95, 0.01],  # User 0 — loves action
    [0.98, 0.97, 0.96, 0.02],  # User 1 — loves romance
    [0.02, 0.01, 0.03, 0.99],  # User 2 — loves comedy
    [0.87, 0.05, 0.60, 0.10],  # User 3 — mixed action
    [0.78, 0.95, 0.70, 0.03],  # User 4 — mixed romance
])

movies = np.array([
    [0.95, 0.01, 0.90, 0.02],  # "Action Hero"
    [0.97, 0.96, 0.95, 0.01],  # "Love Story"
    [0.01, 0.02, 0.02, 0.98],  # "Comedy Night"
    [0.88, 0.04, 0.65, 0.08],  # "Battle cry"
    [0.75, 0.94, 0.72, 0.02],  # "Romance Road"
    [0.02, 0.95, 0.03, 0.10],  # "Laugh Out Loud"
])

movie_names = [
    "Action Hero",
    "Love Story",
    "Comedy Night",
    "Battle Cry",
    "Romance Road",
    "Laugh Out Loud"
]

def similarity(a,b):
    return np.dot(a,b) / ((np.linalg.norm(a)) * (np.linalg.norm(b)))
    
for i in range(len(users)):
    movie_list = []
    for j in range(len(movies)):
        score = np.round(similarity(users[i],movies[j]),2)
        movie_list.append((j,score))
    movie_list.sort(key = lambda x : x[1], reverse = True)
    print(f"User {i}")
    for rank,(idx,score) in enumerate(movie_list[:2]):
        print(f"Rank {rank+1}  {movie_names[idx]} --> similarity: {score}")