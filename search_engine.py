import numpy as np

# Knowledge base of topic vectors
knowledge_base = np.array([
    [0.99, 0.02, 0.95, 0.01],  # "Machine Learning"
    [0.98, 0.97, 0.96, 0.02],  # "Deep Learning"
    [0.02, 0.01, 0.03, 0.99],  # "Web Development"
    [0.87, 0.05, 0.60, 0.10],  # "Data Science"
    [0.78, 0.95, 0.70, 0.03],  # "Neural Networks"
    [0.15, 0.98, 0.12, 0.05],  # "Natural Language Processing"
    [0.92, 0.11, 0.88, 0.07],  # "Computer Vision"
    [0.05, 0.92, 0.08, 0.12],  # "Reinforcement Learning"
])

topics = [
    "Machine Learning",
    "Deep Learning",
    "Web Development",
    "Data Science",
    "Neural Networks",
    "Natural Language Processing",
    "Computer Vision",
    "Reinforcement Learning"
]

queries = np.array([
    [0.96, 0.95, 0.94, 0.01],  # Query 0
    [0.88, 0.06, 0.82, 0.09],  # Query 1
    [0.03, 0.93, 0.05, 0.11],  # Query 2
])

query_names = ["AI Overview", "Vision & ML", "Language & RL"]

def similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

for i in range(len(queries)):
    query_list = []
    for j in range(len(knowledge_base)):
        score = np.round(similarity(queries[i], knowledge_base[j]), 4)
        query_list.append((j, score))
    query_list.sort(key=lambda x: x[1], reverse=True)
    top3 = query_list[:3]
    top3_scores = [score for idx, score in top3]
    total = sum(top3_scores)
    print(f"Query: {query_names[i]}")
    for idx, score in top3:
        confidence = np.round(score / total, 2)
        if confidence > 0.30:
            print(f"  {topics[idx]:<25} raw: {score}  confidence: {confidence}")
    print()