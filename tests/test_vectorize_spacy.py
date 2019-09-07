def test_vectorize_spacy():

	from signs.vectorize.spacy import spacy_load, spacy_word2vec

	model = spacy_load()
	model = spacy_load('en')

	test = round(sum(spacy_word2vec('test', model)), 2)
	test2 = round(sum(spacy_word2vec('testing sentence', model)), 2)
