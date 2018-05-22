---
title: "Partial Functions"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Partial functions using Scala."
type: technical_note
draft: false
---
`isDefinedAt` determines which inputs are accepted. `apply` is the actual operation.

## Create A Partial Function


```scala
// Create a new partial function that inputs a integer and outputs a string
val dayOfTheWeek = new PartialFunction[Int, String] {
    // Create an array with the days of the week
    val days = Array("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    
    // Only accept input integers that are between 0 and 6
    def isDefinedAt(i: Int) = i > 0 && i < 6
    
    // If accepted, return the correct day of the week string
    def apply(i: Int) = days(i-1)
}
```

## Run The Partial Function


```scala
dayOfTheWeek(2)
```




    Tuesday


