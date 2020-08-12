---
title: CoCom
description: metrics focused on source code analysis
author: Nishchith Shetty
screenshot: sigils/cocom.gif
created_at: 
grimoirelab_version: 0.2.0
layout: panel
---

The CoCom panel is focused on analyzing source code information obtained
from Graal. [Graal](https://github.com/chaoss/grimoirelab-graal) is a tool
which uses a wide range of Backends for specific tasks, one of them
being **`Code Complexity(CoCom)`** which provides source code related
information such as Code Complexity, Lines of Code, Functions and many
more from a given software repository.

## Metrics
From left to right and top to bottom, some of the metrics provided are:

* **Repositories Overview**: Overview of all the repositories and overall metrics 
  per project.
* **Evolution: Code Complexity & Functions**: Evolution of Code Complexity and 
  Functions over a given period of time.
* **Evolution: LOC & Comments**: Evolution of Lines of Code and Comment Lines
  over a given period of time.
* **All Files: Code complexity, LOC and ratios**: Shows metrics such as Code
  Complexity, LOC, Functions, and others for every file in a project. It can be
  delegated for a module with the help of the Selector.

Additionally, the visualizations can be delegated with the help of Selector at the Top(left);
which provides filters such as **`Module Path`**, **`Interval`**, **`Repository`** and many more
for specific purposes.

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* See [grimoirelab-sirmordred documentation][sirmordred-cocom] for details on how to deploy it.
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] [![Index Pattern][ip-icon]][index-pattern-2] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the 
following commands:
```
kidash -e https://user:pass@localhost:443/data --import cocom-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import cocom_study-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import cocom.json
```

[sirmordred-cocom]: https://github.com/chaoss/grimoirelab-sirmordred#cocom-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/cocom.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/cocom-index-pattern.json
[index-pattern-2]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/cocom_study-index-pattern.json
