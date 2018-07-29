from signs.vectorize.spacy import spacy_load, spacy_word2vec


def run_test():

    model = spacy_load()
    model = spacy_load('en')

    if round(sum(spacy_word2vec('test',
                                model)), 2) != 2.40:
        raise ValueError('spacy_word2vec() test failed')

    if round(sum(spacy_word2vec('testing sentence',
                                model)), 2) != -0.72:

        raise ValueError('spacy_word2vec() test failed')
