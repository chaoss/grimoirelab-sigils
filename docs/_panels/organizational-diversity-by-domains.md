---
title: 'Organizational Diversity by domains'
description: panel focused on organizational diversity for contributions and contributors specifying the domains information.
screenshot: sigils/organizational_diversity_by_domains.png
author: Daniel Izquierdo Cortázar
created_at: 2019-01-15
grimoirelab_version: 0.2.2
layout: panel
---

This panel aims at providing a view of the diversity in terms of domains in a project. A domain
is the domain used by the contributor in any data source.  The goal of this panel is to show
how many active domains there are in a specific timeframe of activity together with their 
evolution over time.  This information can be filtered by data source.


## Metrics
From left to right and top to bottom, the metrics provided are:

* **Active Domains**: total number of unique active organizations in any data source.
* **Active Domains over Time by Data Source**: evolutionary chart displaying the number of
  active domains for each data source.
* **Number of Contributions**:  each slice in the pie chart is a domain. The bigger the slice
  the more contributions were done by such domain. 
* **People Contributing**: each slice in the pie chart is a domain. The bigger the slice the
  more people contributing from such domain.
* **Data Sources by Domain, Contributions and Contributors**:  this tables displays all of the
  information available for this panel, but ordered in a table. This has four columns that are
  the data source, the domain, the number of contributions across all of the data sources and the
  number of contributors across those data sources.

In addition to Kibana filters and search box ont top, filtering by `Data Source`, `Domain`
and/or `Project` is allowed by using the top left corner widget.

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
kidash -e https://user:pass@localhost:443/data --import organizational_diversity_by_domains.json
```

[sirmordred-general]: https://github.com/chaoss/grimoirelab-sirmordred#general
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/organizational_diversity_by_domains.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/all_enriched-index-pattern.json
