---
title: Onion Analysis
description: general information about onion analysis.
author: Bitergia
screenshot: sigils/overall-community-structure.png
created_at: 
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
