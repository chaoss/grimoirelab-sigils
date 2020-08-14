---
title: GitLab Merge Requests Efficiency
description: efficiency solving (merging or closing) MRs on GitLab.
author: Miguel-Ángel Fernández
screenshot: sigils/gitlab-mergerequests-efficiency.png
created_at: 2018-12-12
grimoirelab_version: 0.2.1
layout: panel
---

This panel offers a view of efficiency solving (merging or closing) merge requests based on three metrics:
* **REI**: Review Efficiency Index, defined as the number of solved (merged or closed) merge requests divided
  by the number of open ones in a given period of time. Measures efficiency solving merge requests.
* **Lead Time**:  the time expressed in days between the initiation and completion of a production
  process, in this case, a merge request. Shown in average in this panel.
* **Time to Merge**: time from merge request creation to the moment in which it's solved.


Filtering by Organization and Project is allowed by using the top left corner
widget.

**REI** is shown next to filtering widget. Moving average is set to 8 weeks
to identify changes in trends. Average is also shown as reference. REI values
greater than 1 means the community is solving more merge requests than those they are
opening. Values smaller than 1 means the opposite, i.e., more merge requests open than
those solved during a given time frame.

**Median Time to Merge** gauge is set to show green color for less than 7 days, yellow
for values from 7 to 30 days and red from 30 to 90 days. This means we are
considering a week as a good time to solve. This is just a visual reference and
you can always rely on the number, ignoring this color scheme.

Next to this gauge, **Lead Time** shows the average Time to Merge expressed in days together to its
trend. This helps to identify peaks and visualize the global evolution of time
spent in solving merge requests.

Finally, a table on the right splits **Median Time to Solve** by repository,
giving an insight on the differences among them.

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`gitlab_merge_requests` index][gitlab_merge_requests-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-gitlab_merge_requests] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import gitlab_merge_requests-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import gitlab_merge_requests_efficiency.json
```

[gitlab_merge_requests-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/gitlab_merges.csv
[sirmordred-gitlab_merge_requests]: https://github.com/chaoss/grimoirelab-sirmordred#gitlab-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/gitlab_merge_requests-index-pattern.json
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/gitlab_merge_requests_efficiency.json
