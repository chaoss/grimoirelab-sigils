---
title: README
description: quick start information.
layout: default
---
## Dashboard Panels

Please visit our [FAM - Frequently Asked Metrics](fam.md) for a list of the usually
requested metrics. This document provides links and images to how to calculate
those.

When you come to Bitergias' dashboard you will find data from several data sources
organized in several panels. Depending on the amount of information or on
information nature, sometimes you will find information from a given data
source logically split across several panels, being each of them based on a
different use case.

* [Standard Panels](#standard-panels)
* [Dashboard Customization](#dashboard-customization)

## Standard Panels

The following is a list with the several panels available in the dashboard. All of them are either dependent from a data source or contains information from several data sources at the same time.

* Data Source: **Any**
  * [Overview](overview.md): summary of the available data sources about **activity** and **community**.
  * [Data Status](data-status.md): summary of the data freshness available in the dashboard.
* Data Source: **Apache**
* Data Source: **Askbot**
* Data Source: **Bugzilla**
  * Bugzilla Overview: general metrics about **activity** and **community** in Gerrit repositories.
  * Bugzilla Timing: **process** metrics such as engineering bottlenecks and time to code review estimations.
  * Bugzilla Backlog: **process** metrics to help developers to focus on the open changesets/open backlog of the community in Gerrit.
* Data Source: **Confluence**
* Data Source: **Discourse**
* Data Source: **Gerrit**
  * Gerrit Overview: general metrics about **activity** and **community** in Gerrit repositories.
  * Gerrit Timing: **process** metrics such as engineering bottlenecks and time to code review estimations.
  * Gerrit Backlog: **process** metrics to help developers to focus on the open changesets/open backlog of the community in Gerrit.
* Data Source: **Git**
  * [Git Overview](git.md): general metrics about **activity** and **community** in Git repositories.
  * [Git Demographics](git-demographics.md): newcomers (those attracted) and people leaving the **community** in the Git repositories.
* Data Source: **GitHub**
  * [GitHub Issues Overview](github-issues.md): general metrics about **activity** and **community** in GitHub issues repositories.
  * [GitHub Pull Requests Overview](github-pullrequests.md): general metrics about **activity** and **community** in GitHub pull requests repositories.
  * [GitHub Issues Timing](github-issues-timing.md): **process** metrics such as engineering bottlenecks and time to close issues estimations.
  * [GitHub Pull Requests Timing](github-pullrequests-timing.md): **process** metrics such as engineering bottlenecks and time to code review estimations.
  * [GitHub Backlog](github-backlog.md): **process** metrics to help developers to focus on the pull requests/issues/open backlog of the community in GitHub.
* Data Source: **Google Hits**
* Data Source: **IRC**
* Data Source: **Jenkins**
* Data Source: **Jira**
  * Jira Overview: general metrics about **activity** and **community** in Jira repositories.
  * Jira Timing: **process** metrics such as engineering bottlenecks and time to close issues estimations.
  * Jira Backlog: **process** metrics to help developers to focus on the open issues/open backlog of the community in Jira.
  * Jira Effort: **process** metrics to help developers to understand their effort estimations and work in progress.
* Data Source: **Kitsune**
* Data Source: **Mailing List**
* Data Source: **Maniphest**
* Data Source: **Mediawiki**
* Data Source: **Meetup**
* Data Source: **Redmine**
  * Redmine Overview: general metrics about **activity** and **community** in Redmine repositories.
  * Redmine Timing: **process** metrics such as engineering bottlenecks and time to close issues estimations.
  * Redmine Backlog: **process** metrics to help developers to focus on the open issues/open backlog of the community in Redmine.
* Data Source: **Reps**
* Data Source: **RSS**
* Data Source: **Stackoverflow**
* Data Source: **Telegram**
* Data Source: **Twitter**

## Dashboard Customization

It is possible to create new panels or visualizations, or customizing the standard ones. Some recommendations to do that without breaking standard panels and visualizations can be read in the document linked below:

* [Dashboard Customization](dashboard-customization.md)

## Metrics

Each of the described panels contains several widgets and those provide information about some metrics over time, aggregated or filtered. Those are defined in the following document:

* [Basic Metrics Documentation](metrics.md)
