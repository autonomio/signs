from ..preprocess.embedding_index import embedding_index
from ..preprocess.embedding_matrix import embedding_matrix
from ..preprocess.tokenize import tokenize

from keras.layers import Embedding


class Embeds:

    def __init__(self, trained_vectors):

        '''Takes as input trained vectors and returns an object which can be
        used to to create a Keras Embeds layer given input of documents.

        e = Embeds('glove.twitter.27B.25d.tx')
        embedding_layer  = e.layer(docs)

        '''

        self.t_v = trained_vectors
        self.embeddings_index, self.vector_dims = embedding_index(self.t_v)

    def _matrix(self):

        '''Helper function for processing input docs for the
        Keras Embeds layer'''

        self.x, self.vocab_size, self.word_index = tokenize(self.docs)
        self.embedding_matrix = embedding_matrix(self.word_index,
                                                 self.vector_dims,
                                                 self.embeddings_index)

    def layer(self, docs):

        '''Takes as input a series or array of documents and returns
        a Keras embeddings layer and x data. 

        USE:

        embeds_layer, x = e.layer(docs) 

        then in Keras model: 

        model.add(embeds_layer)
        model.fit(x=x)

        '''

        self.docs = docs

        self._matrix()

        embeddding_layer = Embedding(self.vocab_size,
                                     self.vector_dims,
                                     weights=[self.embedding_matrix],
                                     input_length=self.x.shape[1],
                                     trainable=False)

        return embeddding_layer, self.x
