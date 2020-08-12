---
title: GitHub Issues Comments Feelings
description: sentiment and emotions among people on GitHub issues.
author: Bitergia
screenshot: sigils/github-issues-comments-feelings.png
created_at: 
grimoirelab_version: 0.2.38
layout: panel
---

This dashboard enhances the dashboard about [GitHub issues comments and collaboration](https://chaoss.github.io/grimoirelab-sigils/panels/github-issues-comments-and-collaboration/) with
additional widgets that focus on emotion and sentiment data extracted from the issue comments. 

Emotions can be of the following types: `Anger`, `Fear`, `Joy`, `Love`, `Sadness` and `Surprise`. Comments which emotion has not
been identified are marked as `Not classified`.

Sentiment can assume the values: `Positive`, `Neutral` and `Negative`. Comments which sentiment has not been identified are marked as `Not classified`.

The new widgets are described below.

* **Emotions overview**: a pie chart that shows the proportion of the different emotions in the issue trackers.
* **Emotions per repository**: a pie chart that highlights the number of comments per emotion per each issue tracker. 
* **Emotions per issue**: a table that focuses on the number of comments per emotion per issue.
* **Sentiment overview**: a pie chart that shows the proportion of the different sentiments in the issue trackers.
* **Emotions per repository**: a pie chart that highlights the number of comments per sentiment per each issue tracker. 
* **Emotions per issue**: a table that focuses on the number of comments per sentiment per issue.

### Getting sentiment and emotion data

Sentiment and emotion data is obtained via the CROSS-NLP-REST-API tool. Details about how to execute it in combination with
GrimoireLab are available in the [GrimoireLab repository][sentiment].

The fields that can be used to aggregate sentiment and emotion data are the followings:

* **has_emotion**: 0 if the emotion has been extracted yet from the comment, 1 otherwise
* **has_sentiment**: 0 if the sentiment has been extracted yet from the comment, 1 otherwise
* **feeling_emotion**: Label of the emotion
* **feeling_sentiment**: Label of the sentiment

### Files
To use this dashboard with your own GrimoireLab deployment you need to:
* Check [`github2_issues` index][github2_issues-schema] is available on your GrimoireLab instance
(see [grimoirelab-sirmordred documentation][sirmordred-github2_issues] and [how to configure
third party stuff to add sentiment and emotion][sentiment] for details on how to deploy it).
* Import the following JSON files using [Kidash tool](https://github.com/chaoss/grimoirelab-kidash/).

| [![Index Pattern][ip-icon]][index-pattern] | | [![Dashboard][dash-icon]][dashboard] |
| :---------: | ---------- | :-------------: |
| **Index Pattern** | ----- | **Dashboard** |

<br />

#### Command line instructions
Once you have the data in place, if you need to manually upload the dashboard execute the
following commands:
```
kidash -e https://user:pass@localhost:443/data --import github2_issues-index-pattern.json
kidash -e https://user:pass@localhost:443/data --import github2_issues_comments_feelings.json
```

[sentiment]: https://github.com/chaoss/grimoirelab/tree/master/third-party#docker-image-cross-nlp-rest-api
[github2_issues-schema]: https://github.com/chaoss/grimoirelab-elk/blob/master/schema/github2_issues.csv
[sirmordred-github2_issues]: https://github.com/chaoss/grimoirelab-sirmordred#github2-
[dash-icon]: ../assets/images/icons/dashboard.png
[ip-icon]: ../assets/images/icons/file-ruled.png
[index-pattern]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github2_issues-index-pattern.json
[dashboard]: https://raw.githubusercontent.com/chaoss/grimoirelab-sigils/master/json/github2_issues_comments_feelings.json
