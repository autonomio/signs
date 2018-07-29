import spacy as sp
try:
    import en_core_web_sm
except ModuleNotFoundError:
    pass

from gensim.models import KeyedVectors, FastText
from gensim.scripts import glove2word2vec


class Signs:

    '''LOAD SPACY MODEL

    The default option 'en' loads the spacy default vectors.
    Alternative a local vector file can be loaded or one of the
    other spacy vectors.

    trained_vectors :: name or path to the pre-trained vector file
    backend :: either 'spacy' or 'gensim'
    mode :: applies to backend 'gensim'. The options are 'glove', 'word2vec',
            and 'fasttext'
    temp :: filename for glove to word2vec conversion
    binary :: if the vector file format is binary or not

    '''

    def __init__(self,
                 trained_vectors='en',
                 backend='spacy',
                 mode=None,
                 temp='signs_temp.sig',
                 binary=False):

        self.backend = backend
        self.mode = mode
        self.temp = temp
        self.binary = binary
        self.trained_vectors = trained_vectors
        self._null = self.load_model()

    def load_model(self):

        if self.backend == 'spacy':
            self.model = sp.load(self.trained_vectors)

        elif self.backend == 'gensim':

            if self.mode is None:
                self.mode = 'glove'

            if self.mode == 'glove':
                glove2word2vec(self.trained_vectors, self.temp)
                self.model = KeyedVectors.load_word2vec_format(self.temp,
                                                               binary=self.binary)
                os.remove(self.temp)

            elif self.mode == 'word2vec':
                self.model = KeyedVectors.load_word2vec_format(self.trained_vectors,
                                                               binary=self.binary,
                                                               encoding='latin-1')
            elif self.mode == 'fasttext':
                self.model = FastText.load_fasttext_format(self.trained_vectors,
                                                           encoding='latin-1')

    def vectors(self, word):

        '''GET VECTOR REPRESENTATION

        Takes as input a string (word or sentence) and
        returns the vector representation based on trained vectors.

        '''

        if self.backend == 'spacy':
            return self.model(word).vector

        elif self.backend == 'gensim':
            return self.model[word]

    def similarity(self, word1, word2):

        '''WORD SIMILARITY
        Takes as input two words and returns similarity.

        PARAMS
        ------
        word1 :: a string
        word2 :: another string


        EXAMPLE
        -------
        get = Signs(backend='gensim',
        trained_vectors="e:/signs_dev/vectors/glove/glove.twitter.27B.25d.txt")
        get.similarity('donald', 'trump')

        '''

        if self.backend == 'gensim':
            return self.model.similarity(word1, word2)

        if self.backend == 'spacy':

            a = nlp(word1)
            b = nlp(word2)

            return a.similarity(b)
