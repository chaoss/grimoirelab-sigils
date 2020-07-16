---
title: GitHub closed events
description: metrics focused on the GitHub closed events.
author: Bitergia
screenshot: sigils/github-closed-events.png
created_at: 2020-04-21
grimoirelab_version: 0.2.0
layout: panel
---

This dashboard shows information related to the connection between the issues closed by pull requests. Such connections
are derived from the close events returned by the GitHub API. The widgets in the dashboard are described below.

- **Summary** gives an idea of the number of issues fixed.
- **Projects** highlights statistics of the number of issues fixed on the different projects.
- **Selector** allows focusing on one or more repositories.
- **Issues fixed by Organizations** offers a view of the issues fixed by pull request submitters' organizations.
- **Issues fixed by Organizations, over time** shows the evolution of the issues fixed by pull request submitters' organizations.
- **Table** provides details about the issues, the pull requests and the people involved (reporter, merger and submitter).

### Building the Dashboard: details about Index and Fields

This dashboard is built on top of a search on [github_events] index which includes the closing events by pull 
requests. The generation of such events is described below. 

When a pull request references a keyword (e.g., fixes, closes, resolves) and issue number, GitHub creates an 
association between the pull request and the issue. When the pull request is merged into the repository's default 
branch, the corresponding issue is automatically closed, and the corresponding event is generated.

By default, the closed event includes the author that triggered the action (e.g., the user that merged a pull request).
During the enrichment process, the issue reporter and pull request submitter are also added to the enriched 
items (attributes `reporter_*` and `submitter_*`).   

[github_events]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/github_events.csv