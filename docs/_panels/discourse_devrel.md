---
title: Discourse Devrel
description: DevRel related metrics for Discourse.
author: Bitergia
screenshot: sigils/discourse_devrel.png
created_at: 2020-06-02
grimoirelab_version: 0.2.40
layout: panel
---

This dashboard focuses on Discourse activity and active authors in different time slots.


* To filter bots there is a filter on top of the dashboard.
* Links to Hatstall are provided within the tables to allow to editing profiles in case there are unmerged profiles or bots that are not marked as such.
* There are 3 tables, one per each time interval.

The metrics you'll find are:
* **Posts Created**: Number of new posts by month 30/60/90 day rolling avg posts/day. This calculates 
the numbers per day, as rolling averages are per day too. Metric says posts: a post is either
a question or an answer (this can be easily modified to count only one of them or to count 
them separately).
* **Posts**: Top 30 contributors in the last 30/60/90 days (excluding any automated tooling, 
see bots filter on top).




