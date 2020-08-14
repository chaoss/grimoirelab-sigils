---
title: Git
description: metrics focused on Git commits.
author: Bitergia
screenshot: sigils/git.png
created_at: 
grimoirelab_version: 0.2.0
layout: panel
---

The Git panel shows information about commits in git repositories. For each
commit, git stores meta-information about who authored the commit (author),
and when, and about who included the commit in the repository (committer),
and when.

Each author and committer in git are usually identified by a name and an email
address. We use the information in the email addresses to find domains and as a
first approach to enrich the information to obtain organizations information.

Dates and times (author time, committer time) in git are expressed usually in
the time zone of the computer where the person performed the action (creation of
the commit, or merging of it in the repository). We use that to display time
zone information.


### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`git` index][git-schema] is available on your GrimoireLab instance 
(see [grimoirelab-sirmordred documentation][sirmordred-git] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import git-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import git.json
```


[git-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/git.csv
[sirmordred-git]: https://github.com/chaoss/grimoirelab-sirmordred#git-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/git.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/git-index-pattern.json
