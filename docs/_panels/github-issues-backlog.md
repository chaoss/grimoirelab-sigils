---
title: GitHub Issues Backlog
description: focused on pending (open) tasks.
author: Bitergia
screenshot: sigils/github-issues-backlog.png
created_at: 
grimoirelab_version: 0.2.0
layout: panel
---

This panel focuses on pending tasks, that is, those Issues
that remain open. Of course this depends on when we retrieved the
data. [Grimoirelab-sirmordred documentation][sirmordred-github_issues]
provides information on how to configure data retrieval.

It is possible to filter data in the same way as in other GitHub panels
(by submitter, repository and domain).

A list with the oldest Issues is also shown, providing direct
links to them and some basic information as their titles, how long they have
been open, and when they were created.


### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`github_issues` index][github_issues-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-github_issues] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import github_issues-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import github_issues_backlog.json
```

[github_issues-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/github_issues.csv
[sirmordred-github_issues]: https://github.com/chaoss/grimoirelab-sirmordred#issue
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github_issues_backlog.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github_issues-index-pattern.json
