from ..preprocess.prepocess_embeddings import keras_embeddings
from ..preprocess.prepocess_embeddings import keras_tokenize
from ..preprocess.prepocess_embeddings import keras_embedding_matrix

from keras.layers import Embedding


class Embeds:

    def __init__(self, trained_vectors):

        self.t_v = trained_vectors
        self.embeddings_index, self.vector_dims = keras_embeddings(self.t_v)

    def _matrix(self):

        self.x, self.vocab_size, self.word_index = keras_tokenize(self.docs)
        self.embedding_matrix = keras_embedding_matrix(self.word_index,
                                                       self.vector_dims,
                                                       self.embeddings_index)

    def layer(self, docs):

        self.docs = docs

        self._matrix()

        embeddding_layer = Embedding(self.vocab_size,
                                     self.vector_dims,
                                     weights=[self.embedding_matrix],
                                     input_length=self.x.shape[1],
                                     trainable=False)

        return embeddding_layer, self.x
