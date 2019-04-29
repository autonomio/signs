class Describe:

	def __init__(self, tokens):

		self.tokens = tokens

	def get_counts(self):

	    from collections import Counter

	    '''Takes in a list-of-lists where each sublist
	    contains a string value such as paragraph.'''
	 
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
