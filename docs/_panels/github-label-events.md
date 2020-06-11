---
title: GitHub label-related events
description: metrics focused on the GitHub labeled/unlabeled events.
author: Bitergia
screenshot: sigils/github-label-events.png
created_at: 2020-06-09
grimoirelab_version: 0.2.0
layout: panel
---

This dashboard shows information related to the activity for labeling issues and pull requests. Such information
is derived from the labeling and unlabeling events returned by the GitHub API. The widgets in the dashboard are described below.

- **Projects** highlights statistics of the labels used on the different projects and repositories.
- **Pie charts** focus on the labels used and on the organizations and users adding and removing them.
- **Bar chart** shows the evolution of labeling and unlabeling actions.
- **Table** provides details about the activity on issues such as:
  - time to triage: from the issue creation until the first time a given label was added.
  - time to untriage: from the first time a label was added until the last time it was removed.
  - time to process: from the first time a label was added until the issue was closed.
  - time to close: from the creation of the issue until it was closed.