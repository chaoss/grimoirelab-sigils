How to Contribute
-----------------
In order to get your contribution accepted, please follow the following requirements:

For panels:
* Export the panel using Kidash tool. Kidash is Bitergia's tool for importing/exporting 
panels. All panels in this repo follows Kidash JSON format, which is slightly different
from Kibana's format. See [Using Kidash to Import/Export Panels](#using-kidash-to-importexport-panels)
* There are two special panels: **Overview** and **Data Status**. These panels use widgets from
almost all available data sources. In order to avoid noise when importing them, once exported
we need to remove the content of `index_patterns` JSON object, i.e., make it an empty list:

```
{
    "dashboard": {
        "id": "Overview",
        "value": {
            ...
        }
    },
    "index_patterns": [],
                     ^^^^
```


* Panel should work in Kibana/Kibiter 5.1.1.
* Follow naming conventions explained in our [README.md](README.md)
* Follow [our suggestions on working with branches](#working-with-branches)
* Use GitHub interface to create a new Pull Request from your branch to our master repo!
  * If your panel needs something special, like creating a specific alias on ES, please use comments space
  in your Pull Request to give us instructions on how to proceed.

For other files:
* Follow [our suggestions on working with branches](#working-with-branches)
* Use GitHub interface to create a new Pull Request from your branch to our master repo!

Working with Branches
---------------------
The usual workflow we encourage you to follow is:
* Fork repository.
* Create a new branch with a meaningful name. As you are going to create or modify a panel, use
the name of the panel together with some keywords about what that branch intends to achieve. For
instance, for a new git timing panel we would use a branch called `git-timing`. For a fix on
widgets related to organizations in an existing gerrit timing panel we would use something like
`gerrit-timing-fix-orgs`.


Using Kidash to Import/Export Panels
------------------------------------
Kidash is part of [GrimoireELK](https://github.com/grimoirelab/GrimoireELK) toolchain
and can be installed as a pypi package: `grimoire-kidash` [![PyPI version](https://badge.fury.io/py/grimoire-kidash.svg)](https://badge.fury.io/py/grimoire-kidash)
We recommend you to install it in a Python Virtual Environment:
```
$> pyvenv kidash-venv
$> . kidash-venv/bin/activate
(kidash-venv)$> pip3 install grimoire kidash
(kidash-venv)$> kidash.py
usage: usage: kidash [options]
kidash.py: error: --export or --import or --list needed
```

As starting point, you will probably want to import some existing panels into your
Kibana environment. Choose the panel you want to work with from [panels/json](json) 
folder and import it to your Kibana/Kibiter using a line like the following:
```
(kidash-venv)$> kidash.py -e https://<user>:<password>@<domain>:443/<path>/ --import <file_name>.json
```
And you should be able to load the panel from your Kibana/Kibiter instance.

In order to export the panel you have been working on, once Kidash is installed 
(we recommend you to do it in a Python virtual environment), you can use a line
like the following:
```
(kidash-venv)$> kidash.py -e https://<user>:<password>@<domain>:443/<path>/ --dashboard <dashboard_name> --export <file_name>.json
```
**Notice that <dashboard_name> is the name of the panel in Kibana, substituting spaces by dashes**, e.g. a panel
named `Git Timing` in Kibana should be written as `Git-Timing` in kidash command line.

And you will get a wondeful JSON file ready for sharing with the community!
