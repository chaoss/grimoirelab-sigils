Generic Dashboards for GrimoireLab
==================================

Each of the files found in this directory are a JSON file that contains all of the information related to a Kibana dashboard.
This usually has information about the following artifacts:
* Original indexes where the information come from.
* Searches on those indexes that provide a sub-set of the information.
* Widgets either built on top of the original indexes or on top of the searches.
* Final panels that are an aggregation of several widgets.

There are Dashboards for Kibana 4 and Kibana 5 right now stored in:
* `dashboards`: kibana 4 versions.
* `dashboards5`: kibana 5 versions.

Panels
------

A panel is composed by the several widgets this contains.
So far the panels proposed as generic are a mix of the several data sources available in a project. Those could be only focused on Git, but there are others such as review systems like Gerrit, IRC channels, mailing lists, etc.

The structure for naming files should be:
* For data sources: 
```
<data_source>[-<panel_name>][-<filters>].json

Examples:
git-<filters>.json
gerrit-<filters>.json
```
* For other panels not focused on particular data sources we just use the name of the panel:
```
<panel_name>[-<filters>].json

Examples:
about.json
overview-<filters>.json
```
Note: `<filters>` part is described in next section ([Filters Naming](#filters-naming))

To give some examples, below there is a list of some panels that can be found in this directory:
* git-'filters'.json: provides aggregated information about all of the gits in the analysis. Project/, repository, domains or organizations can be provided for filtering purposes.
* gerrit-'filters'.json: provides aggregated information from all of the gerrit projects. Project/, repository, domains or organizations can be provided for filtering purposes.
* gerrit-backlog-'filters'.json: provides specific widgets to track the backlog of the project with the addition of several filters per project or repository.
* mailinglists-'filters'.json: provides information about the discussions that take place in the several mailing lists.
* about.json: provides some widgets detailing this information and how to interact with the panels.
* overview-'filters'.json: provides a generic view of the dataset with some widgets that help to drill down the information from the whole list of data sources.

Filters Naming
--------------

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

In general, titles should follow the same naming scheme as the widget itself, substituting underscore characters by single spaces and adding capital letters. Nevertheless, **widgets title depends on the name of the panel** in which the widgets are located: 

- **If the panel shows information for several data sources, then the name of the data source must be included**. For example, it's the case of Data Status Panel, because it contains the same information per data source, so using data source name in title is mandatory.  

- **If the name of the data source is included in the title of the panel, then the name of the data source shouldn't be included in widgets' title**, except in cases where it could help understand what the widget contains.


```
 <data_source> <metric_used>
 
 Example: 
   Same visualization for top authors would be named: 
 
   - 'Top Authors' in 'Git' panel, as the panel is giving us context.
   - 'Git Top Authors' in 'Overview' panel where we could have similar visualizations for other data sources.
```

Searches Naming
---------------

```
Search:_<field>:<search>

Example: Search:_pull_request:true
```


Indexes Naming
--------------
Raw indexes should use suffix `-raw`:
```
<data_source>-raw

Example: git-raw
Example: gerrit-raw
Example: stackoverflow-raw
Example: jira-raw
Example: bugzilla-raw
```
Enriched indexes should use just the name of the data source:
```
<data_source>

Example: git
Example: gerrit
Example: stackoverflow
Example: jira
Example: bugzilla
```

Aliases Naming
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

Index patterns in Kibana should follow the same naming scheme as aliases in ES (see [Aliases Naming](#aliases-naming) section). This way, is easy to know what alias is being used by a given index pattern. Besides, it makes easier to select index patterns from kibana, because their names include the field configured for time series in that index pattern. 


Common Index Fields
-------------------

Following fields that should be included in any index pattern:

* id
* url
* metadata__timestamp
* metadata__updated_on
* author_bot
* author_name
* author_org_name
* author_uuid
* author_domain
* author_user_name
* origin
* grimoire_creation_date


Data model
----------

Each of the indexes are based on a previous definition. This
is declared in CSV format with two columns: name and type.

More information at the [Schema README](schema/README.md) file.


How this info was retrieved
---------------------------

These json files were retrieved taking advantage of the toolchain provided in the grimoirelab project in GitHub. Specifically the script GrimoireELK/utils/kidash.py.

Example of how to run this:

```

 $ ./kidash.py -e https://<user>:<password>@<domain>:443/<path>/ --dashboard <dashboard_name> --export <export_path>/<file_name>.json

```
