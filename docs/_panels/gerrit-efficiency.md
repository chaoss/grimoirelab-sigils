---
title: Gerrit Efficiency
description: efficiency closing changesets in Gerrit.
author: Bitergia
screenshot: sigils/gerrit-efficiency.png
created_at: 
grimoirelab_version: 0.2.1
layout: panel
---

This panel offers a view of efficiency closing changesets based on two metrics:
* **REI**: Review Efficiency Index, defined as the number of closed changesets divided
  by the number of open ones in a given period of time. Measures efficiency closing changesets.
* **Lead Time**: the time expressed in days between the initiation and completion of a production
  process, in this case, a changesets. Shown in average in this panel.
* **Time to Merge**: time from changeset creation to the moment in which it's merged or abandoned.

Filtering by Organization and Project is allowed by using the top left corner
widget.

**REI** is shown next to filtering widget. Moving average is set to 8 weeks
to identify changes in trends. Average is also shown as reference. REI values
greater than 1 means the community is closing more changesets than those they are
opening. Values smaller than 1 means the opposite, i.e., more changesets open than
those closed during a given time frame.

**Median Time to Merge** gauge is set to show green color for less than 7 days, yellow
for values from 7 to 30 days and red from 30 to 90 days. This means we are
considering a week as a good time to merge. This is just a visual reference and
you can always rely on the number, ignoring this color scheme.

Next to this gauge, **Lead Time** shows the average Time to Merge expressed in days together to its
trend. This helps to identify peaks and visualize the global evolution of time
spent in closing changesets.

Finally, a table on the right splits **Median Time to Merge** by repository,
giving an insight on the differences among them.

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
kidash -e https://user:pass@localhost:443/data --import gerrit_efficiency.json
```

[gerrit-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/gerrit.csv
[sirmordred-gerrit]: https://github.com/chaoss/grimoirelab-sirmordred#gerrit-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/gerrit_efficiency.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/gerrit-index-pattern.json
