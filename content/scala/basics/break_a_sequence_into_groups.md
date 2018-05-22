---
title: "Break A Sequence Into Groups"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Break a sequence into groups using scala."
type: technical_note
draft: false
---
## Create An Array Sequence


```scala
// Create an array that contains arrays with first and last names
val ages = List(42,25,28,38,58,63,23,458,2569,584,25,25,878)
```

## Group Array By Anonymous Function


```scala
// If an element is even, return True, if not, return False
val isEven = ages.groupBy(_ % 2 == 0)
```

## View Groups


```scala
// View group that is evens
evensOdds(true)
```




    List(42, 28, 38, 58, 458, 584, 878)




```scala
// View group that is odds
evensOdds(false)
```




    List(25, 63, 23, 2569, 25, 25)


