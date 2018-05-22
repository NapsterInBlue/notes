---
title: "Stemming Words"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to stem words in unstructured text data for machine learning in Python."
type: technical_note
draft: false
---
<a alt="Stemming Words" href="https://machinelearningflashcards.com">
    <img src="/images/machine_learning_flashcards/Stemming_Words_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load library
from nltk.stem.porter import PorterStemmer
```

## Create Text Data


```python
# Create word tokens
tokenized_words = ['i', 'am', 'humbled', 'by', 'this', 'traditional', 'meeting']
```

## Stem Words

Stemming reduces a word to its stem by identifying and removing affixes (e.g. gerunds) while keeping the root meaning of the word. NLTK's `PorterStemmer` implements the widely used Porter stemming algorithm.


```python
# Create stemmer
porter = PorterStemmer()

# Apply stemmer
[porter.stem(word) for word in tokenized_words]
```




    ['i', 'am', 'humbl', 'by', 'thi', 'tradit', 'meet']


