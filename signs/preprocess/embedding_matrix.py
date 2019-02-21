import numpy as np


def embedding_matrix(word_index,
                     vector_dims,
                     embeddings_index,
                     max_num_words=None):

    if max_num_words is None:
        max_num_words = len(word_index) + 1

    num_words = min(max_num_words, len(word_index) + 1)
    embedding_matrix = np.zeros((num_words, vector_dims))

    for word, i in word_index.items():
        if i >= num_words:
            continue
        embedding_vector = embeddings_index.get(word)

        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector

    return embedding_matrix
