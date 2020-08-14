---
title: GitHub Pull Requests Timing
description: metrics focused on how long pull requests remain open.
author: Bitergia
screenshot: sigils/github-pullrequests-timing.png
created_at: 
grimoirelab_version: 0.2.0
layout: panel
---

These panels contain information about evolution of Pull Requests in time.
Although it shows submitters, repositories and domains as previous GitHub panels,
here we focus on how long Pull Requests remain open.  Thus, we can work with
this panel in a similar way for filtering, but dealing with different information.

Among other information we can find statistical information on closing times and
also tables with the latest and the oldest Pull Requests.

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`github_issues` index][github_issues-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-github_pullrequests] for details on how to deploy it).
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
kidash -e https://user:pass@localhost:443/data --import github_pull_requests_timing.json
```

[github_issues-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/github_issues.csv
[sirmordred-github_pullrequests]: https://github.com/chaoss/grimoirelab-sirmordred#pull-request
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github_pull_requests_timing.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github_issues-index-pattern.json
