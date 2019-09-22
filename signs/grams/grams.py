class Grams:

    def __init__(self, text):

        '''Takes in a list of words representing a document
        and returns a list of ngrams or skipgrams.

        text : list
            A list of words representing a document.

        '''

        self._text = text
        self._counter = len(text)

    def ngrams(self, ngram=2, skip=0):

        '''Produce ngrams or skipgrams.

        ngram: int
            Number of words per gram.
        skip : int
            The number of words to skip for each gram'''

        # the output
        out = []

        # process the doc word-by-word
        for i in range(self._counter):
            try:
                # create the list for single instance of grams
                words = [self._text[i]]

                # find the grams
                for ii in range(ngram - 1):
                    words.append(self._text[i + ii + 1 + skip])

                # add to the output
                out.append(words)

            # handle the case where end is near
            except IndexError:
                pass

        return out

    def combinations(self, length=3):

        '''Produce every possible combination of n length.

        length | int | length of the combinations
        '''

        import itertools

        out = []

        for i in list(itertools.combinations(self._text, length)):
            if len(i) == len(set(i)):
                out.append(i)

        return out

    def flexgrams(self, length=3, flex_n=1):

        '''Simple flexgram where all combinations of certain length
        are returned, but n items are randomly dropped. The final
        length must be shorter than number of items minus flex_n

        length | int | length of the resulting combinations
        flex_n | int | the number of items to randomly drop

        '''
        import random
        import itertools

        combinations = list(itertools.combinations(self._text, length))

        out = []

        for i in [random.choices(i, k=length-flex_n) for i in combinations]:
            if len(i) == len(set(i)):
                if i not in out:
                    out.append(i)

        return out

    def sobolgrams(self, length=3, n=2):

        '''Sobolgram is a random variation of a flexgram, where
        instead of following a sequential order of strings and then
        randomly dropping words, there is no order at all and grams
        are formed based on random pick within the doc.

        length | int | length of the resulting combinations
        n | int | number of grams to draw

        '''

        import random

        out = []

        while len(out) < n:

            gram = random.choices(self._text, k=length)

            if len(set(gram)) == length:
                if gram not in out:
                    out.append(gram)

        return out

    def skipgrams(self, length=3, skip_nth=2):

        '''Simple flexgram where all combinations of certain length
        are returned, but n items are randomly dropped. The final
        length must be shorter than number of items minus flex_n

        length | int | length of the resulting combinations
        skip_nth | int | the number of item to skip

        '''

        import itertools
        import numpy as np

        combinations = list(itertools.combinations(self._text, length))

        # create indicies
        indicies = list(range(length))
        indicies.remove(skip_nth)

        out = []

        for i in [np.array(i)[indicies].tolist() for i in combinations]:
            if i not in out:
                out.append(i)

        return out
