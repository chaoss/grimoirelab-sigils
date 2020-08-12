---
title: CoLic
description: metrics focused on license analysis
author: Nishchith Shetty
screenshot: sigils/colic.gif
created_at: 
grimoirelab_version: 0.2.0
layout: panel
---

The CoLic panel is focused on analyzing the License & Copyright related
information obtained from Graal. [Graal](https://github.com/chaoss/grimoirelab-graal)
is a tool which uses a wide range of Backends for specific tasks, one of them
being **`Code License(CoLic)`** which provides License & Copyright related
information from a given software repository.

## Metrics
From left to right and top to bottom, some of the metrics provided are:

* **Repositories Overview**: Overview of all the repositories with the number of
  licensed and copyrighted files.
* **Evolution: Licensed & Copyrighted Files**: Evolution of Total Files vs Licensed and
  Copyrighted files.
* **License & Copyright Definition**: A Pie-Chart showing the top Copyright and License
  definitions in the project.
* **All Files: License & Copyright Definition**: Shows license & copyright definition
  for every file in a project. It can be delegated for a module with the help of the
  Selector.

Additionally, the visualizations can be delegated with the help of Selector at the Top(left);
which provides filters such as **`Module Path`**, **`Interval`**, **`Repository`** and many more
for specific purposes.

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* See [grimoirelab-sirmordred documentation][sirmordred-colic] for details on how to deploy it.
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] [![Index Pattern][ip-icon]][index-pattern-2] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the 
following commands:
```
kidash -e https://user:pass@localhost:443/data --import colic-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import colic_study-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import colic.json
```

[colic-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/colic.csv
[sirmordred-colic]: https://github.com/chaoss/grimoirelab-sirmordred#colic-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/colic.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/colic-index-pattern.json
[index-pattern-2]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/colic_study-index-pattern.json
