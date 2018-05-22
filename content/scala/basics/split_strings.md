---
title: "Split Strings"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Split Strings Using Scala."
type: technical_note
draft: false
---
## Split Up A String By Spaces


```scala
// Create a value called text that is a string
val text: String = "This is a sentence that we want to split along every space"

// Split up the value along every space
text.split(" ")
```




    Array(This, is, a, sentence, that, we, want, to, split, along, every, space)



## Split Up A String By Commas


```scala
// Create a value called csv_row that is a string and contains one row of data
val csv_row: String = "Billy, Miller, 22, Baker, High School"

// Split up that row by commas
csv_row.split(",")
```




    Array(Billy, " Miller", " 22", " Baker", " High School")


