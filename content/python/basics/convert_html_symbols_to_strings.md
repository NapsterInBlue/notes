---
title: "Convert HTML Characters To Strings"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Convert HTML Characters To Strings Using Python."
type: technical_note
draft: false
---

```python
## Preliminaries
```


```python
import html
```


```python
## Create Text
```


```python
text = 'This item costs &#165;400 or &#163;4.'
```


```python
## Convert To String
```


```python
html.unescape(text)
```




    'This item costs ¥400 or £4.'




```python
## Convert To HTML Entities
```


```python
html.escape(text)
```




    'This item costs &amp;#165;400 or &amp;#163;4.'


