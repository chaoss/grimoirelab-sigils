---
title: GitHub Issues
description: activity and community metrics focused on Issues.
author: Bitergia
screenshot: sigils/github-issues.png
created_at: 
grimoirelab_version: 0.2.0
layout: panel
---

GitHub Issues panels show information related to how community evolves in terms
of submitters, domains and activity.

These panels show activity by domains and repositories. Each issue has a creation
date and closing date, and of course a state (open or closed). We measure
activity based on the amount of tickets created over time and their states.

This way, we can filter to get activity information related to a given submitter,
domain or/and repository.


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
kidash -e https://user:pass@localhost:443/data --import github_issues.json
```

[github_issues-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/github_issues.csv
[sirmordred-github_issues]: https://github.com/chaoss/grimoirelab-sirmordred#issue
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github_issues.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github_issues-index-pattern.json
