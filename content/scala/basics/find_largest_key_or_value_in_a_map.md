---
title: "Find Largest Key Or Value In A Map"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Find largest key or value in a map using Scala."
type: technical_note
draft: false
---
## Create A Map


```scala
// Create an immutable map with three key value pairs
val numbers = Map(1 -> 100, 
                  2 -> 200,
                  3 -> 300)
```

## Find Largest Key


```scala
// Find largest key
numbers.max
```




    (3,300)



## Find Largest Value


```scala
// Find the largest value
numbers.valuesIterator.max
```




    300


