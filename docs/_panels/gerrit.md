---
title: Gerrit
description: metrics focused on Gerrit changesets.
author: Bitergia
screenshot: sigils/gerrit.png
created_at: 
grimoirelab_version: 0.2.37
layout: panel
---

This dashboard focuses on metrics derived from Gerrit changesets, thus it shows insights about the changesets in terms of their status, patchsets and submitters. It also provides information split by repository and organization in order to ease comparisons. Two filters are set on top of the dashboard, `Changesets Only` and `NOT bots`, the former allows to visualize only changesets, while the latter removes any changeset created by bots.

* **Gerrit**: a set of metrics that show general numbers about the number of changesets, submitters, repositories and median time to first review.
* **Organizations**: a pie chart that highlights the number of changesets grouped by organizations.
* **Repositories**: a table that reports the number of changesets and submitters per repository, plus the average and median of the first review. 
* **Changesets by Status**: a bar chart that depicts the evolution of changesets per status (e.g., merged, abandoned and new).
* **Status**: a pie chart that summarizes the number of changesets grouped by status.
* **Changeset Submitters**: a bar chart that describes the evolution of changeset submitters.
* **Changesets Statistics (Open Time in Days)** a set of metrics that report statistics about the number of days changesets are left opened.
* **Patchset Statistics per Changeset** a set of metrics that summarize statistics about the number of patchsets included in changesets.
* **Organizations**: a bar chart that shows the evolution of the number of changesets per organizations.
* **Submitters**: a table that reports the number of changesets, projects and average number of patchsets per submitter.
* **Patchsets per Changeset**: a bar chart that shows the evolution of the number of patchsets included in changesets.

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`gerrit` index][gerrit-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-gerrit] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import gerrit-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import gerrit.json
```

[gerrit-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/gerrit.csv
[sirmordred-gerrit]: https://github.com/chaoss/grimoirelab-sirmordred#gerrit-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/gerrit.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/gerrit-index-pattern.json
