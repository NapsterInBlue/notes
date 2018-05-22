---
title: "Loop A Collection"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Loop a collection using Scala."
type: technical_note
draft: false
---
## Create A Vector Collection


```scala
val vector = Vector("Male", 2, true)
```

## Loop Over The Collection


```scala
// For each item in the collection, print the class type of the element
vector.foreach((i: Any) => println(i, i.getClass.getSimpleName))
```

    (Male,String)
    (2,Integer)
    (true,Boolean)



```scala
// For each item in the collection
vector.foreach {
    // If one of these, print "Man"
    case "Male" | "M" | "Man" | "Gentleman" | "Boy" => println("Man")
    // For everything else, print "Something Else"
    case _ => println("Something Else")
}
```

    Man
    Something Else
    Something Else

