Generic Dashboards for GrimoireLab
==================================

Each of the files found in this directory are a JSON file that contains all of the information related to a Kibana dashboard.
This usually has information about the following artifacts:
* Original indexes where the information come from.
* Searches on those indexes that provide a sub-set of the information.
* Widgets either built on top of the original indexes or on top of the searches.
* Final panels that are an aggregation of several widgets.

Panels
------

A panel is composed by the several widgets this contains.
So far the panels proposed as generic are a mix of the several data sources available in a project. Those could be only focused on Git, but there are others such as review systems like Gerrit, IRC channels, mailing lists, etc.

This is the list of panels that can be found in this directory:
* git-'filters'.json: provides aggregated information about all of the gits in the analysis. Project/, repository, domains or organizations can be provided for filtering purposes.
* gerrit-'filters'.json: provides aggregated information from all of the gerrit projects. Project/, repository, domains or organizations can be provided for filtering purposes.
* gerrit-backlog-'filters'.json: provides specific widgets to track the backlog of the project with the addition of several filters per project or repository.
* mailinglists-'filters'.json: provides information about the discussions that take place in the several mailing lists.
* about.json: provides some widgets detailing this information and how to interact with the panels.
* overview-'filters'.json: provides a generic view of the dataset with some widgets that help to drill down the information from the whole list of data sources.

Files Naming
------------

Each panel may contain specific information in the name related to the available
filters. This is intended to help when automatically deploying those.

The current set of available filters are:
* organizations: this is a list or pie chart with information about organizations
* projects: this is a list or pie chart with information about projects

Some examples of file names:
* git-organizations-projects.json: this is a panel of Git containing information
about projects and organizations.
* git.json: this is a panel of Git containing basic filters about authors and
repositories
* git-organizations.json: this is a panel of Git containing organizations filters


Widgets Naming
--------------

```
 <data_source>_<metric_used>

 Example: git_top_authors
 Example: git_authors
```

Where data source could be git, gerrit, mbox, etc.

Widgets Title Naming
--------------------

In general, titles should follow the same naming scheme as the widget itself, substituting underscore characters by single spaces and adding capital letters:

```
 <data_source> <metric_used>
 
 Example: Git Top Authors
 Example: Git Authors
```

Nevertheless, **widgets title depends on the name of the panel** in which the widgets are located.

**If the panel shows information for several data sources, then the name of the data source must be included**. For example, it's the case of Data Status Panel, because it contains the same information per data source, so using data source name in title is mandatory.  

**If the name of the data source is included in the title of the panel, then the name of the data source shouldn't be included in widgets' title**, except in cases where it could help understand what the widget contains.  

Searches Naming
---------------

```
Search:_<field>:<search>

Example: Search:_pull_request:true
```


Indexes Naming
--------------

```
<data_source>

Example: git
Example: gerrit
Example: stackoverflow
Example: jira
Example: bugzilla
```

Aliases Naming <a id="Aliases-Naming"></a>
--------------

For each index there should be as many aliases as date fields stored in that index. Each alias is intended to be used for building panels or visualizations based on different time series. The name of an alias should follow the following pattern:

```
<data_source_name>_<field_name>

Example for git index and metadata__timestamp:
git_metadata__timestamp

Example for git index and metadata__updated_on:
git_metadata__updated_on

Example for jenkins and created_at field:
jenkins_created_at
```

Index Pattern Naming
--------------------

Index patterns in Kibana should follow the same naming scheme as aliases in ES (see [Aliases Naming](#Aliases-Naming) section). This way, is easy to know what alias is being used by a given index pattern. Besides, it makes easier to select index patterns from kibana, because their names include the field configured for time series in that index pattern. 


How this info was retrieved
---------------------------

These json files were retrieved taking advantage of the toolchain provided in the grimoirelab project in GitHub. Specifically the script GrimoireELK/utils/kidash.py.

Example of how to run this:

```

 $ ./kidash.py -e https://<user>:<password>@<domain>:443/<path>/ --dashboard <dashboard_name> --export <export_path>/<file_name>.json

```
