---
title: "Zip Together Two Lists"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Zip Together Two Lists Using Scala."
type: technical_note
draft: false
---
## Create Two Vectors


```scala
// Create two vectors
val firstName = Vector("Steve", "Bob", "Jack", "Jill")
val lastName = Vector("Jackson", "Dillan", "Bower", "Stein")
```

## Zip Together Vectors


```scala
// Create a new variable that zips the sequences
val fullNames = firstName zip lastName
```


```scala
// View the zipped sequences and convert to a map
fullNames
```




    Vector((Steve,Jackson), (Bob,Dillan), (Jack,Bower), (Jill,Stein))


