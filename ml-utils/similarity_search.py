import numpy as np

def cosine_similarity(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector2 = np.linalg.norm(vector2)
    similarity = dot_product / (norm_vector1 * norm_vector2)
    return similarity

# Example usage:
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
similarity_score = cosine_similarity(vector1, vector2)
print("Cosine Similarity:", similarity_score)

# Adding reusable cosine similarity search function

def similarity_search():
    print(f"Similarity Score: {similarity_score}")
