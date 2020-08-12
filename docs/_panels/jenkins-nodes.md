---
title: Jenkins Nodes
description: Information about Jenkins Nodes
author: Bitergia
screenshot: sigils/jenkins-nodes.png
created_at: 2020-03-11
grimoirelab_version: 0.2.38
layout: panel
---

This panel provides an overview of the nodes used by the Jenkins instances.

## Metrics

From left to right and top to bottom, the metrics provided are:

* **Summary**: total numbers of builds, jobs, nodes and build durations.
* **Results**: a pie chart that summarizes the proportions of the build results (success, failure, unstable, aborted).
* **Projects and Nodes**: a pie chart that highlights the number of nodes per project.
* **Jobs**: a bar chart that shows the evolution of the jobs.
* **Duration Trend**: a line chart that shows the evolution of the build durations.
* **Success/Failures in percentage**: a stacked bar chart that allows to compare the proportion of build success and failures.
* **Nodes**: a table that details the number of builds, durations, success and failures per node.

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`jenkins` index][jenkins-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-jenkins] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import jenkins-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import jenkins_nodes.json
```

[jenkins-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/jenkins.csv
[sirmordred-jenkins]: https://github.com/chaoss/grimoirelab-sirmordred#jenkins-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/jenkins-index-pattern.json
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/jenkins_nodes.json
