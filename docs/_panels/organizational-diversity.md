---
title: 'Organizational Diversity'
description: panel focused on organizational diversity for contributions and contributors
screenshot: sigils/organizational_diversity.png
author: Daniel Izquierdo Cortázar
created_at: 2019-01-15
grimoirelab_version: 0.2.2
layout: panel
---

This panel aims at providing a view of the diversity in terms of organizations in a project. 
An organization can be defined as any entity, from business units within a large corporation, 
to the corporation itself. The goal of this panel is to show how many active organizations 
there are in a specific timeframe of activity together with their evolution over time. This
information can be filtered by data source.


## Metrics
From left to right and top to bottom, the metrics provided are:

* **Active Organizations**: total number of unique active organizations in any data source.
* **Active Organizations over Time by Data Source**: evolutionary chart displaying the number
  of active organizations for each data source.
* **Number of Contributions**:  each slice in the pie chart is an organization. The bigger the
  slice the more contributions were done by such organization. 
* **People Contributing**: each slice in the pie chart is an organization. The bigger the slice
  the more people contributing from such organization.
* **Data Sources by Organization, Contributions and Contributors**:  this tables displays all
  of the information available for this panel, but ordered in a table. This has four columns
  that are the data source, the organization, the number of contributions across all of the data 
  sources and the number of contributors across those data sources.

In addition to Kibana filters and search box ont top, filtering by `Data Source`, 
`Organization` and/or `Project` is allowed by using the top left corner widget.