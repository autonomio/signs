class Transform:
    
    def __init__(self, documents):
        
        '''Accepts input docs as list-of-lists where
        each sublist consist of a string value representing
        a single document, for example a paragraph.'''
        
        from signs.preprocess import create_tokens
        from signs.preprocess import lists_to_list
        from signs.preprocess import lists_to_blob
        from signs import Clean
        
        self.documents = documents
        self.create_tokens = create_tokens
        self.lists_to_list = lists_to_list
        self.lists_to_blob = lists_to_blob
        self.Clean = Clean
    
    def docs(self, clean=True):
        
        '''Returns list-of-lists of strings'''
        
        if clean:
            return [self.Clean(doc, auto=True).text for doc in self.documents]
        else:
            return self.documents
    
    def tokens(self, clean=True):
        
        '''Returns a list-of-lists of tokens'''
        
        return self.create_tokens(self.documents, flatten=False, clean=clean)
    
    def tokens_flat(self, clean=True):
        
        '''Returns a flattened list of tokens'''
        
        return self.create_tokens(self.documents, flatten=True, clean=clean)
    
    def docs_flat(self, clean=True):
        
        '''Returns a flatted list of strings'''
        
        return self.lists_to_list(self.documents)
    
    def docs_string(self, clean=True):
        
        '''Returns a single string with blobbed documents'''

        if clean:
            return self.lists_to_blob(
                [self.Clean(doc, auto=True).text for doc in self.documents])
        else:
            return self.lists_to_blob(self.documents)
