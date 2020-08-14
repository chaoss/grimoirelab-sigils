---
title: GitHub Pull Requests Efficiency
description: efficiency closing Pull Requests.
author: Bitergia
screenshot: sigils/github-pullrequests-efficiency.png
created_at: 
grimoirelab_version: 0.2.1
layout: panel
---

This panel offers a view of efficiency closing pull requests based on two metrics:
* **REI**: Review Efficiency Index, defined as the number of closed pull requests divided
  by the number of open ones in a given period of time. Measures efficiency closing pull requests.
* **Lead Time**:  the time expressed in days between the initiation and completion of a production
  process, in this case, a pull request. Shown in average in this panel.
* **Time to Merge**: time from pull request creation to the moment in which it's closed.


Filtering by Organization and Project is allowed by using the top left corner
widget.

**REI** is shown next to filtering widget. Moving average is set to 8 weeks
to identify changes in trends. Average is also shown as reference. REI values
greater than 1 means the community is closing more pull requests than those they are
opening. Values smaller than 1 means the opposite, i.e., more pull requests open than
those closed during a given time frame.

**Median Time to Merge** gauge is set to show green color for less than 7 days, yellow
for values from 7 to 30 days and red from 30 to 90 days. This means we are
considering a week as a good time to merge. This is just a visual reference and
you can always rely on the number, ignoring this color scheme.

Next to this gauge, **Lead Time** shows the average Time to Merge expressed in days together to its
trend. This helps to identify peaks and visualize the global evolution of time
spent in closing pull requests.

Finally, a table on the right splits **Median Time to Merge** by repository,
giving an insight on the differences among them.

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
kidash -e https://user:pass@localhost:443/data --import github_pull_requests_efficiency.json
```

[github_issues-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/github_issues.csv
[sirmordred-github_pullrequests]: https://github.com/chaoss/grimoirelab-sirmordred#pull-request
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github_pull_requests_efficiency.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github_issues-index-pattern.json
