def embeds_to_text(x_test, word_index):

    '''EMBEDS TO TEXT CONVERTER

    Takes in keras embeddings and converts it back to text.
    Note that the resulting strings are limited by max_words
    from tokenization. Use embeds_to_original() to get the full
    string instead.'''

    l = []

    for i in range(len(x_test)):

        inv_map = {v: k for k, v in word_index.items()}
        words = list(map(inv_map.get, x_test[i]))
        sentence = ' '.join([x for x in words if x is not None])
        l.append(sentence)

    return l


def embeds_to_original():

    return
