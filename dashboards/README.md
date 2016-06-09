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
* git.json: provides aggregated information about all of the gits in the analysis. Project/, repository, domains or organizations can be provided for filtering purposes.
* gerrit.json: provides aggregated information from all of the gerrit projects. Project/, repository, domains or organizations can be provided for filtering purposes.
* gerrit-backlog.json: provides specific widgets to track the backlog of the project with the addition of several filters per project or repository.
* mailinglists.json: provides information about the discussions that take place in the several mailing lists.
* about.json: provides some widgets detailing this information and how to interact with the panels.
* overview.json: provides a generic view of the dataset with some widgets that help to drill down the information from the whole list of data sources.

How this info was retrieved
---------------------------

These json files were retrieved taking advantage of the toolchain provided in the grimoirelab project in GitHub. Specifically the script GrimoireELK/utils/kidash.py.

Example of how to run this:

```

 $ ./kidash.py -e https://<user>:<password>@<domain>:443/<path>/ --dashboard <dashboard_name> --export <export_path>/<file_name>.json

```
