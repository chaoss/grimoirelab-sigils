---
title: Gerrit Approvals
description: metrics focused on Gerrit approvals.
author: Bitergia
screenshot: sigils/gerrit-approvals.png
created_at: 
grimoirelab_version: 0.2.37
layout: panel
---

This dashboard focuses on metrics derived from Gerrit approvals. It provides insights in terms of projects, repositories, reviewers and submitters. Due to automation is a key part in Gerrit workflow a filter is set on the top of the dashboard (`NOT Bots`) to ignore any kind of activity issued by bots. This is the default behaviour. The visualizations composing the dashboard are described below.

* **Total Changesets and Approvals**: A set of metrics that show the total number of changesets and approvals.
* **Activity by Project and Repository**: A table that summarizes the number of changesets, patchsets and approvals per project and repository.
* **Approvals by Reviewer**: A table that describes the number of approvals grouped by their values (i.e., -2, -1, +1, +2) per reviewer.
* **Approvals by Reviewer, Project and Repo**: A table that describes the number of approvals and their values per review, project and repository.
* **Approvals by Submitter**: A table that summarizes the number of approvals and their values per changeset submitter.
