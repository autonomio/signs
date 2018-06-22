<img src='https://raw.githubusercontent.com/autonomio/signs/master/logo.png'>

[![Build Status](https://travis-ci.org/autonomio/signs.svg?branch=master)](https://travis-ci.org/autonomio/signs) [![Coverage Status](https://coveralls.io/repos/github/autonomio/signs/badge.svg?branch=master)](https://coveralls.io/github/autonomio/signs?branch=master) [![CodeFactor](https://www.codefactor.io/repository/github/autonomio/signs/badge)](https://www.codefactor.io/repository/github/autonomio/signs)

A set of tools for text preparation, vectorization and processing.


## features 

- preprocessing
- vectorization model training
- document vectorization
- similarity


### preprocessing 

- remove stopwords
- remove punctuations
- to lower 
- capitalization
- remove line breaks
- remove emojis and other icons
- remove trailing and leading whitespace
- remove tabs 
- surpress whitespaces (trim to one)

### vectorization model training 

- train custom model with gensim

### document vectorization 

- character level embeddings 
- word level embeddings
- gensim doc2vec 
- gensim sent2vec
- gensim word2vec 
- spacy word2vec

### similarity

- Annoy
- Spacy similarity
