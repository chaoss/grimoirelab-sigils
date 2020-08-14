---
title: Docker
description: Smells and dependencies from Dockerfiles.
author: Bitergia
screenshot: sigils/docker-smells-and-dependencies.png
created_at: 
grimoirelab_version: 0.2.38
layout: panel
---

This dashboard focuses on smells (i.e., indicators that possibly point to problems in terms of quality, security, etc.) and dependencies extracted from Dockerfiles. The widgets in the dashboards are described below.

* **Repository**: a selector useful to focus on one or more repositories.  
* **Dependency and smells metrics**: general numbers about the number of repositories, dependencies and smells found. 
* **Dependencies per repository**: a pie chart that shows the proportion of dependencies per repository.
* **Dependencies shared by repositories**: a table that summarizes the number of repositories sharing a dependency.
* **Dependencies graph**: a graph that highlights the relationships between repositories (circles) and Docker dependencies (boxes). The repository node size is proportional to the number of dependencies found in that repository. An edge exists between a dependency and a repository if that dependency has been found in a Dockerfile of the repository.
* **Smells per repository**: a pie chart that shows the proportion of smells per repository.
* **Smells shared by repositories**: a table that summarizes the number of repositories sharing a smell.
* **Smells graph**: a graph that highlights the relationships between repositories (circles) and Docker smells (boxes). The repository node size is proportional to the number of smells found in that repository. An edge exists between a smell and a repository if that smell has been found in a Dockerfile of the repository.

### Getting Dockerfiles smells and dependencies

Dockerfiles information data is obtained via [Jadolint](https://github.com/crossminer/crossJadolint), which is included in the [third-party](https://github.com/chaoss/grimoirelab/tree/master/third-party) image of GrimoireLab. 

Details about how to execute with GrimoireLab are available in the [Sirmordred repository](https://github.com/chaoss/grimoirelab-sirmordred)

### Building the Dashboard: details about Index and Fields

This dashboard is built on top of the [dockerdeps](https://github.com/chaoss/grimoirelab-elk/blob/master/schema/docker_deps.csv) and [dockersmells](https://github.com/chaoss/grimoirelab-elk/blob/master/schema/docker_smells.csv) indexes.

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`dockerdeps` index][dockerdeps-schema] and [`dockersmells` index][dockersmells-schema] are available
on your GrimoireLab instance (see [grimoirelab-sirmordred dockerdeps][sirmordred-dockerdeps] and
[grimoirelab-sirmordred dockersmells][sirmordred-dockersmells] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] [![Index Pattern][ip-icon]][index-pattern-2] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Patterns** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import docker_deps-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import docker_smells-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import docker.json
```

[dockerdeps-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/docker_deps.csv
[dockersmells-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/docker_smells.csv
[sirmordred-dockerdeps]: https://github.com/chaoss/grimoirelab-sirmordred#dockerdeps-
[sirmordred-dockersmells]: https://github.com/chaoss/grimoirelab-sirmordred#dockersmells-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/docker.json
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/docker_deps-index-pattern.json
[index-pattern-2]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/docker_smells-index-pattern.json
