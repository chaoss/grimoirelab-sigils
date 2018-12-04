# How to Contribute

Please follow these guidelines before sending your contribution.

## Directory structure

There are two important places in Sigils:
* `docs/` directory: it contains panels documentation.
* `<collection_name>/` directory: it contains JSON files corresponding to a collection named `<collection_name>`. The current standard Bitergia's collection is `panels/`.

We refer to these directories later for creating your Pull Request.

## Opening a new Pull Request

A new Pull Request could contain a panel and its corresponding documentation. A panel with outdated documentation will not be accepted. Once in your branch, follow below steps to export your panel(s) and create/update documentation if needed. 

### Working with branches

The usual workflow we encourage you to follow is:
* Fork repository.
* Create a new branch with a meaningful name. As you are going to create or modify a panel, use
the name of the panel together with some keywords about what that branch intends to achieve. For
instance, for a new git timing panel we would use a branch called `git-timing`. For a fix on
widgets related to organizations in an existing gerrit timing panel we would use something like
`gerrit-timing-fix-orgs`.

### Importing panels

If you don't have Kidash tool installed, please see [#installing-kidash](installing Kidash section).

As starting point, you will probably want to import some existing panels into your
Kibana environment. Choose the panel you want to work with, for instance from [panels/json](json)
folder and import it to your Kibana/Kibiter using a line like the following:
```
(kidash-venv)$> kidash -e <elasticsearch_endpoint> --import <file_name>.json
```
And you should be able to load the panel from your Kibana/Kibiter instance. Notice you may need to import also some index pattern files to get the panel working. You can do it with the same line, just using index pattern file name as <file_name>.

For instance, to import Git panel to an empty environment:
```
(kidash-venv)$> kidash -e <elasticsearch_endpoint> --import git.json

(kidash-venv)$> kidash -e <elasticsearch_endpoint> --import git-index-pattern.json

```

### Exporting panel

* Panel should work in Kibana/Kibiter 6.1.0.
* Follow naming conventions explained in our [README.md](README.md)
* Export the panel using Kidash tool. If you don't have Kidash tool installed, please see [#installing-kidash](installing Kidash section).

In order to **export the panel you have been working on**, once Kidash is installed, you can use a line like the one below:
```
(kidash-venv)$> kidash --split-index-patterns -e <elasticsearch_endpoint> --dashboard <dashboard_name> --export <file_name>.json
```
Two important details:
* Index patterns are stored in separate files, this is why the option `--split-index-patterns` is needed.
* Only add your index pattern(s) to your PR in case you modified something related to that index pattern (fields format, scripted fields, new fields added) or if you are using a totally new index pattern.
* `<dashboard_name>` is the identifier of the panel in Kibiter, that is the string you see after last slash of the URL when the panel is loaded in your browser.E.g.:
```
https://xxxxx.biterg.io/app/kibana#/dashboard/Gerrit?_g=(refreshInterval...  

identifier --> Gerrit

https://xxxxx.biterg.io/app/kibana#/dashboard/2e968fe0-b1bb-11e8-8aac-ef7fd4d8cbad?_g=(refreshInterval:(display:....
identifier ---> 2e968fe0-b1bb-11e8-8aac-ef7fd4d8cbad
```

After the execution of kidash you should get at least two files, one per each index pattern used in the panel and one with the panel itself. You should put them under `<collection_name>/` directory.

### Adding or updating documentation

If you are adding a new panel or updating an existing one, you will be required to document it. Bug fixes usually don't need documentation updates.

Under `docs/` directory you'll find the following structure:
```
.
├── docs
│   ├── _layouts
│   ├── _panels
|   ├── assets
│   │   └── images
│   ├── _config.yml
│   └── index.html
│    
├── panels
├── CONTRIBUTING.md
├── LICENSE.md
└── README.md
```
As you can see, for each collection we have a directory in root folder and then another one in `docs/`. For instance, `panels` collection has a directory `panels/` in root folder (this is actually a link to `json` directory, that is the legacy directory for Bitergia's panel) and then a `_panels` in `docs/` (notice the `_` before the name, this is needed for Jekyll collections to work).

What you may need to modify is:
* `_config.yml` and `index.html`: if you added a new collection, you need to add a collection in `_config.yml` similar to `panels`. You also need to add a loop in `index.html` to iterate over all docs in the collection and add links to them, again it would be copying, pasting and slightly modifying what is already done for `panels`.
* `_panels/` or `_<collection_name>/`: here you need to put MarkDown files for your panels or updating those you modified. These files must contain a Jekyll Front Matter like the following in order to be correctly rendered (modify title and description if needed):
```
---
title: Community Structure
description: find who are your core, regular and casual contributors.
layout: panel
---
```
* `assets/images/`: the place to store screenshots, if needed.

For more details on how to build local links, please see the existing files. For instance, this would be a link to an image:
```
![Global View]({{ site.baseurl }}/assets/images/onion_filters_on_top_2.png)
###### Figure 1a. Panel filter on top and Data Source widget at the right
```
And this a link to another local MarkDown file:
```
[Data Status](data-status.md)
```

### Creating your Pull Request

Use GitHub interface to create a new Pull Request from your branch to our master repo.
  * If your panel needs something special, like creating a specific alias on ES, please use comments space
  in your Pull Request to give us instructions on how to proceed.
  
## Installing kidash

Kidash is Bitergia's tool for importing/exporting
panels. All panels in this repo follows Kidash JSON format, which is slightly different
from Kibana's format.

Kidash is part of [GrimoireELK](https://github.com/grimoirelab/GrimoireELK) toolchain
and can be installed as a pypi package: `grimoire-kidash` [![PyPI version](https://badge.fury.io/py/grimoire-kidash.svg)](https://badge.fury.io/py/grimoire-kidash)
We recommend you to install it in a Python Virtual Environment:
```
$> python -m venv kidash-venv
$> . kidash-venv/bin/activate
(kidash-venv)$> pip3 install kidash
(kidash-venv)$> kidash
usage: usage: kidash [options]
kidash: error: --export or --import or --list needed
```





