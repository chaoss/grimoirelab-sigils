---
title: Maniphest
description: activity and metrics focused on Tasks.
author: Bitergia
screenshot: sigils/maniphest.png
created_at: July 10th, 2020
grimoirelab_version: 0.2.42
layout: panel
---

This dashboard contains information about submitters, projects, and status of the issues.

These panels show activity by projects and status of the issues. Each issue
has a creation date and statuses. We measure activity based on the amount of tasks
created over time and their statuses.

This way, we can filter to get activity information related to a given submitter,
projects or/and status of the issues.

## Metrics

The metrics provided are:

* **Issues**: total numbers of issues, submitters, assignees.
* **Issues by Status, over time**: a bar chart that shows the evolution of the issue status over time.
* **Assigned Organizations**: a pie chart that summarizes the issues by the assignees' organization.
* **Projects**: a table sorted by projects that details the number of issues, submitters, assignees, the average time
the issues have been open (days), and the average changes.
* **Submitters, over time**: a bar chart that shows the evolution of the number of submitters over time.
* **Submitters**: a table sorted by submitters that details the number of issues, projects, assignees, and the average
time the issues have been open (days).
* **Issues by Organization, over time**: a bar chart that summarizes the issues by the submitters' organization over time.
* **Assigned Organizations**: a table sorted by organizations that details the number of issues, assignees,
and the average time the issues have been open (days).
