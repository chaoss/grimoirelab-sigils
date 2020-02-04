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
* **Authors by Organization*: pie chart showing how many authors are affiliated to each organization.
    Our main goal here will be keeping the `Unknown` slice as small as posible.
* **Summary**: global numbers to complement the pie chart.
* **Data Sources**: tag cloud showing the amount of contributions coming from each data source. It 
    allows filtering in data sources by clicking on them. For selecting several at the same time, 
    please use `Data Source` widget instead (or add a filter manually on top).
* **Authors**: table to search from the most active contributors. By correctly affiliating the most
    active ones we will quickly improve the results of the pie chart and, by extension, of our analysis in
    all other dashboards. The column titled `Profile` provides direct links to the corresponding
    page on **Hatstall** web app, where affiliations may be queried and modified.
* **Organizations**: table providing information at the level of organization. Offers more detail than
    the pie chart.
     

In addition you'll see some filters on top. The obvious one is filtering bots out. The other two are there
to exclude those profiles that can't be affiliated because there is no information available (name, username,
e-mail).
