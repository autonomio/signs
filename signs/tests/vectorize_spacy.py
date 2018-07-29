from signs.vectorize.spacy import spacy_load, spacy_word2vec


def run_test():

	model = spacy_load()
	model = spacy_load('en')

	if sum(spacy_word2vec('test', model)) != 2.406518764793873:
	    raise ValueError('spacy_word2vec() test failed')

	if sum(spacy_word2vec('testing sentence', model)) != -0.7180192619562149:
	    raise ValueError('spacy_word2vec() test failed')