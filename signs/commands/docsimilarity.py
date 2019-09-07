class DocSimilarity:
    
    def __init__(self, model, docs):
        
        from signs.similarity import doc_similarity as sims
        from signs.utils.html_print import html_print
        
        self._sims = sims
        self._model = model
        self._docs = docs
        self._html_print = html_print
        
    def seen_matrix(self):
        
        '''creates a 2d matrix with similarities'''
    
        return self._sims.seen_similarity_matrix(self._model)

    def unseen_matrix(self, docs):
        
        '''same as above but for unseen docs'''
        
        return self._sims.unseen_similarity_matrix(self._model, docs)

    def similar_docs(self, doc):
    
        '''for comparing a single doc against all seen docs'''
        return self._sims.similarity_docs(doc, self._model)

    def spatial_distance(self, doc1, doc2):
        
        '''for comparing two unseen or seen docs'''
        return self._sims.vector_spatial_distance(self._model,
                                                  doc1,
                                                  doc2)
    
    def preview_results(self, docs=None):
        
        if docs is None:
            # get the keys from docs with similarities
            similarities = self._get_similarities(self._docs.docs())
        else:
            similarities = self._get_similarities(docs)
        
        # print out the highest and lowest match
        self._print_highest(similarities)
        self._print_lowest(similarities)
    

    def _get_similarities(self, docs):

        import random

        # pick a ramdom document
        doc_id = random.randint(0, len(docs))

        # find similar documents
        similarities = self._sims.similarity_docs(docs[doc_id], self._model)

        return similarities

    def _print_highest(self, similarities):

        # create content
        text = self._docs.docs(False)[list(similarities.keys())[0]][0]

        # create similarity value and round
        similarity = similarities[list(similarities.keys())[0]]
        similarity = round(similarity, 4)

        # parse together the title
        title = "HIGHEST MATCH : " + str(similarity)

        # print it out
        self._html_print(text, title)


    def _print_lowest(self, similarities):

        # create content
        text = self._docs.docs(False)[list(similarities.keys())[-1]][0]

        # create similarity value and round
        similarity = similarities[list(similarities.keys())[-1]]
        similarity = round(similarity, 4)

        # parse together the title
        title = "LOWEST MATCH : " + str(similarity)

        # print it out
        self._html_print(text, title)