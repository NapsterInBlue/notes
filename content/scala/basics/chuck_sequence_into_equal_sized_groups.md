---
title: "Chunk Sequence In Equal Sized Groups"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Chunk sequence in equal sized groups using Scala."
type: technical_note
draft: false
---
## Create An Array Sequence


```scala
// Create an array that contains arrays with first and last names
val ages = List(42,25,28,38,58,63,23,458,2569,584,25,25,878)
```

## Chunk Array Into Groups Of Two Elements


```scala
// Slide over sequence, create a list of two elements, then take two steps
ages.sliding(2,2).toArray
```




    Array(List(42, 25), List(28, 38), List(58, 63), List(23, 458), List(2569, 584), List(25, 25), List(878))



## Chunk Array Into Groups Of Two Elements, With Overlap


```scala
// Slide over sequence, create a list of two elements, then take one step
ages.sliding(2,1).toArray
```




    Array(List(42, 25), List(25, 28), List(28, 38), List(38, 58), List(58, 63), List(63, 23), List(23, 458), List(458, 2569), List(2569, 584), List(584, 25), List(25, 25), List(25, 878))


