---
title: Slack Devrel
description: DevRel related metrics for Slack.
author: Bitergia
screenshot: sigils/slack_devrel.png
created_at: 2020-06-08
grimoirelab_version: 0.2.40
layout: panel
---

This dashboard focuses on Slack activity, active users, and channel members. 

To filter bots there is a filter on top of the dashboard. Server Activity is excluded 
from specific visualizations (see [Excluding Server Activity](#excluding-server-activity))
because doing it at dashboard level would create a conflict with the way we identify
new users by looking at `join` messages to specific channels 
(see [How to customize our definition of `New Users`](#how-to-customize-our-definition-of-new-users)).

The visualizations you can find on the dashboard are:
* **General Numbers** widget displays aggregated numbers for the time slot of analysis.

* **New Users** counts **number of users joining one of the following 
channels: `#announcements`, `#community-meetings`, or `#devrel`**. Note that if a given user 
would join two of them at different dates we could count them twice as we can only count 
unique users joining those channels between the dates specified on each bar. 

* **Active Users**  gives an aggregated number of all people that have sent at least one 
message to any Slack channel during the time range we are analyzing. 

* **Channel Members**, **Active Members**, and **Inactive Members** show those members 
by each of the channels. The Channel Member value is given by Slack and not calculated by 
the tool. This is why the total number of **Channel Members** or **Active Members** is 
higher than the number of **Active Users**. **Members** are used to indicate those people
that are registered and/or participating in any of the channels. A member is different
from an **Active User** as a member belongs to a certain Slack channel and may or may not
be active in the period of analysis. An **Active User** has been active for sure.

* **Active Channels** displays the number of channels with messages during the period
 of analysis.
 
### How to customize our definition of `New Users`
The way we to identify new users is looking for the channels they joined. We can do it
because we know there is a set of channels to which new users are automatically added when
joining the community for the first time. However, this is specific from each community so, 
to get accurate results, you may need to modify this set of channels.
 
By default, the **New users** visualization relies on a Search named 
`slack_join_messages_to_main_channels`. This search looks for join messages on the
following channels:
 * `#announcements`
 * `#community-meetings`
 * `#devrel`

Thus, to customize the dashboard you should modify `slack_join_messages_to_main_channels`
according to your community.

### Excluding Server Activity
Server messages are filtered out of these metrics. Specifically we exclude messages
corresponding to the following subtypes:
 * `channel_join`
 * `bot_message`
 * `bot_add`
 
### Acknowledgments

We would like to thank Frances Chao-Gay and 
[benny Vasquez](https://github.com/bennyvasquez) from [chef.io](https://www.chef.io/) 
project for their collaboration. This dashboard hadn't been
possible without them. It is based on their ideas and they were the actual reviewers of
the work done.

We had also the opportunity of discussing the use case with benny during one of our
bi-weekly CHAOSS-GrimoireLab calls, 
[publicly available on YouTube](https://www.youtube.com/watch?v=sWyHzCVz8e0). 

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`slack` index][slack-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-slack] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import slack-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import slack_devrel.json
```

[slack-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/slack.csv
[sirmordred-slack]: https://github.com/chaoss/grimoirelab-sirmordred#slack-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/slack-index-pattern.json
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/slack_devrel.json
