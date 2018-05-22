---
title: "Filter A Sequence"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Filter A Sequence using Scala."
type: technical_note
draft: false
---
## Create An Array Sequence


```scala
// Create an array that contains arrays with first and last names
val ages = Array(42,25,28,38,58,63,23,458,2569,584,25,25,878)
```

## Elements Less Than 100


```scala
ages.filter(_ < 100)
```




    Array(42, 25, 28, 38, 58, 63, 23, 25, 25)



## Elements Greater Than 100


```scala
ages.filter(_ >= 100)
```




    Array(458, 2569, 584, 878)



## Elements That Are Even


```scala
ages.filter(_ % 2 == 0)
```




    Array(42, 28, 38, 58, 458, 584, 878)


