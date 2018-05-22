---
title: "Replacing Parts Of Strings"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Replacing Parts Of Strings using Scala."
type: technical_note
draft: false
---
## Create A String


```scala
// Create a string value
val text: String = "Lt. Steve Miller will be leading the attack."
```

## Create A Regex Pattern


```scala
// Create a regex pattern for a name
val find_steve = "Steve Miller".r
```

## Replace Anything That Matches That Pattern With Something Else


```scala
// Replace all instances of the pattern with a different name
find_steve.replaceAllIn(text, "Peter Jackson")
```




    Lt. Peter Jackson will be leading the attack.



## Replace First Match


```scala
// Replace first instance of the pattern with a different name
find_steve.replaceFirstIn(text, "Peter Jackson")
```




    Lt. Peter Jackson will be leading the attack.


