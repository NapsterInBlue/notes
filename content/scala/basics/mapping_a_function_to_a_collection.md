---
title: "Mapping A Function To A Collection"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Mapping a function to a collection using Scala."
type: technical_note
draft: false
---
## Preliminaries


```scala
import scala.collection.mutable.ArrayBuffer
```

## Create Collection


```scala
// Create an array of strings
var birds = ArrayBuffer("Hawk", "Condor", "Eagle", "Pigeon")
```

## Create Function


```scala
// Create a function that returns the length of a string
val getLength = (i: String) => i.length
```

## Map The Function To The Collection


```scala
// Map the function to the array
birds.map(getLength)
```




    ArrayBuffer(4, 6, 5, 6)



## Map An Anonymous Function To The Collection


```scala
// Map the anonymous function to the collection
birds.map(_.toUpperCase)
```




    ArrayBuffer(HAWK, CONDOR, EAGLE, PIGEON)


