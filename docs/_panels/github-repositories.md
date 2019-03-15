---
title: GitHub Repositories
description: metrics focused on repositories popularity.
author: Bitergia
screenshot: sigils/github-repositories.png
created_at: 
grimoirelab_version: 0.2.0
layout: panel
---

The GitHub Repositories panel shows information about the popularity
of a repository in GitHub. The popularity is based in a set of
indicators: the number of forks, times a repository has been stared
and the number of subscriptions.

## Metrics

From left to right and top to bottom, the metrics provided by each
visualization are:

* **GitHub Repositories**: summary with the number of analyzed repositories
and the average amount of forks, stars and subscribers per
repository.
* **Repositories**: table with the maximum number of forks, stars
and subscribers each repository has had. See [below](#use-notes)
for more details.

Below these, there are two visualizations for each indicator:
**Evolution over time** and **Growth deltas over time**. 

* **Evolution over time**: it shows the total or accumulated value
of each indicator for each period. For example, if the number of
forks was `100` in `January` and in `February` it increased by `50`,
the visualization will show `150` in `February`.

* **Growth deltas over time**: it shows the variation of the indicator
from one period to another. Taking the example from above, the
the visualization will show `50` forks for `February`.

Please check some [use notes](#use-notes) below.

## Use notes

* Due to limitations in how Kibana performs certain queries, **Repositories**
visualization only shows the maximum number of each indicator. It does not
show its current value. Future versions of GrimoireLab will include
a different type of items (events) where these values will be available. 
   
* Evolution visualizations are limited to the **top 10 repositories** for each
indicator because more than that, will make the visualization illegible.

* Evolution visualizations set periods of **1 month** for one value to another.
