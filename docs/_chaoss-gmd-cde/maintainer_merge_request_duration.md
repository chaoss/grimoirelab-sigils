---
title: Maintainer Response to Merge Request Duration.
description: panel focused on the time to response after a pull request took place.
author: Daniel Izquierdo Cortázar
created_at: 2019-01-19
grimoirelab_version: 0.2.2
layout: panel
screenshot: chaoss-gmd-cde/maintainer_response_to_merge_request_duration.png
---

This panel provides information about the time to first response to a pull request.

The goal of this panel is to provide several data access layers (organizations, projects
and repositories) and play with the time to first response using the average and the median
as main metrics.

#### Widgets and metrics provided in the panel

* **Summary**: number of pull requests submitted and their time to first attention in
average and in median.
* **Average Time to First Response in Days over time**: evolution of the average time
to response a pull request. This chart aggregates the information by the date of creation
of the pull request. Thus, each of the columns displayed in the chart shows the average of the
first time to response of all of the pull requests opened in such timeslot.

* **Repository Data**: this widgets displays information about the time to response in average and in median per repository.
This provides the number of pull requests per respository as well.

Filtering by Organization and Project is allowed by using the top left corner
widget.

Finally, a short text is shown at the bottom to explain the basics needed to understand
the panel.

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
kidash -e https://user:pass@localhost:443/data --import maintainer_response_to_merge_request_duration.json
```

[github_issues-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/github_issues.csv
[sirmordred-github_issues]: https://github.com/chaoss/grimoirelab-sirmordred#github-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/chaoss-gmd-cde/github_issues-index-pattern.json
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/chaoss-gmd-cde/maintainer_response_to_merge_request_duration.json
