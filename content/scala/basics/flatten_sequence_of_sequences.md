---
title: "Flatten Sequence Of Sequences"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Flatten sequence of sequences using Scala."
type: technical_note
draft: false
---
## Create An Array Sequence


```scala
// Create an array that contains arrays with first and last names
val fullNames = Array(
    Array("Jason", "Miller"),
    Array("Jason", "Miller"), // Duplicate
    Array("Sally", "Fields"),
    Array("Betty", "Johnson")
)
```

## Flatten The Sequence 


```scala
// Flatten the sequence
fullNames.flatten
```




    Array(Jason, Miller, Jason, Miller, Sally, Fields, Betty, Johnson)



## Flatten The Sequence And Only Keep Unique Values


```scala
// Flatten the sequence and remove any duplicates
fullNames.flatten.distinct
```




    Array(Jason, Miller, Sally, Fields, Betty, Johnson)


