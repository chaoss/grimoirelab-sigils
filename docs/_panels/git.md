---
name: Git
description: metrics focused on Git commits.
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
