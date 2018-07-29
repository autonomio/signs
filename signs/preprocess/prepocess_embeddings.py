from numpy import asarray, zeros
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


def keras_tokenize(texts, num_words=None, maxlen=12, padding='post'):

    '''TOKENIZE

    Create a word index and returns padded docs in return.

    '''

    tokenizer = Tokenizer(num_words=num_words)
    tokenizer.fit_on_texts(texts)
    encoded_docs = tokenizer.texts_to_sequences(texts)
    word_index = tokenizer.word_index

    x = pad_sequences(encoded_docs, maxlen=maxlen, padding=padding)
    vocab_size = max(list(word_index.values())) + 1

    return x, vocab_size, word_index


def keras_embeddings(trained_vectors):

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
                coefs = asarray(values[1:], dtype='float32')
            except ValueError:
                pass
            embeddings_index[word] = coefs

    vector_dims = len(list(embeddings_index.values())[0])

    return embeddings_index, vector_dims


def keras_embedding_matrix(word_index,
                           vector_dims,
                           embeddings_index,
                           max_num_words=None):

    if max_num_words is None:
        max_num_words = len(word_index) + 1

    num_words = min(max_num_words, len(word_index) + 1)
    embedding_matrix = zeros((num_words, vector_dims))

    for word, i in word_index.items():
        if i >= num_words:
            continue
        embedding_vector = embeddings_index.get(word)

        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector

    return embedding_matrix
