def test_stopwords():

	from signs import Stopwords, Transform

	doc = ' Jack is a green  😂😂😂 cat... \n with a hat \n  '

	# transform doc/s to the right format
	tokens = Transform([doc]).tokens()

	# filter the docs
	filtered_tokens = Stopwords(tokens)

	# then access the filtered docs
	filtered_tokens.docs

	# set minimum length for words
	Stopwords(tokens, min_length=3)

	# set maximum threshold for words (accept all words above this)
	Stopwords(tokens, max_threshold=8)

	# add custom words
	Stopwords(tokens, add_stopwords=['jack'])

	# just use custom words
	Stopwords(tokens, common_stopwords=False, add_stopwords=['jack']).docs