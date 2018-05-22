---
title: "Search A Map"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Search A Map using Scala."
type: technical_note
draft: false
---
## Create A Map


```scala
// Create an immutable map with three key value pairs
val staff = Map("CEO" -> "Judith Jackson", 
                "CFO" -> "Sally Shields",
                "CTO" -> "Steven Miller")
```

## Test If Key Exists


```scala
// Test if key exists
staff.contains("CTO")
```




    true



## Test If Value Exists


```scala
// Test is any value exists which contains part of a string
staff.valuesIterator.exists(_.contains("Miller"))
```




    true


