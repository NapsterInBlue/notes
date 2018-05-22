---
title: "Generator Expressions"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Generator expressions in Python."
type: technical_note
draft: false
---

```python
# Create a list of students
students = ['Abe', 'Bob', 'Christina', 'Derek', 'Eleanor']
```


```python
# Create a generator expression that yields lower-case versions of the student's names
lowercase_names = (student.lower() for student in students)
```


```python
# View the generator object
lowercase_names
```




    <generator object <genexpr> at 0x104837518>




```python
# Get the next name lower-cased
next(lowercase_names)
```




    'abe'




```python
# Get the next name lower-cased
next(lowercase_names)
```




    'bob'




```python
# Get the remaining names lower-cased
list(lowercase_names)
```




    ['christina', 'derek', 'eleanor']


