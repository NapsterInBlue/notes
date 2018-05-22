---
title: "Make Numbers Pretty"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Make numbers pretty using Scala."
type: technical_note
draft: false
---
## Load The NumberFormat Library


```scala
// Make value that is assigned to an instance of numberformat
val make_pretty = java.text.NumberFormat.getInstance
```

## Make An Integer Pretty


```scala
// Format 10000 to 10,000
make_pretty.format(10000)
```

## Make A Float Pretty


```scala
// Format to 10000.1928 to 10,000.193
make_pretty.format(10000.1928)
```




    10,000.193



## Load The NumberFortmat Library Set For European Numbers


```scala
// Set the locale to germany
val germany = new java.util.Locale("de", "DE")

// Make value that is assigned to an instance of numberformat set to germany
val make_pretty_de = java.text.NumberFormat.getIntegerInstance(germany)
```

## Make An Integer Pretty


```scala
// Format 1000000 to 1.000.000
make_pretty_de.format(1000000)
```




    1.000.000


