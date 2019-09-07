def similarity_docs(doc, model):
    
    '''Computes similarity scores for docs in the
    training corpus based on input doc.'''

    vecs = model.infer_vector(doc)
    sims = model.docvecs.most_similar([vecs],  topn=len(model.docvecs))
    
    return dict(sims)

def seen_similarity_matrix(model):
    
    '''Computes a similarity matrix for all the docs
    in the training corpus or in a set of documents
    based on the trained model.'''
    
    import numpy as np
    
    similarities = []
    out = []
    
    for i in range(len(model.docvecs)):
        
        # get similarities
        sims = model.docvecs.most_similar([model.docvecs[i]],
                                          topn=len(model.docvecs))

        # add to a list in dictionary format
        similarities.append(dict(sims))
    
    for sims in similarities:
        
        temp = []
        
        for i in range(len(sims)):
            temp.append(sims[i])
        
        out.append(temp)

    return np.array(out)


def unseen_similarity_matrix(model, docs):
    
    '''Computes a similarity matrix for unseen documents
    based on a trained doc2vec model.'''

    import numpy as np
    
    out = []
    
    for doc in docs:
        temp = []
        for i in range(len(docs)):
            sim = model.docvecs.similarity_unseen_docs(model, doc, docs[i])
            temp.append(sim)
        out.append(temp)
        
    return np.array(out)

def vector_spatial_distance(model, doc1, doc2):
    
    '''>> EXPERIMENTAL <<
    
    Computes spatial distance cosine for two documents
    based on a trained model.'''
    
    import scipy

    vec1 = model.infer_vector(doc1)
    vec2 = model.infer_vector(doc2)
    
    return 1 - scipy.spatial.distance.cosine(vec1, vec2)