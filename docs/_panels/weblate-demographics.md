---
title: Weblate Demographics
description: attraction and retention of contributors.
author: Bitergia
screenshot: sigils/weblate-demographics.png
created_at: 
grimoirelab_version: 0.2.48
layout: panel
---

This panel focuses on the attraction of contributors and those leaving the community.
There are two main bar charts where you can filter the information.

By clicking on the drop down list you can select any project and any of its components.

The first bar chart, on the top, displays the amount of contributors that made
their first contribution in that period of time.

The bar chart below groups contributors by their last detected contribution.
Thus, the first bar chart provides information about how the community is
attracting contributors while the second bar chart provides information about
the evolution of the people leaving the community.

This panel is intended to be used with the whole history of the community
activated and not with some pre-established timeframe of activity as in other
panels (for instance, 2 years). This is done in this way as the information is
pre-computed and displayed focused on the first and last contribution of each
person.

The table on the bottom, showing contributions per project,
is mere informative and shouldn't be used to filter information. It is
worth mentioning that when clicking on any of them and a filter is enabled,
the information displayed is not filtered as it is usually done in Kibana.
Let us imagine that the filter by a project X is enabled. This panel would
show the _attraction/retention/contributors leaving_ the community that **at
some point participated in such project**. However, **this does not display
the specific _attraction/retention/contributors leaving_ rate for that
project**.

As the information is pre-computed per contributor and not done on-demand by
Kibana, this forces to use this approach.

In addition to this, information about contributors that recently left the
community is based on not having any contribution during the last 3 months
(so sent their last contribution three months ago). The selection of three months
as the period to define a contributor as inactive is based on our own experience
measuring open source communities. Although each community may have their own
peculiarities that may vary the approach, we use to set a six-month period for
code-related contributions, which in general, has been a good indicator up to now.
However, we think Weblate contributions are more dynamic than code-related ones,
so that's why we opted for reducing this time period for considering someone
is inactive. 

## Known limitations & issues

*  In order to count things we would need a common field that uniquely identifies
each contribution. E.g. in Git we could use `hash`, but it is not present in other
sources. Currently I used a count of index items to keep the metric compatible
with all indices, but this way **we are not excluding duplicates**. We could use
`uuid`, but in data sources like StackOverflow it is not used in answers, so
the result would be even worse than counting items.

* **There is a known issue that may affect the readability of the panel**:
when a person has been detected as sending her first contribution in 1970.
This is a problem of the analyzed Git repository that contains that information,
but also in the cleaning process of the Grimoire infrastructure. This data-issue
provokes that the information for such contributor for her first contribution took
place in 1970, and this is clearly wrong. Those contributions should be ignored or
updated to a real timeframe of activity at some point. If you see this behaviour
in the dashboard, please report this as a bug.

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check `weblate` index is available on your GrimoireLab instance and contains the proper demography fields.
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import weblate-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import weblate_demographics.json
```

[elk-studies]: https://github.com/chaoss/grimoirelab-elk/blob/master/doc/studies.md#running-studies-from-mordred
[sirmordred-studies]: https://github.com/chaoss/grimoirelab-sirmordred#backend-nametag-tag-is-optional
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/weblate_demographics.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/weblate-index-pattern.json
