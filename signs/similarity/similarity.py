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

            a = self.model(word1)
            b = self.model(word2)

            return a.similarity(b)
