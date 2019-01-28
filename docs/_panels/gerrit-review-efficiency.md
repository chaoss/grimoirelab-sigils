---
title: Gerrit Review Efficiency
description: efficiency closing reviews in Gerrit.
author: Bitergia
screenshot: sigils/demographics.png
created_at: 
grimoirelab_version: 0.2.1
layout: panel
---

This panel offers a view of efficiency closing reviews based on two metrics:
* **REI**: Review Efficiency Index, defined as the number of closed reviews divided
  by the number of open ones in a given period of time. Measures efficiency closing reviews.
* **Lead Time**: the time expressed in days between the initiation and completion of a production
  process, in this case, a review. Shown in average in this panel.
* **Time to Merge**: time from review creation to the moment in which it's merged or abandoned.

Filtering by Organization and Project is allowed by using the top left corner
widget.

**REI** is shown next to filtering widget. Moving average is set to 8 weeks
to identify changes in trends. Average is also shown as reference. REI values
greater than 1 means the community is closing more reviews than those they are
opening. Values smaller than 1 means the opposite, i.e., more reviews open than
those closed during a given time frame.

**Median Time to Merge** gauge is set to show green color for less than 7 days, yellow
for values from 7 to 30 days and red from 30 to 90 days. This means we are
considering a week as a good time to merge. This is just a visual reference and
you can always rely on the number, ignoring this color scheme.

Next to this gauge, **Lead Time** shows the average Time to Merge expressed in days together to its
trend. This helps to identify peaks and visualize the global evolution of time
spent in closing reviews.

Finally, a table on the right splits **Median Time to Merge** by repository,
giving an insight on the differences among them.
