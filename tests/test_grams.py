def test_grams():

    from signs import Grams

    docs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    grams = Grams(docs)

    grams.combinations()
    grams.flexgrams()
    grams.ngrams()
    grams.skipgrams()
    grams.sobolgrams(n=50)
