<img src='https://raw.githubusercontent.com/autonomio/signs/master/logo.png'>

[![Build Status](https://travis-ci.org/autonomio/signs.svg?branch=master)](https://travis-ci.org/autonomio/signs) [![Coverage Status](https://coveralls.io/repos/github/autonomio/signs/badge.svg?branch=master)](https://coveralls.io/github/autonomio/signs?branch=master) [![CodeFactor](https://www.codefactor.io/repository/github/autonomio/signs/badge)](https://www.codefactor.io/repository/github/autonomio/signs)

A set of tools for text preparation, vectorization and processing. The below explains the functionalities included in Signs. 

## 1. features 

1.1) preprocessing

1.2) vectorization model training

1.3) vectorization

1.4) down stream applications


## 1.1. preprocessing 

- remove stopwords
- remove punctuations
- to lower 
- capitalization
- remove line breaks
- remove emojis and other icons
- remove trailing and leading whitespace
- remove tabs 
- surpress whitespaces (trim to one)


## 1.2. vectorization model training 

In order to vector words and documents, there needs to be two different options: 

- use pre-trained model such as Spacy
- train models using a custom corpus

## 1.3. vectorization

### 1.3.1 word and document vectorization

There are two types of vectorization: 

- word vectorization (single word)
- document vectorization (anything longer than a single word)

NOTE: it is the case that word vectors can be used to create document vectors using averaging[source](http://aclweb.org/anthology/P/P16/P16-1089.pdf), TF-IDF[source](http://aclweb.org/anthology/P/P16/P16-1089.pdf) and so forth. It is also the case that approaches specifically targeting document vectorization (i.e. skipping the need to vectorize words explicity first is skipped) are available.

Signs supports all three approaches: 

- word vectorization 
- word vectorization based document vectorization
- direct vectorization

### 1.3.2 other distinctions

Generally speaking the text can be treated in two ways: 

- words
- characters

Both of these can be treated directly, or by using various approaches to producing 'grams':

- ngrams
- skipgrams
- flexgrams

There are two approaches to leveraging various gram approaches; one where the documents are first transformed [example](https://github.com/keras-team/keras/blob/master/examples/imdb_fasttext.py) and the other where a an inbuilt feature of a model is used [example]((https://radimrehurek.com/gensim/models/word2vec.html))


## 1.4. Downstream Applications 

The main intended use case for Signs is to provide the suitable data for making classifications with deep learning models. Most notably:

- plain vanilla vectors 
- data for sequantial models 

There is also support for various tasks directly withing Signs for both words and documents: 

- similarity 
- part of speech tagging
- classification

## 2 Useful Links

- gensim FastText [source](https://rare-technologies.com/sent2vec-an-unsupervised-approach-towards-learning-sentence-embeddings/)
- Efficient n-gram & skipgram modelling on text corpora [source](https://proycon.github.io/colibri-core/)