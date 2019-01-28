---
title: Community Structure
description: find who are your core, regular and casual contributors.
author: Bitergia
screenshot: sigils/community-structure.png
created_at: 
grimoirelab_version: 0.2.0
layout: panel
---

## Introduction
In order to analyze community structure we rely on Onion model. All panels
related to community structure are based on [the onion study included in
grimoirelab-elk project.](https://github.com/chaoss/grimoirelab-elk/blob/master/doc/studies.md#onion-study)

Thus, structure is provided by dividing contributors into three main groups:
 * **Core**: those contributing **80% of the activity**. These are the most
 committed developers, and those on which the project relies most.
 * **Regular**: those contributing the next **15% of the activity**. These are
  people committed to the project, and most likely to become part of the
  core group or maybe were already in it. The core and regular teams together
  account for 95% of the activity.
 * **Casual**: those contributing the **last 5% of the activity**. There are
  people in the periphery of the project. However, they are important because
  it is very likely that future core and regular contributors will come out
  from this group.

In most models of FOSS development, where there are employees, they usually
start directly in regular or core, depending on their positions, experience
and responsibilities in the company. On the other hand, non-employees
generally start as a part of the casual group. Some of them will become
regular and maybe core contributors as they gain experience about the project.

## Use Cases
In order to understand panels, we have defined a set of use cases to guide
you in your journey to get the most of our community structure panels.
Please read first [General Details section](#general-details) to learn
some basic features you will find in all community structure panels.

### General Details
* Wherever you see **`_Global_`** as organization or project name, it means
    results computed for all organizations or projects together. We will
    see more on this within each use case.
* As data is pre-computed for performance reasons, **it is important to
    follow use cases described here to get meaningful results**. Use cases
    will guide you to the answers you can get from the panels.
* All panels have **a filter on top to select the data source**. By default
    Git is selected. These filters can be modified by using Data Source widget
    placed on first row. Depending on each panel layout it is at the left or
    right.

![Global View]({{ site.baseurl }}/assets/images/onion_filters_on_top_2.png)
###### Figure 1a. Panel filter on top and Data Source widget at the right
![Global View]({{ site.baseurl }}/assets/images/onion_filters_on_top.png)
###### Figure 1b. Panel filter on top and Data Source widget at the left

* **Only one of data source filter should be active at the same time**.
    In Kibana/Kibiter, filters are combined by means of `AND` operators.
    E.g. if we enable Git and GitHub filters, under the hood we get
    an ElasticSearch query like:
    ```
    data_source=git AND data_source=github
    ```
    Thus, by selecting more than one data source filter at the same time,
    we won't get any result, because data come from one data source or another,
    but not several at the same time.
* Data Source widget automatically manages this for you, so you just need to
    select the desired data source in the drop down list and click on
    `Apply changes`.
* Data is meaningful only if **one and only one data source** is selected for
    filtering.

### UC1. Onion model for the whole community.
This use case is covered by **Overall Community Structure** panel.

![Overall Onion Panel]({{ site.baseurl }}/assets/images/onion_overall.png)
###### Figure 2. Community Structure Panel

This panel shows the results of computing onion for all contributions in
a given data source.

On the top left corner we find the evolution of the differen onion roles
through time, divided in quaters. Just below, another bar chart shows the
evolution of contributions in such a way one can compare both to better
understand how groups evolve.

On the right hand side there is a table showing number of people and
contributions by role for the selected time frame.

The bottom of the panel contains a table of authors, showing the total
number of contributions of eaxh one in the selected time frame together
with the number of quarters that author has been active in the community.


### UC2. Onion model for a given organization.
This use case is covered by **Community Structure by Organization** panel.

![Onion by Organization Panel]({{ site.baseurl }}/assets/images/onion_orgs.png)
###### Figure 3. Community Structure by Organization Panel

This panel splits data into organizations. **Onion model is computed individually
for each organization**.

In order to have meaningful data, we need to select the organization we
are interested in from the donut chart on top right corner or from
organizations table just below. Then, a new filter will appear on top, next
to the other ones, and we'll get the data we need in the panel.

![Organization Filter]({{ site.baseurl }}/assets/images/onion_filtered_by_org.png)
###### Figure 4. Apllying a filter on Community Structure by Organization Panel


**LIMITATION: when no organization is selected for filtering** (as
in Figure 3) chart on the top left corner shows sums group sizes
&mdash;core, regular, casual&mdash; of all organizations. That is, if we have
organization A with 5 people in core group for 2018Q1 and organization B
with 2 people in core group for 2018Q1, bar chart will show 7 as value
for core group, which **is not** the result of computing onion for both organizations
together but the sum of their specific results. This is due to the use of
pre-computed values by organizations. In order to get data for all
organizations together, see
[UC1. Onion model for the whole community.](#uc1-onion-model-for-the-whole-community)


### UC3. Onion model for a given project.
This use case is covered by **Community Structure by Project** panel.

![Onion by Organization Panel]({{ site.baseurl }}/assets/images/onion_projects.png)
###### Figure 5. Community Structure by Project Panel

This panel splits data into projects. **Onion model is computed individually
for each project**.

In order to have meaningful data, we need to select the project we
are interested in from the donut chart on top right corner or from
projects table just below. Then, a new filter will appear on top, next
to the other ones, and we'll get the data we need in the panel.

![Organization Filter]({{ site.baseurl }}/assets/images/onion_filtered_by_project.png)
###### Figure 6. Apllying a filter on Community Structure by Project Panel


**LIMITATION: when no project is selected for filtering** (as
in Figure 5) chart on the top left corner shows sums group sizes
&mdash;core, regular, casual&mdash; of all projects. That is, if we have
project A with 5 people in core group for 2018Q1 and project B
with 2 people in core group for 2018Q1, bar chart will show 7 as value
for core group, which **is not** the result of computing onion for both projects
together but the sum of their specific results. This is due to the use of
pre-computed values by projects. In order to get data for all
projects together, see
[UC1. Onion model for the whole community.](#uc1-onion-model-for-the-whole-community)


## Implementation Details
To better understand how panels are built we need to understand how Onion metric
is calculated. We use different levels of granularity to compute onion for
different groups of contributors:

* **Globally**: takes all data into account, i.e., computes onion for each and
    every contribution, no matter what organization or project authors
    belongs to. It is denoted as `_Global_` in panels to avoid collisions
    with existing organization or project names.
* **By organization**: splits data by organization and compute onion for each
    one.
* **By project**: same as above, but splits data by project.
* **By organization and project**: splits data by organization and project, so
    onion roles are associated to a person in an organization and a project.

All this data is pre-computed and stored for performance reasons.

Each item in our current onion indices contains fields specified at
[study schema definition in grimoirelab-elk project](https://github.com/chaoss/grimoirelab-elk/blob/master/schema/onion.csv).

More details on study configuration can be found at [the onion study documentation included in
grimoirelab-elk project](https://github.com/chaoss/grimoirelab-elk/blob/master/doc/studies.md#onion-study).
