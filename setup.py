from distutils.core import setup

setup(name='Siamese CBOW',
      version='1.0',
      description='Siamese CBOW is a neural network architecture for calculating word embeddings optimised for being averaged across sentences to produce sentence representations.',
      py_modules=['wordEmbeddings','siamese-cbow'],
      install_requires=[
          'gensim',
          'lasagne',
          'theano'
      ])
