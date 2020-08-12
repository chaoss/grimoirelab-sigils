---
title: Gitter
description: metrics focused on Gitter messages.
author: Nitish Gupta <imnitish.ng@gmail.com>
screenshot: sigils/gitter.png
created_at: 2020-04-18 (YYYY-MM-DD)
grimoirelab_version: 0.2.0
layout: panel
---

The Gitter panel shows information about the messages sent in a Gitter room over time. 
The references included in these messages are used to highlight mentioned users and links 
to issue trackers (e.g., GitHub and GitLab) and other resources. 

Each user in a room is uniquely identified by a username and a user-id. This
information is used to identify the most active and mentioned users.
Similarly, the links shared are identified as github issues or pull requests
or categorized into URL hostnames if they belong to other sources (e.g., StackOverflow, Twitter).

Weekly, hourly and daily activity of the room is put into perspective by
widgets displaying the number of messages sent or unique users active in
the for selected time range. 

* **Top users chart** shows the people most active in a room (messages sent), for the selected time range.
* **Top mentioned URLs** gives an overview of the most common websites being linked in the room.
* **Weekly active users** displays the number of unique users active in the room per week.
* **Daily message count** displays the number of messages sent daily.
* **Users reading messages daily** shows the average number of users reading messages daily.
* **Top mentioned users/pull requests/issues** shows the respective most mentioned field in the messages over the selected time zone.
* **Messages sent per hour** shows the most active hours, when the most messages are sent in a day.

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`gitter` index][gitter-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-gitter] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import gitter-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import gitter.json
```

[gitter-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/gitter.csv
[sirmordred-gitter]: https://github.com/chaoss/grimoirelab-sirmordred#gitter-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/gitter-index-pattern.json
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/gitter.json
