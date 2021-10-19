---
title: Discourse Devrel
description: DevRel related metrics for Discourse.
author: Bitergia
screenshot: sigils/discourse_devrel.png
created_at: 2020-06-02
grimoirelab_version: 0.2.40
layout: panel
---

This dashboard focuses on Discourse activity and active authors in different time slots.


* To filter bots there is a filter on top of the dashboard.
* Links to Hatstall are provided within the tables to allow to editing profiles in case there are unmerged profiles or bots that are not marked as such.
* There are 3 tables, one per each time interval.

The metrics you'll find are:
* **Posts Created**: Number of new posts by month 30/60/90 day rolling avg posts/day. This calculates 
the numbers per day, as rolling averages are per day too. Metric says posts: a post is either
a question or an answer (this can be easily modified to count only one of them or to count 
them separately).
* **Posts**: Top 30 contributors in the last 30/60/90 days (excluding any automated tooling, 
see bots filter on top).

### Acknowledgments

We would like to thank Frances Chao-Gay and 
[benny Vasquez](https://github.com/bennyvasquez) from [chef.io](https://www.chef.io/) 
project for their collaboration. This dashboard hadn't been
possible without them. It is based on their ideas and they were the actual reviewers of
the work done.

We had also the opportunity of discussing the use case with benny during one of our
bi-weekly CHAOSS-GrimoireLab calls, 
[publicly available on YouTube](https://www.youtube.com/watch?v=sWyHzCVz8e0). 

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`discourse` index][discourse-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-discourse] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import discourse-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import discourse.json
```

[discourse-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/discourse.csv
[sirmordred-discourse]: https://github.com/chaoss/grimoirelab-sirmordred#discourse-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/discourse.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/discourse-index-pattern.json
