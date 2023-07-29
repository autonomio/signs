class LoadVectors:

    '''Load, train, and

    The default option 'en' loads the spacy default vectors.
    Alternative a local vector file can be loaded or one of the
    other spacy vectors.

    trained_vectors :: name or path to the pre-trained vector file. 
                       If set to 'en' then spacy small web vectors 
                       will be used.
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

        import os

        if self.backend == 'spacy':

            import spacy as sp

            if self.trained_vectors == 'en':

                import en_core_web_sm
                self.model = en_core_web_sm.load()
            
            else:
                self.model = sp.load(self.trained_vectors)

        elif self.backend == 'gensim':

            from gensim.models import KeyedVectors, FastText
            from gensim.scripts.glove2word2vec import glove2word2vec

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
