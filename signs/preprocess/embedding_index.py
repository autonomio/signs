import numpy as np


def embedding_index(trained_vectors):

    '''KERAS EMBEDDING INDEX

    Takes in trained vectors (e.g. GloVe) and returns
    a Keras embeddings index.

    PARAMS
    ------

    trained_vectors :: a file with the trained vectors

    '''

    embeddings_index = {}

    with open(trained_vectors, encoding='utf-8') as f:

        for line in f:

            values = line.split()
            word = values[0]
            try:
                coefs = np.asarray(values[1:], dtype='float32')
            except ValueError:
                pass
            embeddings_index[word] = coefs

    vector_dims = len(list(embeddings_index.values())[0])

    return embeddings_index, vector_dims
