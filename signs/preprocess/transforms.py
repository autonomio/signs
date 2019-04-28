def lists_to_list(list_of_lists):
    
    '''Takes in list of lists and makes it into a flat list'''
    
    return [item for sublist in list_of_lists for item in sublist]

def strings_to_tokens(docs):
    
    '''Converts list-of-lists where each sublist
    is a string, to list-of-lists where each sublist
    consist of tokens'''

    return [doc[0].split() for doc in docs if doc[0] is not None]