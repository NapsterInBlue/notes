---
title: "Tokenize Text"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to tokenize text from unstructured text data for machine learning in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Load library
from nltk.tokenize import word_tokenize, sent_tokenize
```

## Create Text Data


```python
# Create text
string = "The science of today is the technology of tomorrow. Tomorrow is today."
```

## Tokenize Words


```python
# Tokenize words
word_tokenize(string)
```




    ['The',
     'science',
     'of',
     'today',
     'is',
     'the',
     'technology',
     'of',
     'tomorrow',
     '.',
     'Tomorrow',
     'is',
     'today',
     '.']



## Tokenize Sentences


```python
# Tokenize sentences
sent_tokenize(string)
```




    ['The science of today is the technology of tomorrow.', 'Tomorrow is today.']


