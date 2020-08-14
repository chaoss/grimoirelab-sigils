---
title: Jira Timing
description: metrics focused on how long issues remain open..
author: Bitergia
screenshot: sigils/jira-timing.png
created_at: August 5th, 2020
grimoirelab_version: 0.2.45.1
layout: panel
---

This dashboard contains information about the evolution of tickets over time. It
shows submitters, repositories and status of the tickets, and gives also insights about
the time to process them.

Among other information we can find statistical information on closing times and
also tables with the latest and the oldest Issues.

## Metrics

The metrics provided are:

* **Jira Summary**: total numbers of issues, submitters, assignees, median of the time the issue stay open (days),
and average of the time the issue stay open (days).
* **Issues Open in Median (Days)**: a bar chart that shows the evolution of the median of the time the issues stay
open (days).
* **Issues Open (best 80 Percent of them) (Days)**: a bar chart that shows the evolution of the 80 percentile of
the time the issues stay open (days).
* **Status**: a pie chart that summarizes the proportion of the issues by status.
* **Assigned Organizations**: a pie chart that summarizes the issues by the submitters' organization.
* **Issues**: a bar chart that shows the evolution of the number of issues over time.
* **Submitters**: a bar chart that shows the evolution of the number of submitters over time.
* **Organizations**: a table sorted by organizations that details the number of issues open, submitters, assignees,
median of the time the issue stay open (days), and the average time the issues have been open (days).
* **Submitters**: a table sorted by submitters that details the number of issues, repositories, assignees,
and the average time the issues have been open (days).
* **Projects**: a table sorted by projects that details the number of issues, submitters, assignees,
median of the time the issue stay open (days), and median the issue has been changed.
* **Closed Issues by Repository**: a table sorted by the number of issues that details the project key, project name,
number of issues, average time the issues have been open (days), first issue closed, and last issue closed.
* **Issues**: a table sorted by open date of issues that details the summary, submitter,
status, project, issue URL, open date, and the time the issue stay open (days).

## Known Limitations

To be able to properly calculate the time a given ticket has been in `open` state we need to relay on a painless
scripted field called `painless_delay`. The idea behind the field is:

* If the ticket is still open, `painless_delay` will be the time from its creation to now.
* If it is already closed, `painless_delay` will be the time from its creation to the moment it was closed
(`resolution_date`).

Unfortunately, we found corner cases in which Jira doesn't provide all the information we need. The actual cases
covered by `painless_delay` scripted field are:

* `diff(grimoire_creation_date, resolution_date)`: If the issue is already closed, `resolution_date` exists,
and `status` is `Close` or `Done`.
* `time_to_close_days` (pre-computed field storing the time closed issues were open): If the issue is closed,
`resolution_date` doesn't exist or status is not `Close` or `Done`.
* `diff(grimoire_creation_date, now)`: If the issue is still open.


### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`jira` index][jira-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-jira] for details on how to deploy it).
* Check `jira_resolution_date-index-pattern` index is available on your GrimoireLab instance
([grimoirelab-sirmordred][sirmordred-general] automatically creates this alias for you).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern-1][![Index Pattern][ip-icon]][index-pattern-2] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Patterns** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import jira-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import jira_resolution_date-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import jira_timing.json
```

[jira-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/jira.csv
[sirmordred-jira]: https://github.com/chaoss/grimoirelab-sirmordred#jira-
[sirmordred-general]: https://github.com/chaoss/grimoirelab-sirmordred#general
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[index-pattern-1]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/jira-index-pattern.json
[index-pattern-2]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/jira_resolution_date-index-pattern.json
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/jira_timing.json
