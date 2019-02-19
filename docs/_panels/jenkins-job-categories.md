---
title: Jenkins Job Categories
description: results of Jenkins job executions by category.
author: Bitergia
screenshot: sigils/jenkins-job-categories.png
created_at: 2019-02-19
grimoirelab_version: 0.2.0
layout: panel
---

This panel is focused on offer a view of Jenkins data classified by job
categories. The idea behind the panel is helping to identify those
categories that are using more CI resources.

#### Filtering by Job Category

As Jenkins do not provide any particular field for category name, this panel
uses `installer` field. **This may not correspond to actual categories**. 

However, filtering by job name allows us to visualize data corresponding to
a given category. **In order to filter by category**, please use the search
box on top and the following query:
```
job_name:*<search_string>*
```
Where `<search_string>` should be what you are looking for, e.g. 
`distribution-test`. Wildcards(`*`) allow to filter those job names that
contains the category name we are looking for.

## Metrics

From left to right and top to bottom, the metrics provided are:

* **Big Numbers**: total numbers about what we are 
  visualizing in the panel. 
* **Jobs Evolution**: number of jobs through time.
* **Results per Category**: heat map to visually identify categories with 
  more runs and their results.
* **Categories**: aggregated numbers by category (actually by `installer` as
  exlained [above](#filtering-by-job-category)).
* **Jobs**: ggregated numbers by job name.

