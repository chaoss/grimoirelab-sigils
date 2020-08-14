---
title: GitHub Devrel
description: DevRel related metrics for GitHub.
author: Bitergia
screenshot: sigils/github_devrel.png
created_at: 2020-06-04
grimoirelab_version: 0.2.40
layout: panel
---

This dashboard focuses on GitHub activity, commits and pull requests, and top contributors.

To filter bots there is a filter on top of the dashboard.
* Links to Hatstall are provided within the tables to allow to edit profiles.
* There are 3 tables for each visualization, one per each time interval.

The visualizations you can find on the dashboard are: 
* **Project Filter**: GitHub all projects, or by project. This is a selector to filter projects. 
* **Commits & Pull Requests General Numbers**: number of authors and organizations for commits
 and pull requests. An author of a pull request is the person who submitted the first version
 of this (not any further iterations).
* **Top 30 contributors** in the last 30/60/90 days, for commits and Pull Requests, and 
excluding any automated tooling (see bots filter on top).
* **Pull Request created**: Number of pull requests / day 30/60/90 day rolling avg pull
 requests / day.
 
### Acknowledgments

We would like to thank Frances Chao-Gay and 
[Benny Vasquez](https://github.com/bennyvasquez) from [chef.io](https://www.chef.io/) 
project for their collaboration. This dashboard hadn't been
possible without them. It is based on their ideas and they were the actual reviewers of
the work done.

We had also the opportunity of discussing the use case with Benny during one of our
bi-weekly CHAOSS-GrimoireLab calls, 
[publicly available on YouTube](https://www.youtube.com/watch?v=sWyHzCVz8e0). 

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check `all_enriched` index is available on your GrimoireLab instance
([grimoirelab-sirmordred][sirmordred-general] automatically creates this alias for you).
* Check [`git` index][git-schema] is available on your GrimoireLab instance 
(see [grimoirelab-sirmordred documentation][sirmordred-git] for details on how to deploy it).
* Check [`github_issues` index][github_issues-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-github_issues] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern-1] [![Index Pattern][ip-icon]][index-pattern-2] [![Index Pattern][ip-icon]][index-pattern-3] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Patterns** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import all_enriched-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import git-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import github_issues-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import github_devrel.json
```

[git-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/git.csv
[sirmordred-git]: https://github.com/chaoss/grimoirelab-sirmordred#git-
[github_issues-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/github_issues.csv
[sirmordred-github_issues]: https://github.com/chaoss/grimoirelab-sirmordred#issue
[sirmordred-general]: https://github.com/chaoss/grimoirelab-sirmordred#general
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github_devrel.json
[index-pattern-1]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/all_enriched-index-pattern.json
[index-pattern-2]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/git-index-pattern.json
[index-pattern-3]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github_issues-index-pattern.json
