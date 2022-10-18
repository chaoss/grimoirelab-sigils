Generic Dashboards for GrimoireLab
==================================

Each of the files found in this directory are a JSON file that contains all of the information related to a Kibana dashboard.
This usually has information about the following artifacts:
* Original indexes where the information come from.
* Searches on those indexes that provide a sub-set of the information.
* Widgets either built on top of the original indexes or on top of the searches.
* Final panels that are an aggregation of several widgets.

There are Dashboards for Kibana 6 right now stored in `panels/json`

Panels
------

A panel is composed by the several widgets this contains.
So far the panels proposed as generic are a mix of the several data sources available in a project. Those could be only focused on Git, but there are others such as review systems like Gerrit, IRC channels, mailing lists, etc.

The structure for naming files should be:
* For data sources: 
```
<data_source>[_<panel_name>].json

Examples:
git_<panel_name>.json
gerrit_<panel_name>.json
```
* For other panels not focused on particular data sources we just use the name of the panel:
```
<panel_name>.json

Examples:
about.json
overview.json
git.json
git_pair_programming.json
gerrit.json
gerrit_timing.json
```
To give some examples, below there is a list of some panels that can be found in this directory:
* git.json: provides aggregated information about all of the gits in the analysis.
* gerrit.json: provides aggregated information from all of the gerrit projects.
* gerrit-backlog.json: provides specific widgets to track the backlog of the project.
* mailinglists.json: provides information about the discussions that take place in the several mailing lists.
* about.json: provides some widgets detailing this information and how to interact with the panels.
* overview.json: provides a generic view of the dataset with some widgets that help to drill down the information from the whole list of data sources.

All panels will provide widgets for filtering information by project, domain, organization, etc. depending on the availability of that information in the corresponding index.

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

Of course this is a general rule, just have context into account with naming widgets to know if data source is clear or not.

Searches Naming
---------------

```
Search:_<field>:<search>

Example: Search:_pull_request:true
```


Indexes Naming
--------------
Notice that optional date is included to allow keeping several copies of the same data source when needed.

Raw indexes should use suffix `-raw`:
```
<data_source>-raw[_date]

Example: git-raw
Example: gerrit-raw
Example: stackoverflow-raw
Example: jira-raw
Example: bugzilla-raw
```
Enriched indexes:
```
<data_source>_enriched[_date]

Example: git_enriched
Example: gerrit_enriched
Example: stackoverflow_enriched
Example: jira_enriched
Example: bugzilla_enriched
```

Aliases Naming
--------------

Finally, an alias should be created pointing to the enriched index. This allows to easily modify the data used under the hood in a transparent way from the point of view of panels. Its name should be just the name of the data source, but sometimes we need different indexes for the same data source. In that case we would add a suffix to indicate the functionality of that alias.
```
<data_source>

Example: git
Example: gerrit
Example: stackoverflow
Example: jira
Example: bugzilla
```

For each index there could be as many aliases as needed. The most usual use case is using aliases for building panels or visualizations based on different time series. E.g.:
```
<data_source>_<field_name>

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

More information at the [Schema](https://github.com/chaoss/grimoirelab-elk/tree/master/schema) directory.


How this info was retrieved
---------------------------

These json files were retrieved using [Kidash](https://github.com/chaoss/grimoirelab-kidash).

Example of how to run this:

```
$ kidash -g -e <elasticsearch-url> --dashboard <dashboard-id>* --export <local-file-path> --split-index-patterns

example: 
$ kidash -g -e https://admin:admin@localhost:9200 --dashboard overview --export overview.json --split-index-patterns
```

More information: [Kidash - Usage](https://github.com/chaoss/grimoirelab-kidash#usage).
