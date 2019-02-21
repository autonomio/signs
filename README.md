<h1 align="center">
  <br>
  <a href="http://autonom.io"><img src="https://raw.githubusercontent.com/autonomio/signs/master/logo.png" alt="Signs" width="300"></a>
  <br>
</h1>

<h3 align="center">Text processing for Deep Learning</h3>

<p align="center">

  <a href="https://travis-ci.org/autonomio/talos">
    <img src="https://img.shields.io/travis/autonomio/signs/master.svg?style=for-the-badge&logo=appveyor" alt="Talos Travis">
  </a>

  <a href="https://coveralls.io/github/autonomio/talos">
    <img src="https://img.shields.io/coveralls/github/autonomio/signs.svg?style=for-the-badge&logo=appveyor" alt="Talos Coveralls">
  </a>

</p>

<p align="center">
  <a href="#Key-Features">Key Features</a> •
  <a href="#Examples">Examples</a> •
  <a href="#Install">Install</a> •
  <a href="#Support">Support</a> •
  <a href="https://autonomio.github.io/docs_signs">Docs</a> •
  <a href="https://github.com/autonomio/sigs/issues">Issues</a> •
  <a href="#License">License</a> •
  <a href="https://github.com/autonomio/signs/archive/master.zip">Download</a>
</p>
<hr>
<p align="center">
Signs unifies Gensim and SpaCy <strong>vectorization backends for Keras users</strong>. Signs provides an easy-to-use vectorization solution to manage complex preprocessing, vectorization, and evaluation workflows through <strong>intuitive one-line commands</strong>.
</p>
<p align="center">
<img src='https://i.ibb.co/3NFH646/keras-model-to-talos.gif' width=550px>
</p>

### Key Features

Signs is a set of tools for text preparation, vectorization and processing and radically simplifies raw text to Keras embeddings workflow. Signs provides a meaningful replacement for dozens of lines of redundant code that are currently required to transform raw text into a a Keras Embeds layer. Key features include:

- unifies Gensim and SpaCy vectorization backends
- supports using common vector models: [GloVe](https://nlp.stanford.edu/projects/glove/), [Fasttext](https://fasttext.cc/docs/en/english-vectors.html), and [word2vec](https://en.wikipedia.org/wiki/Word2vec)
- removes NLP learning curve
- adds no more than a few lines of code to your worflow
- From text to Keras embedding layer in a single command
- Train, save, and load custom vectors
- Evaluate results after training a Keras prediction model
- Powerful text preprocessing features
- Allows completely automated text preprocessing


#### Examples

<img src=https://i.ibb.co/sVLpDH4/signs-nlp-keras-embeddings.png>
[get source code](https://gist.github.com/mikkokotila/ad0138788c93bef2b71eaccc9c95701b)

### Install

Stable version:

#### `pip install signs`

Daily development version:

#### `pip install git+https://github.com/autonomio/signs.git@daily-dev`

### Support

If you want ask a **"how can I use Talos to..."** question, the right place is [StackOverflow](https://stackoverflow.com/questions/ask).

If you found a bug or want to suggest a feature, check the [issues](https://github.com/autonomio/signs/issues) or [create](https://github.com/autonomio/signs/issues/new/choose) a new issue.


### License

[MIT License](https://github.com/autonomio/signs/blob/master/LICENSE)



