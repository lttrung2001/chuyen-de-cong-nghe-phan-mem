import numpy as np
import re

documents = [
    "The quick brown fox jumps over the lazy dog.",
    "A quick brown dog jumps over the lazy fox.",
    "The lazy brown dog jumps over the quick fox."
]

pattern = r'[.]'


# Build a vocabulary of unique words in the documents
vocabulary = set()

for num in range(len(documents)):
    documents[num] = re.sub(pattern, '', documents[num])
    print(documents[num])

for document in documents:
    vocabulary.update(document.lower().split())

print(vocabulary)

print(documents)

# Build the boolean matrix
matrix = np.zeros((len(documents), len(vocabulary)), dtype=int)
for i, document in enumerate(documents):
    words = set(document.lower().split())
    for j, word in enumerate(vocabulary):
        if word in words:
            matrix[i, j] = 1            

# # Print the boolean matrix
print(matrix)
query = "brown AND dog"
query_words = query.lower().split()
query_vector = np.array([1 if word in query_words else 0 for word in vocabulary])
matching_documents = np.nonzero(np.all(matrix[:, query_vector == 1], axis=1))[0]
print(matching_documents)
           