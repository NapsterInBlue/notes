---
title: "Generate Tweets Using Markov Chains"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Generate tweets using Markov Chains in Python."
type: technical_note
draft: false
---
## Preliminaries


```python
import markovify
```

## Load Corpus

The corpus I am using is just one I found online. The corpus you choose is central to generating realistic text.


```python
# Get raw text as string
with open("brown.txt") as f:
    text = f.read()
```

## Build Markov Chain


```python
# Build the model.
text_model = markovify.Text(text)
```

# Generate One Tweet


```python
# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(text_model.make_short_sentence(140))
```

    Within a month, calls were still productive and most devotees of baseball attended the dozens of them.
    Even death, therefore, has a leather bolo drawn through a local rajah in 1949.
    He had a rather sharp and confident.

