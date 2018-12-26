---
title: GitLab Merge Requests Efficiency
description: efficiency solving (merging or closing) MRs on GitLab.
author: Miguel-Ángel Fernández
created_at: 2018-12-12
grimoirelab_version: 0.2.1
layout: panel
---

This panel offers a view of efficiency solving (merging or closing) merge requests based on three metrics:
* **REI**: Review Efficiency Index, defined as the number of solved (merged or closed) merge requests divided
  by the number of open ones in a given period of time. Measures efficiency solving merge requests.
* **Lead Time**:  the time expressed in days between the initiation and completion of a production
  process, in this case, a merge request. Shown in average in this panel.
* **Time to Merge**: time from merge request creation to the moment in which it's solved.

![GitLab Merge Requests Efficiency]({{ site.baseurl }}/assets/images/gitlab_mergerequests_efficiency.png)
###### Figure 1.GitLab Merge Requests Efficiency Panel

Filtering by Organization and Project is allowed by using the top left corner
widget.

**REI** is shown next to filtering widget. Moving average is set to 8 weeks
to identify changes in trends. Average is also shown as reference. REI values
greater than 1 means the community is solving more merge requests than those they are
opening. Values smaller than 1 means the opposite, i.e., more merge requests open than
those solved during a given time frame.

**Median Time to Merge** gauge is set to show green color for less than 7 days, yellow
for values from 7 to 30 days and red from 30 to 90 days. This means we are
considering a week as a good time to solve. This is just a visual reference and
you can always rely on the number, ignoring this color scheme.

Next to this gauge, **Lead Time** shows the average Time to Merge expressed in days together to its
trend. This helps to identify peaks and visualize the global evolution of time
spent in solving merge requests.

Finally, a table on the right splits **Median Time to Solve** by repository,
giving an insight on the differences among them.
