---
title: Lifecycle
description: Level of activity in git repositories
author: Manrique Lopez
screenshot: sigils/lifecycle.png
created_at: 2018-12-12
grimoirelab_version: 0.2.0
layout: panel
---

This panel provides a quick view of the lifecycle of the top 25 git repositories by activity and authors for a given period of time.

## Definition

**Active**: at least 1 commit per month

## Charts

* Evolution of the number of active repositories during selected period of time, and its trend
* Top 25 git repositories by number of commits for selected period of time, showing level of activity by month
* Top 25 git repositories by number of *active* authors for selected period of time, showing level of active authors by month

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`git` index][git-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-git] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import git-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import lifecycle.json
```

[git-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/git.csv
[sirmordred-git]: https://github.com/chaoss/grimoirelab-sirmordred#git-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/git-index-pattern.json
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/lifecycle.json
