---
title: "Random Integer Between Two Values"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Random Integer Between Two Values using Scala."
type: technical_note
draft: false
---
## Load Random


```scala
// Create a value that is the random package
val random = new scala.util.Random
```

## Create A Start And End


```scala
// Create a start and end value pair
val start = -10
val end = 10
```

## Generate Random Integer Between The Start And End Values


```scala
// Then generate a random integer between 0 and the different between end and start + 1
//(to make it inclusive), then shift the value into the desired range by added the start value
start + random.nextInt( (end - start) + 1 )  
```




    1


