---
title: "Try, Catch, Finally"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Try, Catch, Finally Using Scala."
type: technical_note
draft: false
---
## Create Some Operation That Will Cause An Exception


```scala
"Sixteen".toFloat
```




    Name: java.lang.NumberFormatException
    Message: For input string: "Sixteen"
    StackTrace:   at sun.misc.FloatingDecimal.readJavaFormatString(FloatingDecimal.java:2043)
      at sun.misc.FloatingDecimal.parseFloat(FloatingDecimal.java:122)
      at java.lang.Float.parseFloat(Float.java:451)
      at scala.collection.immutable.StringLike$class.toFloat(StringLike.scala:280)
      at scala.collection.immutable.StringOps.toFloat(StringOps.scala:29)



## Try, Catch, Finally


```scala
// Try
try {
    // The bad operation
    "Sixteen".toFloat
// Catch any problems
} catch {
    // If it is an exception, print something
    case e: Exception => println("Something went wrong")
} finally {
    // Regardless of if there is an error or not, print this
    println("We are finally done.")
}
```

    Something went wrong
    We are finally done.





    ()


