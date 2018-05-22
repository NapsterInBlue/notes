---
title: "Mutable Maps"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Mutable maps using Scala."
type: technical_note
draft: false
---
## Create A Mutable Map


```scala
val army = collection.mutable.Map(
    "Tank" -> "A-1 Abrams",
    "Aircraft" -> "F35",
    "Ship" -> "Nimitz Class"
)
```

## Add An Element


```scala
// Add an element
army += ("APC" -> "Bradley IFC")

// Add an element (alternative)
army.put("Weapon", "M60")
```




    None



## Add Multiple Elements


```scala
// Add two elements
army += ("Helicopter" -> "Apache", "Missile" -> "Sidewinder")
```




    Map(Weapon -> M60, APC -> Bradley IFC, Missile -> Sidewinder, Tank -> A-1 Abrams, Aircraft -> F35, Helicopter -> Apache, Ship -> Nimitz Class)



## Remove An Element


```scala
// Remove an element
army -= "Ship"

// Remove an element (alternative)
army.remove("Tank")
```




    Some(A-1 Abrams)



## Change A Value


```scala
// Change the value of an element
army("Tank") = "Tiger Tank"
```

## Filter A Map


```scala
// Keep only the key, value pairs that meet the criteria
army.retain((k,v) => k == "Tank")
```




    Map(Tank -> Tiger Tank)


