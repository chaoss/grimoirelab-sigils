---
title: Overview
description: summary of basic metrics on all analyzed sources.
author: Bitergia
screenshot: sigils/overview.png
created_at: 
grimoirelab_version: 0.2.0
layout: panel
---

The Overview panel shows a summary of the repositories analyzed.
Most of the visualizations found in it can be explored in more detail in
the panels corresponding to the different analysis: Git, GitHub Issues,
GitHub Issues Timing, GitHub Pull Requests, GitHub Pull Requests Timing and
others.


### Files
This is a special dashboard that contains visualizations for all the different data sources available
in GrimoireLab. **[Grimoirelab-sirmordred][sirmordred] uploads it by default and removes all the
visualizations corresponding to the data sources that aren't active**.

**In case you want to upload it manually**, you'll need to remove those visualizations afterwards.
 
Just Import the following JSON file using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/)
and make sure the index patterns for the data sources you are interested in are in place on Kibana.

| [![Dashboard][dash-icon]][dashboard] |
| :-------------: |
| **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import overview.json
```

[sirmordred]: https://github.com/chaoss/grimoirelab-sirmordred#sirmordred-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/overview.json
