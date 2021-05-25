---
title: Mattermost
description: metrics for Mattermost.
author: Bitergia
screenshot: sigils/mattermost.png
created_at: May 25th, 2021
grimoirelab_version: 0.2.55
layout: panel
---

This dashboard focuses on Mattermost activity, active users and channels.

To filter bots there is a filter on top of the dashboard. Server Activity is excluded 
from specific visualizations (see [Excluding Server Activity](#excluding-server-activity)).

## Metrics

The metrics provided are:

* **Mattermost** total number of channels, messages, participants, replies, reactions, and
attachments.
* **Organizations** a pie chart that summarizes the messages by organization.
* **Reactions**  a pie chart that summarizes the reactions.
* **Messages, over time** a bar chart that shows the evolution of the number of messages over time.
* **Participants, over time** a bar chart that shows the evolution of the number of participants over time.
* **Organizations** a table sorted by organizations that details the number of channels, messages, and
  participants.
* **Top Participants** a table sorted by the number of the messages that details the participant name,
  number of messages, channels, first message date, and the last message date.
* **Projects** a table sorted by projects that details the number of channels, messages, and participants.
* **Top 20 Hashtags** a tag cloud of top 20 hashtags.
* **Top 20 terms** a tag cloud of top 20 terms.
* **Channels** a table sorted by the number of messages that details the name of the channel, number of messages,
  participants, replies, reactions, created date, and deleted date.
* **Last Messages** a search sorted by when the message was posted that details the message, author name,
  channel name, number of reactions, hashtags, and user roles.
  
### Excluding Server Activity
Server messages are filtered out of these metrics. Specifically we exclude messages
corresponding to the following subtypes:
 * `system_channel_deleted`
 * `system_join_channel`
 * `system_leave_channel`

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`mattermost` index][mattermost-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-mattermost] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import mattermost-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import mattermost.json
```

[mattermost-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/mattermost.csv
[sirmordred-mattermost]: https://github.com/chaoss/grimoirelab-sirmordred#mattermost-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/mattermost-index-pattern.json
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/mattermost.json
