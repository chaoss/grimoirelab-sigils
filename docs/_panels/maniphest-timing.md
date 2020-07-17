---
title: Maniphest Timing
description: metrics focused on how long tickets/bugs remain open..
author: Bitergia
screenshot: sigils/maniphest-timing.png
created_at: July 17th, 2020
grimoirelab_version: 0.2.42
layout: panel
---

This dashboard contains information about the evolution of tickets/bugs over time. It
shows submitters, project and status of the tickets/bugs, and gives also insights about
the time to process them.

Among other information we can find statistical information on closing times and
also tables with the latest and the oldest Issues.

## Metrics

The metrics provided are:

* **Maniphest Summary**: total numbers of tickets/bugs, submitters, assignees, median of the time the tickets/bugs stay open (days),
and average of the time the tickets/bugs stay open (days).
* **Median Open Time (Days)**: a bar chart that shows the evolution of the median of the time the tickets/bugs stay open (days).
* **80 Percent Open Time (Days)**: a bar chart that shows the evolution of the 80 percentile of the time the tickets/bugs stay open (days).
* **Status**: a pie chart that summarizes the proportion of the tickets/bugs by status.
* **Submitters**: a bar chart that shows the evolution of the number of submitters over time.
* **Organizations**: a table sorted by organizations that details the number of tickets/bugs open, submitters, assignees,
and the average time the tickets/bugs have been open (days).
* **Submitters**: a table sorted by submitters that details the number of tickets/bugs, assignees,
and the average time the tickets/bugs have been open (days).
* **Projects**: a table sorted by projects that details the number of tickets/bugs, submitters, asignees,
the average time the issue has been open (days), and the average the issue has been changed.
* **Latest Issues**: a table separated by the summary of the tickets/bugs that details the projects, submitter,
status, ticket/bug URL, and date of the creation.
* **Oldest Issues**: a table separated by the summary of the tickets/bugs that details the projects, submitter,
status, ticket/bug URL, date of the creation, and the time the ticket/bug stay open (days).
