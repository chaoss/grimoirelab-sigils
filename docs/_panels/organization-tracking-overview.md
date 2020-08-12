---
title: Organization Tracking Overview
description: track organization activity to code compared to the rest of the data sources.
author: Bitergia
screenshot: sigils/organization-tracking-overview.png
created_at: 
grimoirelab_version: 0.2.38
layout: panel
---

This dashboard focuses on tracking organizations activity through all the available data sources. Different
from the [Overview dashboard]({{ site.baseurl }}/panels/overview), the activity is split between code
contributions and the rest of the contributions.

## Metrics

* **Organization drop down list** on top allows to easily filter data by a set of organizations.
* **Contributions big numbers** right below offers a quick idea of the volume of activity. 
* **Evolution charts** provide a more specific view of the activity and when it happened so we can look
    for peaks or valleys.
* **Author tables** allow to sorting them by number of contributions and accessing their Hatstall profiles
    in order to edit their associated data and fix their affiliations if needed.
* **Projects tables** split numbers by project.
* **Contributions and Contributors pie charts** offers a more visual approach to compare organizations
    weight on the selected projects (if any);

### Building the Dashboard: details about Indexes and Fields

This dashboard is built on top of:
 * The [Git] index.
 * An alias called `all_enriched` that combines all available physical indexes corresponding to the
   different data sources. This allows us to easily build the visualizations shown in the dashboard.
   Git data is filtered out from the visualizations as it shown on its own visualizations. Jenkins
   data is also filtered out because does not contain any contribution or contributor information.
   `all_enriched` allow us to use any field present on any of the indexes it combines.

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check `all_enriched` index is available on your GrimoireLab instance
([grimoirelab-sirmordred][sirmordred-general] automatically creates this alias for you).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import all_enriched-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import organization_tracking_overview.json
```

[sirmordred-general]: https://github.com/chaoss/grimoirelab-sirmordred#general
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/organization_tracking_overview.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/all_enriched-index-pattern.json

[Git]: https://github.com/chaoss/grimoirelab-elk/tree/master/schema/git.csv
