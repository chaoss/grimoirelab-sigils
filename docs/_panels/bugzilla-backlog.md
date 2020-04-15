---
title: Bugzilla Backlog
description: focused on pending (open) bugs.
author: Bitergia
screenshot: sigils/bugzilla-backlog.png
created_at: April 15th, 2020
grimoirelab_version: 0.2.39
layout: panel
---

This dashboard focuses on pending bugs, that is, those Issues
that remain open (note that here we work with data retrieved in the moment of
dashboard creation).

It is possible to filter data in the same way as in other Bugzilla panels
(by submitter, project, and status).

A list with the oldest Issues is also shown, providing direct
links to them and some basic information as their titles, how long they have
been open and when they were created.

## Metrics

The metrics provided are:

* **Open Issues Statistics**: total numbers of open issues, accumulated open days, and the average time
the issues have been open (days).
* **Issues waiting to be closed**: a bar chart that shows the evolution of the status of the open issues over time.
* **Backlog**: a table separated by the title of the issues that details the bug URL, number of comments,
number of updates, open date, and the number of the day that the issue has been open.
* **Accumulated Time (days): Issues waiting to be closed**: a bar chart that shows the evolution of the accumulated
open issues (days).
* **Assignee Organizations**: a pie chart that summarizes the issues by the assignees' organization.
* **Backlog Submitters**: a table sorted by submitters that details the number of issues, average time the issues
have been open (days), and projects.
* **Projects**: a table sorted by projects that details the number of open issues and the average time the issues
have been open (days).
* **Organizations**: a table sorted by organizations that details the number of open issues and the average time
the issues have been open (days).
