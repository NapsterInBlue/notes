---
title: "Iterate Over A Map"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Iterate over a map using Scala."
type: technical_note
draft: false
---
## Create A Map


```scala
// Create a map with three key value pairs
val prices = Map("Video Card" -> 200.00,
                 "Motherboard" -> 400.00,
                 "CPU" -> 100.00)
```

## Loop Over A Map


```scala
// for each key and value in prices
for ((k,v) <- prices) yield {
    // Return the value plus 100
    v+100
}
```




    List(300.0, 500.0, 200.0)



## Apply Function To Each Map Value


```scala
// Increase each value in the map by 1000
prices.mapValues(_+1000)
```




    Map(Video Card -> 1200.0, Motherboard -> 1400.0, CPU -> 1100.0)


