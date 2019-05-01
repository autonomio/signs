def test_transform():

	from signs import Transform

	doc = ' Jack is a green  😂😂😂 cat... \n with a hat \n  '

	docs = Transform([doc])

	# return the original docs
	docs.docs()

	# return the original docs cleaned
	docs.docs(True)

	# return original docs but flattened
	docs.docs_flat()

	# return original docs flattened and clean
	docs.docs_flat(True)

	# return original docs in a single string blob
	docs.docs_string()

	# return original docs in single string blob cleaned
	docs.docs_string(True)

	# return tokenized version of docs
	docs.tokens()

	# return tokenized version cleaned
	docs.tokens(True)

	# return tokenized and flattend
	docs.tokens_flat()

	# return tokenized and flattened clean
	docs.tokens_flat(True)