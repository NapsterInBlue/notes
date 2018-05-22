---
title: "For Loop A Map"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "For loop a map using Scala."
type: technical_note
draft: false
---
## Create A Map


```scala
val vehicles = Map("vehicle_type" -> "Tank", 
                   "number" -> 21)
```

## Loop With Value And Index


```scala
// Create a value for the returned values, for each key and value in the map,
val numberOfVehicles = for ((key, value) <- vehicles) yield {
                         // Return the values
                         value
                       }
```


```scala
// View the returned values
numberOfVehicles
```




    List(Tank, 21)


