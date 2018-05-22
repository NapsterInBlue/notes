---
title: "Search Strings Using Regex"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Search Strings Using Regex using Scala."
type: technical_note
draft: false
---
## Create A String


```scala
// Create a string value
val attack_order : String = "Our 382 troops will attack their east flank at dawn. They have 28 troops there."
```

## Create A Regex Pattern


```scala
// Create a value that is a regex pattern
val find_numbers = "[0-9]+".r
```

## Find First Match


```scala
// Apply the regex to find the first match, output the result, otherwise output "None"
find_numbers.findFirstIn(attack_order).getOrElse("None")
```




    382



## Find All Matches


```scala
// Apply the regex to find all matches and output to an array
find_numbers.findAllIn(attack_order).toArray
```




    Array(382, 28)


