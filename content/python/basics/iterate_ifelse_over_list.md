---
title: "Iterate An Ifelse Over A List"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Iterate an ifelse over a list in Python."
type: technical_note
draft: false
---
## Create some data


```python
word_list = ['Egypt', 'Watching', 'Eleanor']

vowels = ['A', 'E', 'I', 'O', 'U']
```

## Create a for loop


```python
# for each item in the word_list,
for word in word_list:
    # if any word starts with e, where e is vowels,
    if any([word.startswith(e) for e in vowels]):
        # then print is valid,
        print('Is valid')
    # if not,    
    else:
        # print invalid
        print('Invalid')
```

    Is valid
    Invalid
    Is valid

