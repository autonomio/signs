class Describe:

    def __init__(self, tokens):

        '''Takes in a list with tokens.'''

        from signs.preprocess import lists_to_list

        if isinstance(tokens[0], str):
            self.tokens = tokens
        if isinstance(tokens[0], list):
            self.tokens = lists_to_list(tokens)

    def get_counts(self):

        '''Get word frequencies for the aggregate
        of all the tokens in Describe() input.'''

        from collections import Counter

        # return the counted values as dictionary
        return dict(Counter(self.tokens).most_common())

    def get_gram_counts(self, ngram=3, skip=0):

        '''Returns ngram counts. Supports skipgrams.

        docs : list
            A list of lists where each sublist contains a string.
        ngram : int
            The value for 'n' in ngram. For example, 2 for bigram.
        skip : int
            The value for skipgrams. For example, 3 to skip three tokens
        '''

        from collections import Counter
        from signs import Grams, preprocess

        temp = [Grams(self.tokens).ngrams(ngram, skip)]
        temp = preprocess.lists_to_list(temp)
        temp = [' '.join(i) for i in temp]

        return dict(Counter(temp).most_common())
