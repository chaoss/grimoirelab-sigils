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

Details about how to execute with GrimoireLab are available in the [Sirmordred repository](https://github.com/chaoss/grimoirelab-sirmordred#supported-data-sources)

### Building the Dashboard: details about Index and Fields

This dashboard is built on top of the [docker_deps](https://github.com/chaoss/grimoirelab-elk/blob/master/schema/docker_deps.csv) and [docker_smells](https://github.com/chaoss/grimoirelab-elk/blob/master/schema/docker_smells.csv) indexes.