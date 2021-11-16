---
title: 'Affiliations'
description: dashboard focused on manage people affiliations.
screenshot: sigils/affiliations.png
author: Alberto Pérez García-Plaza
created_at: 2020-17-01
grimoirelab_version: 0.2.2
layout: panel
---

This dashboard offers a view across all data sources. Its main goal is helping to analyze and
update those contributors that remain unaffiliated (affiliated to `Unknown`).  

From left to right and top to bottom, the widgets provided are:

* **Data Source**: data source selector.
* **Summary**: global numbers to complement the pie chart.
* **Data Sources**: tag cloud showing the amount of contributions coming from each data source. It 
    allows filtering in data sources by clicking on them. For selecting several at the same time, 
    please use `Data Source` widget instead (or add a filter manually on top).
* **Authors by Organization and Domains**: pie chart showing how many authors are affiliated to each organization
    and domains.
    Our main goal here will be keeping the `Unknown` slice as small as possible.
* **Contributions by Organization and Domains**: pie chart showing how many contributions are affiliated to each
    organization and domains.
    Our main goal here will be keeping the `Unknown` slice as small as possible.
* **Authors**: table to search from the most active contributors. By correctly affiliating the most
    active ones we will quickly improve the results of the pie chart and, by extension, of our analysis in
    all other dashboards. The column titled `Profile` provides direct links to the corresponding
    page on **Hatstall** web app, where affiliations may be queried and modified.
* **Organizations**: table providing information at the level of organization. Offers more detail than
    the pie chart.
     

In addition you'll see some filters on top. The obvious one is filtering bots out. The other two are there
to exclude those profiles that can't be affiliated because there is no information available (name, username,
e-mail).

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`affiliations` index][affiliations-schema] is available on your GrimoireLab instance 
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
kidash -e https://user:pass@localhost:443/data --import affiliations-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import affiliations.json
```

[affiliations-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/affiliations.csv
[sirmordred-general]: https://github.com/chaoss/grimoirelab-sirmordred#general
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/affiliations.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/affiliations-index-pattern.json
