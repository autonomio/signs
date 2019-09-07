def lists_to_list(list_of_lists):

    '''Takes in list of lists and makes it into a flat list'''

    return [item for sublist in list_of_lists for item in sublist]


def strings_to_tokens(docs):

    '''Converts list-of-lists where each sublist
    is a string, to list-of-lists where each sublist
    consist of tokens'''

    return [doc[0].split() for doc in docs if doc[0] is not None]


def docs_to_list(docs):

    '''convert list of sentences to list of word'''

    return [word for line in docs for word in line.split()]


def docs_to_blob(docs):

    '''takes in list of words or sentences
    and returns a single blob of text.'''

    return ' '.join(word for word in docs)


def lists_to_blob(docs):

    return ' '.join([''.join(doc) for doc in docs if doc is not None])


def create_tokens(docs, flatten=True, clean=True):

    '''Takes in a list-of-lists where each sublist
    contains of a string. For example, a paragraph.

    Returns a single list where strings have
    been converted into tokens.'''

    from signs import Clean

    if clean:
        docs = [[Clean(doc, auto=True).text] for doc in docs]

    tokens = strings_to_tokens(docs)

    if flatten:
        return lists_to_list(tokens)
    else:
        return tokens
