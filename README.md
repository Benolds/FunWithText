FunWithText
===========

A collection of python scripts performing various operations on large bodies of text.

Contents
========

bigram_markov_text_generator.py
-------------------------------
Uses a markov probability model to generate a body of text given document(s) to emulate. Generates each word with a probability dependent on how frequently it appears after a previous word in the original document. By default this runs on 'nobel-opening-address.txt'

Also works well when given a collection of essays. Has been known to make profound insights.

count_most_frequent_words.py
----------------------------
An optimized method for returning a sorted list of the most frequent words appearing in a body of text. By default this runs on 'lorem-ipsum-text.txt'