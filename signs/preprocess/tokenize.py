def tokenize(texts, num_words=None, maxlen=12, padding='post'):

    '''TOKENIZE

    Create a word index and returns padded docs in return.

    '''

    from keras.preprocessing.text import Tokenizer
    from keras.preprocessing.sequence import pad_sequences

    tokenizer = Tokenizer(num_words=num_words)
    tokenizer.fit_on_texts(texts)
    encoded_docs = tokenizer.texts_to_sequences(texts)
    word_index = tokenizer.word_index

    x = pad_sequences(encoded_docs, maxlen=maxlen, padding=padding)
    vocab_size = max(list(word_index.values())) + 1

    return x, vocab_size, word_index
