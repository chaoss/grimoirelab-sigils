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

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`bugzilla` index][bugzilla-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-bugzilla] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the 
following commands:
```
kidash -e https://user:pass@localhost:443/data --import bugzilla-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import bugzilla_backlog.json
```

[bugzilla-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/bugzilla.csv
[sirmordred-bugzilla]: https://github.com/chaoss/grimoirelab-sirmordred#bugzilla-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/bugzilla_backlog.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/bugzilla-index-pattern.json
