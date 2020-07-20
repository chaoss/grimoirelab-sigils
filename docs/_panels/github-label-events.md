---
title: GitHub Events - LabelEvents
description: metrics focused on the GitHub labeled/unlabeled events.
author: Bitergia
screenshot: sigils/github-label-events.png
created_at: 2020-06-09
grimoirelab_version: 0.2.0
layout: panel
---

This dashboard shows information related to the activity for labeling issues and pull requests. Such information
is derived from the labeling and unlabeling events returned by the GitHub API. The widgets in the dashboard are described below.

- **Selector** allows to focus on one or more labels.
- **Current labels** show the labels currently used in the project issues. It shouldn't be used for filtering labels.
- **Labels duration** shows the average time (in days) a label has been assigned to issues. It is worth noting that:
  - Closing events are not taken into account to compute the label durations. Thus, if a label is assigned to an issue and the issue is closed, there won't be any duration for that issue.
  - Partial times aren't taken into account. Thus, if a label is assigned and never unassigned to an issue, there won't be any duration for that issue.
  - When several labeling events occur one after another, with no unlabeling event among them, and then an unlabeling event occurs, the duration will be calculated from the unlabeling event to the most recent labeling one.  
- **Summary** highlights statistics of the labels used on the different projects and repositories.
- **Labels duration evolution** shows the avg. time of the label duration on issues on monthly basis.
- **Labeling/unlabeling actions** shows the evolution of labeling and unlabeling actions.
- **Labelers/unlabelers charts** focus on the users/organizations adding and removing labels.

### Building the Dashboard: details about Index and Fields

This dashboard is built on top of a search on [github_events] index which includes labeling, unlabeling and closing events. It is worth mentioning that the visualization
`Current labels` uses the issue labels information (attribute `issue_labels`) to show the labels currently in use, while the other visualizations rely on the label included
within the event (attribute `label`). Thus, the former shouldn't be used for focusing on a target label, but just for browsing purposes. Furthermore, the attribute `duration_from_previous_event` is empty
by default, it can be calculated via the ELK study `enrich_duration_analysis` (see details at in the [GitHubQL enricher]).

[github_events]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/github_events.csv
[GitHubQL enricher]: https://github.com/chaoss/grimoirelab-elk/blob/master/grimoire_elk/enriched/githubql.py