---
title: "Matching Conditions"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Matching conditions using Scala."
type: technical_note
draft: false
---
## Create A String


```scala
// Create some strings
val text1 = "Man"
val text2 = "F"
val text3 = "Dog"
```

## Create A Function That Uses A Match Expression


```scala
// Define a function that takes in a string, and matches it
def findGender(word: String) = word match {
    // If any of these words, return "Woman"
    case "Female" | "F" | "Woman" | "Lady" | "Girl" => "Woman"
    // If any of these words, return "Man"
    case "Male" | "M" | "Man" | "Gentleman" | "Boy" => "Man"
    // If anything else, return "Unknown"
    case _ => "Unknown"
}
```

## Apply The Function To The Strings


```scala
findGender(text1)
```




    Man




```scala
findGender(text2)
```




    Woman




```scala
findGender(text3)
```




    Unknown


