---
title: "Breaking Up String Variables"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Breaking up string variables."
type: technical_note
draft: false
---
### Basic name assignment


```python
variableName = 'This is a string.'
```

### List assignment


```python
One, Two, Three = [1, 2, 3]
```

### Break up a string into variables


```python
firstLetter, secondLetter, thirdLetter, fourthLetter = 'Bark'
```


```python
firstLetter
```




    'B'




```python
secondLetter
```




    'a'




```python
thirdLetter
```




    'r'




```python
fourthLetter
```




    'k'



### Breaking up a number into separate variables


```python
firstNumber, secondNumber, thirdNumber, fourthNumber = '9485'
```


```python
firstNumber
```




    '9'




```python
secondNumber
```




    '4'




```python
thirdNumber
```




    '8'




```python
fourthNumber
```




    '5'



### Assign the first letter of 'spam' into varible a, assign all the remaining letters to variable b


```python
a, *b = 'spam'
a
```




    's'




```python
b
```




    ['p', 'a', 'm']


