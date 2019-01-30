---
title: Pull request merge duration
description: This panel focuses on pull requests merge duration, defined by the time between code merge request and code commit.
author: Ana Jimenez Santamaria
created_at: 2019-01-23
grimoirelab_version: 0.2.3
layout: panel
screenshot: chaoss-gmd-cde/pull_request_merge_duration.png
---


This panel focuses on **Pull request merge duration**.


This panel focuses on pull request merge duration, defined by the time between a code merge request and code commit. In this case, we focus on Github pull requests. When we measure Github, we cannot identify if a pull request has been merged, only if is open or closed. That's the reason why we will base our panel on pull request closing time

The main idea behind this panel is to help us identify a project state (growth maturity or decline) by answering custom queries like:
* **What is the duration of time between code merge request and code commit?**
* **What organizations/authors are being more efficient when closing a pull request?**
* **Is my project taking too long when closing code merge requests?**


### What should I look for in the panel?

We can visualize time to close in that specific time frame. For instance, how good or bad we were closing pull request created last year, two years ago or last week.

Moreover, you can filter pull request merge duration by author or organization to compare different resuts and see how many pull requests have been merged over a period of time

### List of metrics provided on the panel
* **Gauge visualization**: median time to close pull requests over a period of time.
* **Organization list based on closed pull requests**: time to close pull requests filtered by organization name and number of authors involved on each organization.
* **Number of pull requests**: Amount of pull requests over a period of time.
* **Median time open days**: median time to close pull request during the selected time range.

Filtering by Organization and Project is allowed by using the top left corner widget.

Finally, a short text is shown at the bottom to explain the basics needed to understand the panel and its filters.
