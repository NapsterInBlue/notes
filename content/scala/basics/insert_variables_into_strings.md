---
title: "Insert Variables Into Strings"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Insert variables into strings using Scala."
type: technical_note
draft: false
---
The proper term from this is _string interpolation_.

## Create A Value


```scala
// Create some values
val number_of_soldiers: Short = 542
val casualties: Short = 32
```

## Add The Value To A String


```scala
print(f"Before the battle we had $number_of_soldiers soldiers. However, now we have ${number_of_soldiers - casualties}.")
```

    Before the battle we had 542 soldiers. However, now we have 510.
