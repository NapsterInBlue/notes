---
title: "N Dimension Arrays"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "N dimension arrays using Scala."
type: technical_note
draft: false
---
## Create 2 x 2 Array


```scala
// Set the number of rows and columns
val rows = 2
val columns = 2

// Create an array of integers that is 2x2
val matrix = Array.ofDim[Int](rows, columns)
```


```scala
// View array
matrix
```




    Array(Array(0, 0), Array(0, 0))



## Add Values To Array


```scala
// First row, first column
matrix(0)(0) = 1

// First row, second column
matrix(0)(1) = 0

// Second row, first column
matrix(1)(0) = 0

// Second row, second column
matrix(1)(1) = 1
```


```scala
// View array
matrix
```




    Array(Array(1, 0), Array(0, 1))


