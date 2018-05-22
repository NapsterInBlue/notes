---
title: "Bessels Correction"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "A short explanation of Bessel's Correction."
type: technical_note
draft: false
---
Bessel's correction is the reason we use $n-1$ instead of $n$ in the calculations of sample variance and sample standard deviation.

Sample variance:

$$ s^2 = \frac {1}{n-1} \sum\_{i=1}^n  \left(x\_i - \overline{x} \right)^ 2 $$

When we calculate sample variance, we are attempting to estimate the population variance, an unknown value. To make this estimate, we estimate this unknown population variance from the mean of the squared deviations of samples from the overall sample mean. A negative sideffect of this estimation technique is that, because we are taking a sample, we are a more likely to observe observations with a smaller deviation because they are more common (e.g. they are the center of the distribution). The means that by definiton we will underestimate the population variance.

Friedrich Bessel figured out that by multiplying a biased (uncorrected) sample variance $s\_n^2 = \frac {1}{n} \sum\_{i=1}^n  \left(x\_i - \overline{x} \right)^ 2$ by $\frac{n}{n-1}$ we will be able to reduce that bias and thus be able to make an accurate estimate of the population variance and standard deviation. The end result of that multiplication is the unbiased sample variance.
