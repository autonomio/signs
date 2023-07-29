def spacy_load(trained_vectors='en'):

    '''LOAD SPACY MODEL

    The default option 'en' loads the spacy default vectors.
    Alternative a local vector file can be loaded or one of the
    other spacy vectors.

    '''

    import spacy

    if trained_vectors == 'en':

        import en_core_web_sm
        return en_core_web_sm.load()

    else:
        return spacy.load(trained_vectors)


def spacy_word2vec(string, model):

    '''GET VECTOR REPRESENTATION

    Takes as input a string (word or sentence) and
    returns the vector representation based on trained vectors.

    '''

    return model(string).vector
