---
title: GitHub Issues Comments and Collaboration
description: activity and collaboration among people on GitHub issues.
author: Bitergia
screenshot: sigils/github-issues-comments-and-collaboration.png
created_at: 
grimoirelab_version: 0.2.33
layout: panel
---

This dashboard focuses on collaboration among people. Its goal is providing insights about the
most active and participative individuals. It also provides information split by repository and
project in order to be able to compare data from a single person to data from the whole repository
and project.

**Collaboration** is analyzed through the number of issues commented by a set of users. Thus we
consider they are "collaborating" on that thread as they are sharing comments. As a simple
way to measure these interactions **we consider the more the messages written in that thread, the stronger
the collaboration is**.

* **Summary**: general numbers to give an idea about the amount of data taken into account given the
    current dashboard filters and time frame.
* **Collaboration Network**: shows people as nodes. 
    * Node size is the number of issues they created. 
    * Edges link people commenting on the same issue thread. 
    * Edge size represents the number of comments.
* **People**: this table split data by persons. Each row consists of:
    * Issues: number of issues created by that person.
    * Comments: number of comments created by that person.
    * +1: number of `+1` reactions received by issues or comments created by that person.
    * +1 Ratio: result of dividing the previous value by the total count of issues and comments created by
        that person.
    * Reactions Ratio: same as `1 Ratio` but for all kind of reactions. Useful to compare to `+1 Ratio`
        and thus analyze the impact of people's contributions. 
* **Repositories**: same as **People** table but split by repository.
* **Projects**:  same as **People** table but split by project.

Tables are here to allow to drill down on people's contributions and understand their actual impact on the
different repositories and projects. Nevertheless, these tables provide
enough information for comparing GitHub issues activity on the different repositories and projects,
what could be considered as a side use case.

### Building the Dashboard: details about Index and Fields

This dashboard is built on top of [github2_issues][github2_issues-schema] index. It is worth to mention that in GitHub everything
are issues, even pull requests, so issues corresponding to pull requests will appear in this index too.
To avoid counting them as issues, we filter out pull requests by means of a filter
named `Not Pull Requests` placed on top of the dashboard.

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`github2_issues` index][github2_issues-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-github2_issues] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import github2_issues-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import github2_issues_comments_and_collaboration.json
```

[github2_issues-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/github2_issues.csv
[sirmordred-github2_issues]: https://github.com/chaoss/grimoirelab-sirmordred#github2-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github2_issues-index-pattern.json
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github2_issues_comments_and_collaboration.json
