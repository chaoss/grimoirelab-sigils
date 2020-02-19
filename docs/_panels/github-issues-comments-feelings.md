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
GrimoireLab are available in the [GrimoireLab repository](https://github.com/chaoss/grimoirelab/tree/master/third-party#docker-image-cross-nlp-rest-api).

The fields that can be used to aggregate sentiment and emotion data are the followings:

* **has_emotion**: 0 if the emotion has been extracted yet from the comment, 1 otherwise
* **has_sentiment**: 0 if the sentiment has been extracted yet from the comment, 1 otherwise
* **feeling_emotion**: Label of the emotion
* **feeling_sentiment**: Label of the sentiment