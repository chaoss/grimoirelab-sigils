---
title: GitHub closed events
description: metrics focused on the GitHub closed events.
author: Bitergia
screenshot: sigils/github-closed-events.png
created_at: 2020-04-21
grimoirelab_version: 0.2.0
layout: panel
---

This dashboard shows information related to the connection between the issues closed by pull requests. Such connections
are derived from the close events returned by the GitHub API. The widgets in the dashboard are described below.

- **Summary** gives an idea of the number of issues fixed.
- **Projects** highlights statistics of the number of issues fixed on the different projects.
- **Selector** allows focusing on one or more repositories.
- **Issues fixed by Organizations** offers a view of the issues fixed by pull request submitters' organizations.
- **Issues fixed by Organizations, over time** shows the evolution of the issues fixed by pull request submitters' organizations.
- **Table** provides details about the issues, the pull requests and the people involved (reporter, merger and submitter).

### Building the Dashboard: details about Index and Fields

This dashboard is built on top of a search on [`github_events`][github_events-schema] index which includes the closing events by pull 
requests. The generation of such events is described below. 

When a pull request references a keyword (e.g., fixes, closes, resolves) and issue number, GitHub creates an 
association between the pull request and the issue. When the pull request is merged into the repository's default 
branch, the corresponding issue is automatically closed, and the corresponding event is generated.

By default, the closed event includes the author that triggered the action (e.g., the user that merged a pull request).
During the enrichment process, the issue reporter and pull request submitter are also added to the enriched 
items (attributes `reporter_*` and `submitter_*`).   

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`github_events` index][github_events-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-github_events] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import github_events-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import github_events_closed.json
```

[github_events-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/github_events.csv
[sirmordred-github_events]: https://github.com/chaoss/grimoirelab-sirmordred#githubql-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github_events_closed.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github_events-index-pattern.json
