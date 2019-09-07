def gensim_doc2vec_train(docs):
    
    '''Trains a gensim doc2vec model based on a training corpus. 
    Returns the trained model and the training docs.
    
    NOTE: the input docs format is list-of-lists where each
    sublists consist of tokenized document.

    EXAMPLE:

        model, train_corpus = gensim_doc2vec_train(docs[:400])
        test_corpus = docs[400:]

    '''

    from gensim.models.doc2vec import Doc2Vec, TaggedDocument

    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(docs)]
    
    model = Doc2Vec(vector_size=50, 
                    window=2,
                    min_count=2,
                    workers=4,
                    epochs=50)
    
    model.build_vocab(documents)
    
    model.train(documents,
                total_examples=model.corpus_count,
                epochs=model.epochs)
    
    return model, documents