from signs.vectorize.spacy import spacy_load, spacy_word2vec


def run_test():

    model = spacy_load()
    model = spacy_load('en')

    test = round(sum(spacy_word2vec('test', model)), 2)
    test2 = round(sum(spacy_word2vec('testing sentence', model)), 2)

    if test != 2.41:
        raise ValueError('spacy_word2vec() test failed with %f' % test)

    if test2 != -0.72:
        raise ValueError('spacy_word2vec() test failed with %f' % test)
