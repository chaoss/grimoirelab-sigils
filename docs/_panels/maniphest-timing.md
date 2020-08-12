---
title: Maniphest Timing
description: metrics focused on how long tickets/bugs remain open..
author: Bitergia
screenshot: sigils/maniphest-timing.png
created_at: July 17th, 2020
grimoirelab_version: 0.2.42
layout: panel
---

This dashboard contains information about the evolution of tickets/bugs over time. It
shows submitters, project and status of the tickets/bugs, and gives also insights about
the time to process them.

Among other information we can find statistical information on closing times and
also tables with the latest and the oldest Issues.

## Metrics

The metrics provided are:

* **Maniphest Summary**: total numbers of tickets/bugs, submitters, assignees, median of the time the tickets/bugs stay open (days),
and average of the time the tickets/bugs stay open (days).
* **Median Open Time (Days)**: a bar chart that shows the evolution of the median of the time the tickets/bugs stay open (days).
* **80 Percent Open Time (Days)**: a bar chart that shows the evolution of the 80 percentile of the time the tickets/bugs stay open (days).
* **Status**: a pie chart that summarizes the proportion of the tickets/bugs by status.
* **Submitters**: a bar chart that shows the evolution of the number of submitters over time.
* **Organizations**: a table sorted by organizations that details the number of tickets/bugs open, submitters, assignees,
and the average time the tickets/bugs have been open (days).
* **Submitters**: a table sorted by submitters that details the number of tickets/bugs, assignees,
and the average time the tickets/bugs have been open (days).
* **Projects**: a table sorted by projects that details the number of tickets/bugs, submitters, asignees,
the average time the issue has been open (days), and the average the issue has been changed.
* **Latest Issues**: a table separated by the summary of the tickets/bugs that details the projects, submitter,
status, ticket/bug URL, and date of the creation.
* **Oldest Issues**: a table separated by the summary of the tickets/bugs that details the projects, submitter,
status, ticket/bug URL, date of the creation, and the time the ticket/bug stay open (days).

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`maniphest` index][maniphest-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-maniphest] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import maniphest-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import maniphest_timing.json
```

[maniphest-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/maniphest.csv
[sirmordred-maniphest]: https://github.com/chaoss/grimoirelab-sirmordred#phabricator-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/maniphest-index-pattern.json
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/maniphest_timing.json
