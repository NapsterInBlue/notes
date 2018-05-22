---
title: "Extract Substrings Using Regex"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Extract substrings using regex using Scala."
type: technical_note
draft: false
---
## Create String


```scala
// Create a string value
val text: String = "27 aircraft"
```

## Create Regex Pattern


```scala
// Create a regex with two pattern matches (one number and one word)
val pattern = "([0-9]+) ([A-Za-z]+)".r
```

## Extract Substrings That Match Regex


```scala
// Apply the regex pattern such that each of the two pattern matches is assigned to a seperate value
val pattern(vehicle_number, vehicle_type) = text
```

## View Output


```scala
// View the value
vehicle_number
```




    27




```scala
// View the value
vehicle_type
```




    aircraft


