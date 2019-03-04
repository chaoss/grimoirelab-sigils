---
title: Community Structure by Organization
description: view of a community grouping contributors by their activity, split by organizations.
author: Bitergia
screenshot: sigils/community-structure-by-organization.png
created_at: 2019-02-15
grimoirelab_version: 0.2.0
layout: panel
---

In order to analyze community structure we rely on 
[Onion model]({{ site.baseurl }}/common/onion_analysis). All panels
related to community structure are based on [the onion study included in
grimoirelab-elk project.](https://github.com/chaoss/grimoirelab-elk/blob/master/doc/studies.md#onion-study)


## Metrics

This panel splits data into organizations. **Onion model is computed individually
for each organization**.

* **Contributions by Organization**: this donut chart placed on the top of
the panel splits number of contributions by organization. 
* **Community Structure**: on the top right corner we find the evolution of
the different onion roles through time, divided by quarters. 
* **Contributions**: just below, another bar chart shows the
evolution of contributions in order to compare both to better
understand how groups evolve.
* **Authors**: on the left hand side, a table of authors shows the total
number of contributions of each one in the selected time frame together
with the number of quarters that author has been active in the community.
* **Organizations**: below bar charts, there is another table showing number of
people and contributions by organization and role for the selected time frame.

In addition to Kibana filters and search box on top, filtering by `Data
Source` is allowed by using the top left corner widget. Notice the blue filter
on top used for showing only `Git` data. This filter can be modified by using
`Data Source` widget mentioned above.

## Use Notes

##### 1. Only one data source filter should be active at the same time

In Kibana/Kibiter, filters are combined by means of `AND` operators.
E.g. if we enable Git and GitHub filters, under the hood we get
an ElasticSearch query like:
```
data_source=git AND data_source=github
```
Thus, by selecting more than one data source filter at the same time,
we won't get any result, because data come from one data source or another,
but not several at the same time.

**`Data Source` widget automatically manages this for you**, so you just need
to select the desired data source in the drop down list and click on
`Apply changes`. **Data is meaningful only if one and only one data source** 
is selected for filtering.

##### 2. Select one and only one organization to view meaningful data

**In order to have meaningful data, we need to select the organization we
are interested in from the donut chart** on top or from
organizations table below bar charts. Then, a new filter will appear on top, next
to the blue one named `data_source:"git"`, and we'll get the data we need in
the panel.

**LIMITATION: when no organization is selected for filtering** bar chart
on the top right corner will show group sizes
&mdash;core, regular, casual&mdash; aggregated for all organizations. 
That is, if we have _organization A_ with 5 people in core group for 2018Q1
and _organization B_ with 2 people in core group for 2018Q1, bar chart will
show 7 as value for core group, which **is not** the result of computing
onion for both organizations together but the sum of their specific results.
This is due to the use of pre-computed values by organizations. In order
to get data for all organizations together, see 
[Overall Community Structure panel]({{ site.baseurl }}/panels/overall-community-structure).
