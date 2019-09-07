class Transform:

    def __init__(self, documents):

        '''Accepts input docs as list-of-lists where
        each sublist consist of a string value representing
        a single document, for example a paragraph.'''

        self._documents = documents

    def docs(self, clean=True, stopwords=True):

        '''Returns list-of-lists of strings'''

        from signs import Clean

        if clean:
            return [[Clean(doc, auto=True).text] for doc in self._documents]

        return self._documents

    def tokens(self, clean=True, stopwords=True):

        '''Returns a list-of-lists of tokens'''

        from signs.preprocess import create_tokens

        return create_tokens(self._documents, flatten=False, clean=clean)

    def tokens_flat(self, clean=True, stopwords=True):

        '''Returns a flattened list of tokens'''

        from signs.preprocess import create_tokens

        return create_tokens(self._documents, flatten=True, clean=clean)

    def docs_flat(self, clean=True, stopwords=True):

        '''Returns a flatted list of strings'''

        from signs.preprocess import lists_to_list

        return lists_to_list(self._documents)

    def docs_string(self, clean=True, stopwords=True):

        '''Returns a single string with blobbed documents'''

        from signs import Clean
        from signs.preprocess import lists_to_blob

        if clean:
            return lists_to_blob(
                [Clean(doc, auto=True).text for doc in self._documents])
        else:
            return lists_to_blob(self._documents)
