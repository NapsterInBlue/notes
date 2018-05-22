---
title: "Create A Range"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Create a range using Scala."
type: technical_note
draft: false
---
## Create A Range 1 to 10


```scala
// Create a range between 1 and 10
1 to 10
```




    Range(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



## Create A Range In An Array


```scala
// Create an array between 1 and 10 and put in an array
(1 to 10).toArray
```




    Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



## Use A Range In A For Loop


```scala
// For each 1 in 1,2,3,4,5
for (i <- 1 to 10) 
    // Print i
    println("index: "+ i)
```

    index: 1
    index: 2
    index: 3
    index: 4
    index: 5
    index: 6
    index: 7
    index: 8
    index: 9
    index: 10

