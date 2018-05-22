---
title: "Parse HTML"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to parse HTML for machine learning in Python.  "
type: technical_note
draft: false
---
## Preliminaries


```python
# Load library
from bs4 import BeautifulSoup
```

## Create HTML


```python
# Create some HTML code
html = "<div class='full_name'><span style='font-weight:bold'>Masego</span> Azra</div>"
```

## Parse HTML


```python
# Parse html
soup = BeautifulSoup(html, "lxml")

# Find the div with the class "full_name", show text
soup.find("div", { "class" : "full_name" }).text
```




    'Masego Azra'


