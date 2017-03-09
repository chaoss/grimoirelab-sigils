## Dashboard Panels

When you come to Bitergias' dashboard you'll find data from several data sources organized in several panels. Depending on the amount of information or on information nature, sometimes you'll find information from a given data source logically split across several panels, being each of them based on a different use case.

Below you can find a brief description of those panels and the use cases we were thinking about when we created them.

#### Overview

The Overview panel shows a summary of the repositories analyzed. Most of the visualizations found in it can be explored in more detail in the panels corresponding to the different analysis: Git, GitHub Issues, GitHub Issues Timing, GitHub Pull Requests, GitHub Pull Requests Timing and others.

#### Git

The Git panel shows information about commits in git repositories. For each commit, git stores meta-information about who authored the commit (author), and when, and about who included the commit in the repository (committer), and when.

Each author and committer in git are usually identified by a name and an email address. We use the information in the email addresses to find domains and as a first approach to enrich the information to obtain organizations information.

Dates and times (author time, committer time) in git are expressed usually in the time zone of the computer where the person performed the action (creation of the commit, or merging of it in the repository). We use that to display time zone information.

#### Git Demographics



#### GitHub Issues/Pull Requests

GitHub Issues and Pull Requests panels show information related to how community evolves in terms of submitters, domains and activity.

These panels show activity by domains and repositories. Each issue and pull request has a creation date and closing date, and of course a state (open or closed). We measure activity based on the amount of tickets created over time and their states.

This way, we can filter to get activity information related to a given submitter, domain or/and repository.


#### GitHub Issues/Pull Requests Timing

These panels contain information about evolution of Issues and Pull Requests in time. Although it shows submitters, repositories and domains as previous GitHub panels, here we focus on how long Issues and Pull Requests remain open.  Thus, we can work with this panel in a similar way for filtering, but dealing with different information.

Among other information we can find statistical information on closing times and also tables with the latest and the oldest Issues and Pull Requests.

#### GitHub Backlog

This panel focuses on pending tasks, that is, those Issues and Pull Requests that remain open (note that here we work with data retrieved in the moment of dashboard creation).

It is possible to see Issues and Pull Requests together or filter them by using the Activity donut on the top left corner. It is also possible to filter data in the same way as in other GitHub panels (by submitter, repository and domain).

A list with the oldest Issues and Pull Requests is also shown, providing direct links to them and some basic information as their titles, how long they've been open and when they were created.
