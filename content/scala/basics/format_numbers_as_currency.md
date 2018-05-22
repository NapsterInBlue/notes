---
title: "Format Numbers As Currency"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Format numbers as currency using Scala."
type: technical_note
draft: false
---
## Load The NumberFormat Currency Package


```scala
// Create a value with the numberformat currency package
val format_as_dollars = java.text.NumberFormat.getCurrencyInstance
```

## Format A Number As Dollars


```scala
format_as_dollars.format(123.456789)
```




    $123.46



## Change To A Local Currency

Java's locale uses [ISO 3166-1 country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).


```scala
// Load the java libraries
import java.util.{Currency, Locale}

// Create a value with the numberformat currency package
val format_as_afghan = java.text.NumberFormat.getCurrencyInstance

// Set the locale of Currency to Afganistan
val af = Currency.getInstance(new Locale("af", "AF"))

// Set the locale of the numberformat currency package to the Afghan
format_as_afghan.setCurrency(af)
```

## Format A Number As Afghans


```scala
// Format the currency as Afghans
format_as_afghan.format(123456.789)
```




    AFN123,456.79


